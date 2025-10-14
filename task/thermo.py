import os
import sys
import json

from core.util import *

def _parse_thermo_keywords(commands,args):
    thermo_keywords_map={'one':'step temp epair emol etotal press'.split(),
                         'yaml':'step temp epair emol etotal press'.split(),
                         'multi':'etotal ke temp pe ebond eangle edihed eimp evdwl ecoul elong press'.split()}

    try:
        inds=len(commands)-commands[::-1].index('thermo_style')-1
    except:
        inds=None

    thermo_style=args[inds][0] if inds else 'one'

    if thermo_style=='custom':
        thermo_keywords=args[inds][1:] 
    else:
        thermo_keywords=thermo_keywords_map[thermo_style]

    return thermo_keywords


def pre_thermo(task_folder,task,tag):
    #locate lammps input script
    with open(os.path.join(task_folder,tag)) as f:
        file_tag=json.load(f)
    file_names=list(file_tag.keys())
    file_types=list(file_tag.values())
    input_script=file_names[file_types.index('lammps_input')]

    #determain the thermo output info
    commands,args=parse_lammps_script(input_script)
    thermo_keywords=_parse_thermo_keywords(commands,args)

    if task in ['etotal','press','T']:
        pass
    elif task in ['ke','pe']:
        if task not in thermo_keywords:
            print('Error, thermo keyword {task} not specified in lammps script, aborting')
            return False
    elif task=='density':
        cond_density=task in thermo_keywords     
        cond_vol='vol' in thermo_keywords
        cond_size=('lx' in thermo_keywords) and ('ly' in thermo_keywords) and ('lz' in thermo_keywords)

        density_valid=cond_density|cond_vol|cond_size

        if not density_valid:
            print('Error, not enough output info to determain density, aborting')
            return False
    else:
        pass

    return True


def post_thermo(task_dir,tag):
    pass

#def run_thermo(task_dir,tag):
#    pass


