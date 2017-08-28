import plotproject
from project import project
import matplotlib.pyplot as plt

projects_directory = './TestProjecten/'
p=project()
p.load('oud project', projects_directory)

plotproject.progress(p)
plotproject.table_tasklist(p)
p.set_task_status('plan opstellen', 'brainstorm resultaten verwerken','done')
plotproject.progress(p)
plt.show()