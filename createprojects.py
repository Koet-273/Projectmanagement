from project import project, task_status
from projectlist import ProjectList

projects_directory = './TestProjecten/'

myprojlist = ProjectList(projects_directory)

p = project('testproject', 3)
p._priority = 100000
p.add_task('Plan opstellen','eerste voorstel schrijven')
p.add_workpackage('Plan opstellen')
p.add_workpackage('Plan uitvoeren')
p.add_workpackage('Plan nabespreken')
p.insert_workpackage('team samenstellen', 2)
p.add_workpackage('Financiering regelen')
p.repos_workpackage('Financiering regelen',1)

p.add_task('Plan opstellen','eerste voorstel schrijven')
p.add_task('Plan opstellen','eerste voorstel schrijven')
p.add_task('Plan opstellen','commentaar verwerken')
p.add_task('Financiering regelen','Bedelen op straathoek')
p.remove_task('Plan opstellen','eerste voorstel schrijven')
p.remove_task('Plan opstellen','sedfsvs')
p.add_task('team samenstellen', 'aertf')
p.remove_workpackage('team samenstellen')
myprojlist.save_project(p)
p.print()


p2 = project('oud project',2)
p2.add_workpackage('plan opstellen')
p2.add_workpackage('groep verzamelen')

p2.add_task('groep verzamelen','namenlijst maken',1,task_status.doing)
p2.add_task('groep verzamelen','eerste vergadering plannen', 2)
p2.add_task('plan opstellen','brainstorm houden',3)
p2.add_task('plan opstellen','brainstorm resultaten verwerken',4)
p2.remove_task('plan opstellen','brainstorm houden')
p2.set_task_status('groep verzamelen', 'namenlijst maken',task_status.done)
myprojlist.save_project(p2)
p2.print()


p3 = project('Groot project',1)
p3.add_workpackage('groep verzamelen')
p3.add_workpackage('plan opstellen')
p3.add_workpackage('Uitvoer')
p3.add_workpackage('Afronden')

p3.add_task('groep verzamelen','namenlijst maken',1,task_status.doing)
p3.add_task('groep verzamelen','eerste vergadering plannen', 2, task_status.done)
p3.add_task('plan opstellen','brainstorm houden',3,task_status.done)
p3.add_task('plan opstellen','brainstorm resultaten verwerken',4,task_status.doing)
p3.add_task('plan opstellen','grafieken maken',4,task_status.doing)
p3.add_task('plan opstellen','2de brainstorm houden',2,task_status.todo)
p3.add_task('plan opstellen','2de brainstorm resultaten vewerken',2,task_status.todo)
p3.add_task('plan opstellen','plan presenteren',4,task_status.todo)
p3.add_task('Uitvoer','Dingen die ik nog niet weet',100)
p3.add_task('Afronden','Dingen die ik nog niet weet',20)

myprojlist.save_project(p3)
p3.print()
myprojlist.print()