import os
import json
from project import project

class project_list:
    _project_dict = {}
    _directory    = ''
    def __init__(self, directory):
        self._directory = directory
        self._project_dict = self.get_project_list(directory)

    def project_exists(self, name):
        return name in self._project_dict

    def get_project_list(self, directory):
        filename = os.path.join(directory, 'projectlist.dat')
        if os.path.isfile(filename):
            return json.load(open(filename))
        else:
            return {}

    def get_project_byname(self, name):
        newproject = project()
        newproject.load(name, self._directory, self._project_dict[name][0], self._project_dict[name][1])
        return newproject

    def write_to_projectlist(self, directory, name, status, priority):
        self._project_dict[name] = (status, priority)
        filename = os.path.join(directory, 'projectlist.dat')
        json.dump(self._project_dict, open(filename, 'w'))

    def read_project_properties(self, directory, name):
        if name in self._project_dict:
            return self._project_dict[name]
        else:
            return ('none','none')

    def save_project(self, project):
        if not os.path.isdir(self._directory):
            os.makedirs(self._directory)
        self.write_to_projectlist(self._directory, project._name, project._status, project._priority)
        project.save(self._directory)

    def print(self):
        print(self._project_dict)