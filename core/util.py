import os
from shutil import rmtree

'''
checking procedures for lammps input file contents
'''


def ensure_path_exist(path,clean):
    if os.path.exists(path):
        if clean:
            rmtree(path)
    
    os.makedirs(path)
  

#the common lammps commands
lmp_ini=['units', 'dimension', 'boundary', 'atom_style', 'newton', \
         'processors', 'atom_modify']
lmp_self_build_model=['lattice', 'create_box', 'create_atoms', 'read_restart',\
                      'read_dump']
lmp_model=['lattice', 'region', 'create_box', 'create_atoms', 'read_data', 'read_restart', \
           'read_dump', 'replicate', 'delete_atoms', 'displace_atoms', 'molecule', 'change_box']
lmp_force=['pair_style', 'pair_coeff', 'bond_style', 'bond_coeff', 'angle_style', 'angle_coeff', \
           'dihedral_style', 'dihedral_coeff', 'improper_style', 'improper_coeff', 'kspace_style', \
           'special_bonds', 'dielectric']
lmp_gen=['neighbor', 'neigh_modify', 'group', 'timestep', 'reset_timestep', 'run_style', 'min_style', \
         'min_modify', 'mass', 'velocity', 'set']
lmp_cons=['fix', 'fix_modify', 'compute', 'compute_modify', 'variable']
lmp_out=['thermo', 'thermo_style', 'thermo_modify', 'dump', 'dump_modify', 'restart', 'write_restart',\
         'write_data', 'print']
lmp_exe=['minimize', 'temper']
lmp_flow=['clear', 'if', 'then', 'else', 'label', 'next', 'jump', 'include', 'log', 'quit', 'shell']
lmp_tot=set(lmp_ini)|set(lmp_self_build_model)|set(lmp_model)|set(lmp_force)|set(lmp_gen)|set(lmp_cons)|set(lmp_out)|set(lmp_exe)|set(lmp_flow)
lmp_tot=list(lmp_tot)


def parse_lammps_script(src):
    with open(src,'r') as f:
        text=f.read()
        #expand commands within single line
        text=text.replace(';','\n')

        #compact multiple line to single one
        compact_text=[]
        flag=False
        for c in text:
            if c=='&':
                flag=True 
            if flag==True and c=='\n':
                flag=False
                compact_text.append(' ')
                continue
            if not flag:
                compact_text.append(c)
        text=''.join(compact_text)
        lines=text.split('\n')
        
        #remove comment
        lines=[line.strip() for line in lines if not line.strip().startswith('#')]
        lines=[line for line in lines if len(line)>1]
        lines=[line.split('#')[0] for line in lines]
        lines=[line.split('\n')[0] for line in lines]

    #parse inputs
    parsed_line=[line.split() for line in lines]
    
    #parse lammps commands and arguments
    commands=[item[0] for item in parsed_line]
    args=[item[1:] for item in parsed_line]

    return commands,args


def extract_commands(input_script):
    commands,args=parse_lammps_script(input_script)

    return commands 


#determain whether rdf and coordination number 
#computation were definded in lammps inputs
def check_rdf(commands,args):
    #locate the rdf computation in lammps script
    inds=[i for i,com in enumerate(commands) if com=='compute']
    inds=[i for i in inds if args[i][2]=='rdf']
    cond_rdf_comp=len(inds)!=0

    #if no compute were defined, at least one dump should be defined
    inds=[i for i,com in enumerate(commands) if com=='dump']
    cond_rdf_dump=len(inds)!=0

    cond_rdf=cond_rdf_comp|cond_rdf_dump

    return cond_rdf

#determain whether msd and deffusion 
#computation were definded in lammps inputs
def check_msd(commands,args):
    #locate the msd computation in lammps script
    inds=[i for i,com in enumerate(commands) if com=='compute']
    inds=[i for i in inds if args[i][2]=='msd']
    cond_msd_comp=len(inds)!=0

    #if no compute were defined, at least one dump should be defined
    inds=[i for i,com in enumerate(commands) if com=='dump']
    cond_msd_dump=len(inds)!=0

    cond_msd=cond_msd_comp|cond_msd_dump

    return cond_msd


def parse_lammps_log(src):
    is_data=False
    data_header=[]
    data_sections=[]

    for line in open(src,'r'):
        pass    

