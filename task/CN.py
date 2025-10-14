import os
import json
from core.util import *

def pre_CN(task_folder,task,tag):
    #locate lammps input script
    with open(os.path.join(task_folder,tag)) as f:
        file_tag=json.load(f)
    file_names=list(file_tag.keys())
    file_types=list(file_tag.values())

    input_script=file_names[file_types.index('lammps_input')]
    
    #locate the rdf computation in lammps script
    commands,args=parse_lammps_script(input_script)
    
    cond_CN=check_rdf(commands,args) 
    if not cond_CN:
        print('Error, not enough output info for coordination number, aborting')
        return False

    return True


def post_CN(task_folder,task,tag):
    
    pass


#def run_CN(task_folder,task,tag):
    
#    pass


