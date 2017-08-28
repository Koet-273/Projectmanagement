import os
import json


def project_exists(directory, name):
    dict = getprojectlist(directory)
    return name in dict

def getprojectlist(directory):
    filename = os.path.join(directory, 'projectlist.dat')
    return json.load(open(filename))

def write_to_projectlist(directory, name, status, priority):
    filename = os.path.join(directory, 'projectlist.dat')
    if os.path.isfile(filename):
        dict = json.load(open(filename, 'r'))
    else:
        dict = {}
    dict[name] = (status, priority)
    json.dump(dict, open(filename, 'w'))


def read_project_properties(directory, name):
    dict = getprojectlist(directory)
    if name in dict:
        return dict[name]
    else:
        return {}

