import plotproject
from project_list  import project_list
import matplotlib.pyplot as plt

projects_directory = './TestProjecten/'

myprojlist = project_list(projects_directory)
p = myprojlist.get_project_byname('Groot project')

plotproject.progress(p)
plotproject.table_tasklist(p)
p.set_task_status('plan opstellen', 'brainstorm resultaten verwerken','done')
plotproject.progress(p)
plt.show()
print('folkert')