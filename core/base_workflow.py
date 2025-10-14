import os
import sys
import json
import importlib

from ase.io import read,write
from shutil import copyfile
from core.util import ensure_path_exist
from core.prefunc import *
from core.postfunc import *


#map from task name to task module name
task_map={'density':'thermo', 'ke':'thermo', \
          'pe':'thermo','etotal':'thermo','press':'thermo', \
          'T':'thermo','msd':'msd','deff':'deff','CN':'CN','rdf':'rdf'}

default_tag='lammps_file_tag'


def _load_and_run_task(module_name,procedure_name,*arg):
    try:
        module=importlib.import_module(module_name)
        task_procedure=getattr(module,procedure_name)
        if not task_procedure(*arg):
            exit_info()
            return False
    except ImportError:
        print(f'Error, module {module_name} does not exist')
        return False
    except AttributeError:
        print(f'Error, no {procedure_name} was found in module {module_name}')
        return False
    except Exception as e:
        print(f"Error: procedure call {stage}_{module_name}() error: {e}") 
        return False

    return True

def pre_lammps(work_path,arg,tag=default_tag):
    '''
    general preprocessing procedure of lammps

    work_path: expect an absolute path of root working directory
    arg.inputs: absolute paths or file names for lammps input script, data and forcefield file
                they were assumed to be located in work_path if simple file names were provided
    '''

    task,stage=arg.task,arg.process
    exit_info=lambda :print(f'Preprocessing task {task} failed\n')
  
    print(f'Start preprocessing {task}')
    #ensure the root working directory exists
    if not os.path.exists(work_path):
        os.mkdirs(work_path)

    #grep the absolute locations of input files
    sources=[]
    for input_file in arg.inputs:
        #simple file
        if os.path.sep not in input_file:
            searching=os.path.join(work_path,input_file)
        #assumed as a path
        else:
            searching=input_file

        if os.path.isabs(os.path.dirname(searching)) and os.path.isfile(searching):
            sources.append(searching)
        else:
            print(f'Error: could not locate lammps input file {input_file}, aborting')
            exit_info()
            sys.exit(-1)

    #build and initialize the task folder
    task_folder=os.path.join(work_path,'run')
    ensure_path_exist(task_folder,True) # clean the task folder if already exists
    for src in sources:
        file_name=os.path.basename(src)
        copyfile(src,os.path.join(task_folder,file_name))

    #write the tag file for describing the type, name, and format of task input and output files
    task_src=[os.path.join(task_folder,os.path.basename(src)) for src in sources]
    file_tag=resolve_file_tag(task_src)
    with open(os.path.join(task_folder,tag),'w') as f:
        json.dump(file_tag,f)

    #general preprocessing procedure
    if not check_lammps_inputs(task_folder,tag):
        exit_info()
        sys.exit(-1)

    #task dependent prepocessing procedure
    reg_task_name=list(task_map.keys())
    reg_module_name=list(task_map.values())
    if task in reg_task_name:
        module_name=task_map[task] 
        procedure_name=f'{stage}_{module_name}'
        if not _load_and_run_task(f'task.{module_name}',procedure_name,task_folder,task,tag):
            exit_info()
            sys.exit(-1)
    else:
        print(f'Error: unrecognized task name {task}, aborting')    
        exit_info()
        sys.exit(-1)

    print(f'Preprocessing succeed\n')


def run_lammps(work_path,arg,tag=default_tag):
    '''
    General lammps submitting procedure
    '''
    task,stage=arg.task,arg.process

    print(f'Start running {task}')

    exit_info=lambda :print(f'Running task {task} failed\n')
    run_path=os.path.join(work_path,'run')


    #whether preprocessing is completed
    if not check_pre(run_path,tag):
        exit_info()
        sys.exit(-1)
    
    #the task dependent running procedure
    module_name=task_map[task]
    procedure_name=f'{stage}_{module_name}'
    if not _load_and_run_task(f'task.{module_name}',procedure_name,run_path,task,tag):
        #the default running procedure
        print('    fall back to default submitting procedure')
        if not default_lammps_run(run_path,tag):
            exit_info()
            sys.exit(-1)

    print(f'Running succeed\n')


def post_lammps(work_path,arg,slurm_jobid=None):
    pass


