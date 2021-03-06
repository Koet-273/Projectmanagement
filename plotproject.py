import matplotlib.pyplot as plt
from project import task_status
import pandas as pd

def progress(proj):
    packagelist = proj.get_workpackages()
    tasklist = proj.get_tasklist()
    packagenames = packagelist.workpackage[::-1] # reverse order, to get first wp on top
    donebar = [100 * get_done_weight(tasklist, wp)/ get_total_weight(tasklist, wp) for wp in packagenames]
    plt.figure()
    plt.barh(range(len(packagenames)), donebar)
    plt.xlim(0,100)
    plt.xlabel('% complete')
    plt.title(proj.name())
    plt.yticks(range(len(packagenames)), packagenames)
    plt.tight_layout()
    plt.draw()


def table_tasklist(proj):
    packagelist = proj.get_workpackages()
    tasklist = proj.get_tasklist()
    for wp in packagelist.workpackage:
        print('')
        print('workpackage ' + wp)

        maxwidth, outputformat = create_output_format(tasklist, wp)
        doinglist, donelist, todolist = split_task_list(tasklist, wp)

        print(outputformat.format('to do', 'doing', 'done'))
        print('-'.rjust(3*maxwidth+7,'-'))

        for i in range(len(todolist)):
            print(outputformat.format(todolist[i], doinglist[i], donelist[i]))


def split_task_list(tasklist, wp):
    todolist = list(tasklist[(tasklist.workpackage == wp) & (tasklist.status == task_status.todo)]['task'].values)
    doinglist = list(tasklist[(tasklist.workpackage == wp) & (tasklist.status == task_status.doing)]['task'].values)
    donelist = list(tasklist[(tasklist.workpackage == wp) & (tasklist.status == task_status.done)]['task'].values)

    length = max(len(todolist), len(doinglist), len(donelist))
    todolist.extend([''] * (length - len(todolist)))
    doinglist.extend([''] * (length - len(doinglist)))
    donelist.extend([''] * (length - len(donelist)))

    return doinglist, donelist, todolist


def create_output_format(tasklist, wp):
    tasks = list(tasklist[(tasklist.workpackage == wp)]['task'].values)
    maxwidth = len(max(tasks, key=len))
    outputformat = '{{:>{:d}}} | {{:>{:d}}} | {{:>{:d}}}'.format(maxwidth, maxwidth, maxwidth)
    return maxwidth, outputformat


def get_total_weight(tasklist, workpackage):
    return tasklist[tasklist.workpackage == workpackage]['size'].sum()

def get_done_weight(tasklist, workpackage):
    return tasklist[(tasklist.workpackage == workpackage) & (tasklist.status == 'done')]['size'].sum()