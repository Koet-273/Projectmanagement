import pandas as pd
import os
import numpy as np
from collections import namedtuple

task_status_tuple = namedtuple('task_status_tuple', ['todo', 'doing', 'done'])
task_status = task_status_tuple('todo', 'doing', 'done')

class project:
    _tasklist = pd.DataFrame(columns=['workpackage', 'task', 'status', 'size'])
    _wp = pd.DataFrame(columns=['workpackage','order'])
    _name = 'empty'
    _status = 1
    _priority = 1
    _AOI = 'General'

    def __init__(self, name='empty', priority=1):
        self._name = name
        self._priority = priority

    def _load_from_series(self, directory, projectseries):
        self._load(directory, projectseries.AOI, projectseries.name, projectseries.status, projectseries.priority)

    def _load(self, directory, AOI, name, status, priority):
        self._status = status
        self._priority =priority
        self._name = name
        self._AOI = AOI

        self._tasklist = pd.read_csv(os.path.join(directory, name, 'tasklist.csv'), index_col=0)
        self._wp = pd.read_csv(os.path.join(directory, name, 'workpackages.csv'), index_col=0)

    def _save(self, directory):
        project_dir, success = self.prepare_directory(directory)
        if success:
            self._tasklist.to_csv(os.path.join(project_dir, 'tasklist.csv'))
            self._wp.to_csv(os.path.join(project_dir,'workpackages.csv'))

    def prepare_directory(self, directory):
        success = False
        project_dir = ''
        if not os.path.isdir(directory):
            print('Directory \'{}\' does not exist'.format(directory))
            print('Save failed')
        else:
            project_dir = os.path.join(directory, self._name)
            if not os.path.isdir(project_dir):
                os.makedirs(project_dir)
            success = True
        return project_dir, success


    def add_workpackage(self,workpackage):
        self.insert_workpackage(workpackage, np.max(np.append(self._wp['order'].values, [0]))+1)

    def insert_workpackage(self, workpackage, position):
        if self.wp_exists(workpackage):
            print('workpackage \'{}\' alread exists'.format(workpackage))
        else:
            self.shift_positions(position)
            self._wp = self._wp.append({'workpackage': workpackage, 'order': position}, ignore_index = True)
            self.sort_workpackages()

    def sort_workpackages(self):
        if self._wp.order.size > 1:
            if self._wp.order.values[-2] > self._wp.order.values[-1:]:
                self._wp = self._wp.sort_values(by='order')

    def shift_positions(self, position):
        self._wp.loc[self._wp.order >= position, 'order'] += 1

    def repos_workpackage(self, workpackage, position):
        self._wp = self._wp.drop(self._wp[self._wp.workpackage == workpackage].index)
        self.insert_workpackage(workpackage, position)

    def remove_workpackage(self, workpackage):
        self._wp = self._wp.drop(self._wp[self._wp.workpackage == workpackage].index)
        self._tasklist = self._tasklist.drop(self._tasklist[self._tasklist.workpackage == workpackage].index)

    def add_task(self, workpackage, task, size = 1, status=task_status.todo):
        if self.task_exists(task, workpackage):
            print('Task \'{}\' already exists in workpackage \'{}\'.'.format(task, workpackage))
        elif self.wp_exists(workpackage):
            self._tasklist = self._tasklist.append({'workpackage': workpackage, 'task': task, 'status': status, 'size': size}, ignore_index = True)
        else:
            print('add workpackage \'{}\' first'.format(workpackage))

    def wp_exists(self, workpackage):
        return workpackage in self._wp.workpackage.values

    def task_exists(self, task, workpackage):
        return task in self._tasklist[self._tasklist.workpackage == workpackage].task.values

    def remove_task(self, workpackage, task):
        index = self.get_task_index(workpackage, task)
        if index.size==1:
            self._tasklist = self._tasklist.drop(index)
        elif index.size ==0:
            print('Task \'{}\' does not exist in workpackage \'{}\'.'.format(task, workpackage))
        else:
            raise RuntimeError('ERROR in remove_task: task exists twice in same workpackage')

    def set_task_status(self, workpackage, task, status):
        index = self.get_task_index(workpackage, task)
        self._tasklist.loc[index, 'status'] = status

    def get_tasklist(self):
        return  self._tasklist

    def get_workpackages(self):
        return  self._wp

    def name(self):
        return self._name

    def get_task_index(self, workpackage, task):
        return self._tasklist[(self._tasklist.workpackage == workpackage) & (self._tasklist.task == task)].index

    def print(self):
        print('--------------------')
        print('name: ' + self._name)
        print('--------------------')
        print('workpackages:')
        print(self._wp)
        print('--------------------')
        print('tasks:')
        print(self._tasklist)
        print('--------------------')
        print('status = {}'.format(self._status))
        print('--------------------')


