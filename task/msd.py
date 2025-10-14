import os
import json
from core.util import *

def pre_msd(task_folder,task,tag):
    #locate lammps input script
    with open(os.path.join(task_folder,tag)) as f:
        file_tag=json.load(f)
    file_names=list(file_tag.keys())
    file_types=list(file_tag.values())

    input_script=file_names[file_types.index('lammps_input')]
    
    #locate the msd computation in lammps script
    commands,args=parse_lammps_script(input_script)
    cond_msd=check_msd(commands,args)

    if not cond_msd:
        print('Error, not enough output info for msd computation, aborting')
        return False

    return True


def post_msd(task_folder,task,tag):
    
    pass

#def run_msd(task_folder,task,tag):
#    
#    pass


