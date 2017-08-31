import os
import json
from project import project
from collections import namedtuple
import pandas as pd

project_status_tuple = namedtuple('project_status_tuple', ['active', 'closed'])
project_status = project_status_tuple('active', 'closed')

class ProjectList:
    _project_list = pd.DataFrame(columns=['AOI', 'name','priority', 'status'])
    _directory = ''

    def __init__(self, directory):
        self._directory = directory
        self.load_project_list(directory)

    def project_exists(self, name):
        return name in self._project_list.name

    def load_project_list(self, directory):
        filename = os.path.join(directory, 'projectlist.dat')
        if os.path.isfile(filename):
            self._project_list = pd.read_csv(filename, index_col=0)

    def get_project_byname(self, name):
        newproject = project()
        project_series = self._project_list.loc[self._project_list.name == name].iloc[0]
        newproject._load_from_series(self._directory, project_series.iloc[0])
        return newproject

    def write_to_projectlist(self,  AOI, name, status, priority):
        self._project_list.append = ({'AOI': AOI, 'name': name, 'status': status, 'priority': priority})
        filename = os.path.join(self._directory, 'projectlist.dat')
        self._project_list.to_csv(filename)

    def save_project(self, project):
        if not os.path.isdir(self._directory):
            os.makedirs(self._directory)
        self.write_to_projectlist(project._AOI, project._name, project._status, project._priority)
        project._save(self._directory)

    def print(self):
        print(self._project_list)