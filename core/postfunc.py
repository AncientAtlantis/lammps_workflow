import os
import json
import subprocess
import shlex

from core.prefunc import check_lammps_inputs
from core.default_config import nprocess,lmp_exe


'''
global checking procedure for subsequent stages of preprocessing
'''

def check_pre(src,tag_file):
    if not (os.path.exists(src) and (os.path.isabs(src))):
        print('Error, preprocessing not completed, aborting')
        return False

    tag=os.path.join(src,tag_file)
    if not os.path.exists(tag):
        print('Error, preprocessing not completed, aborting')
        return False

    with open(os.path.join(src,tag),'r') as f: 
        tag=json.load(f)

    types=list(tag.values())
    cond_has_script='lammps_input' in types
    for f,t in tag.items():
        cond_has_file=os.path.exists(f) and os.path.isfile(f)
        if not (cond_has_file and cond_has_script):
            print('Error, preprocessing results were corrupted, aborting')
            return False

    return check_lammps_inputs(src,tag_file)


def default_lammps_run(src,tag):
    with open(os.path.join(src,tag),'r') as f:
        tag=json.load(f)
    
    files=list(tag.keys())
    types=list(tag.values())
    
    script=files[types.index('lammps_input')]

    cwd=os.getcwd()
    os.chdir(src)
    command=shlex.split(f'mpirun -n {nprocess} {lmp_exe} -in {script}')
    try:
        subprocess.run(command,check=True,text=True)
    except Exception as e:
        print(f'Error on lammps running, {e}')
        os.chdir(cwd)
        return False

    os.chdir(cwd)
    return True
        

if __name__=='__main__':
    pass
    #test block

