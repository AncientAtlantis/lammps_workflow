import os
import sys
import argparse

from core.base_workflow import *

def main():
    '''
    Usage:
        python main -d destination-folder -i input1 input2 ... -o output-file -t task-name -p process
    '''

    parser = argparse.ArgumentParser(description='Lammps Workflow Main Procedure')
    
    #required parameters
    parser.add_argument('-d', '--destination', type=str, required=True, help='Lammps计算任务的工作路径')
    parser.add_argument('-i', '--inputs', nargs='+',required=True,type=str, help='Lammps计算的输入文件名列表')
    parser.add_argument('-o', '--output', nargs=1,required=True,type=str, help='Lammps计算的输出文件名称')
    parser.add_argument('-t', '--task', choices=['density', 'ke', 'pe','etotal','press', 'T','msd','deff','CN','rdf'], required=True, help='任务类型')
    parser.add_argument('-p', '--process', choices=['pre', 'run', 'post'], required=True, help='处理类型: pre (预处理), run (运行计算), post (后处理)')

    #optional parameters
    parser.add_argument('-j', '--slurm_jobid', type=str, help='Slurm作业ID，用于后处理阶段')
    
    #resolve parameters    
    args = parser.parse_args()
    if not args.destination:
        print('未提供 Lammps 计算任务的工作路径！')
        exit(-1)
    work_path = os.path.abspath(args.destination)

    #execute commands
    if args.process == 'pre':
        #preprocessing
        pre_lammps(work_path, args)
    elif args.process == 'run':
        #running 
        run_lammps(work_path, args)
    elif args.process == 'post':
        #postprocessing
        if args.slurm_jobid:
            post_lammps(work_path, args, args.slurm_jobid)
        else:
            post_lammps(work_path, args)

if __name__ == '__main__':
    #the entrance
    main()

