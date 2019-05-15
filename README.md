# GMDA-Project

This project was made in python 3.7 using windows. We do not ensure compatibility with other versions of python.

## Installation

#### To begin, let's clone the repository:
`git clone https://github.com/TheodoreAouad/GMDA-Project.git` <br/> `cd GMDA-Project`

#### Install the requirements in the folder requirements:
`pip install -r "requirements.txt"`

#### On Linux/MacOS:

#### On Windows:
`pip install requirements\lpsolve55-5.5.2.5-cp37-cp37m-win_amd64.whl`

## Use case

This project is composed of multiple .py files. Some are meant to be launched from the console while others are only modules.

#### To write a .lp file readable and solvable by the lp_solve app as for Q3):
`python file_writer.py "<path to first dataset.csv>" "<path to second dataset.csv>"` <br/>
The two datasets must be in a csv with each row being a point, each column a coordinate except the last column which is the weight of the point.

#### To compute the computation times Q4) of lp_solve and put them in a csv "times_q4.csv":
`python compute_time.py`

#### To view the results of Q4) on the computation times of lp_solve:
`python show_optim_times.py`

#### To view the different clusterings of Q6):
`python show_clusterings_graphs.py`

#### To compute the computation times Q6) of clusterings comparison and put them in a csv "clusterings_times.csv":
`python compute_clusterings_time.py`
