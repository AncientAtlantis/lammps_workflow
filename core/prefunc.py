import os
import sys

import json
from ase.io import read,write
from core.util import lmp_tot,lmp_self_build_model,extract_commands

'''
global checking procedure of lammps input file
'''

def is_lammps_data(src):
    try:
        atoms=read(src,format='lammps-data')
    except:
        return False

    if len(atoms):
        return True
    return False


def is_lammps_input_script(src):
    '''
    whether a text file is lammps input script
    '''

    commands=extract_commands(src)      
    has_lammps_command=len(set(lmp_tot)&set(commands))!=0

    if 'run' in commands and has_lammps_command:
        return True

    return False 


def resolve_file_tag(sources):
    '''
    identify the lammps file type
    '''

    file_tag={}
    for src in sources:
        if is_lammps_data(src):
            file_tag[src]='lammps_data'
        elif is_lammps_input_script(src):
            file_tag[src]='lammps_input'
        else:
            file_tag[src]='other'

    return file_tag


def check_lammps_inputs(src_folder,tag):
    '''
    validation of lammps input files
    '''

    with open(os.path.join(src_folder,tag),'r') as f:
        file_tag=json.load(f)
    input_files=list(file_tag.keys())
    file_types=list(file_tag.values())

    #check the lammps script 
    if 'lammps_input' not in file_types:
        print('Error, no valid lammps input script was found, aborting')
        return False
    if file_types.count('lammps_input')>1:
        print('Warning, more than one lammps input scripts were identified, program behavior will be undetermained')

    #check the data file
    script=input_files[file_types.index('lammps_input')]
    commands=extract_commands(script)
    is_self_build=len(set(commands)&set(lmp_self_build_model))!=0
    if 'lammps_data' not in file_types and not is_self_build:
        print('Warning, simulation model was not build within lammps and no valid data file was found, the simulation is highly likely fail')
    if file_types.count('lammps_data')>1:
        print('Warning, more than one lammps data file were identified, program behavior will be undetermained')

    return True 

if __name__=='__main__':
    pass
    #test block

