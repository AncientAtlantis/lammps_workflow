# Materials Chemistry  Agent Tools
## 代码说明
自动化执行 LAMMPS 分子动力学模拟计算的工作流工具。将完整的 LAMMPS 计算过程分为三个标准化阶段：

前处理 (pre)：准备输入文件并检查计算参数

运行计算 (run)：提交 LAMMPS 计算任务

后处理 (post)：提取和分析计算结果

## 计算场景说明

（例如：我需要计算xx的压力。我需要计算水的势能...）这样的。

## 基本用法
```
python main.py -d <工作路径> -i <输入文件> -o <输出文件> -t <任务类型> -p <处理阶段>
```

## 参数说明
```bash
必需参数：
  -d, --destination DIR    LAMMPS 计算任务的工作路径
  -i, --inputs FILES       LAMMPS 计算的输入文件名列表，至少需要指定一个文件，并需提前放置于destination DIR
  -o, --output FILE        LAMMPS 计算的输出文件名称，仅支持一个文件
  -t, --task TASK          任务类型: density, ke, pe, etotal, press, T, msd, deff, CN, rdf
  -p, --process PROCESS    处理类型: pre, run, post

可选参数：
  -j, --slurm_jobid ID     Slurm 作业 ID，用于后处理阶段
```

python main.py -i ./POSCAR -p pre -t relax 
python main.py -i ./POSCAR -p post -t relax 

python main.py -i ./POSCAR -p pre -t scf 
python main.py -i ./POSCAR -p post -t scf 

python main.py -i ./POSCAR -p pre -t dos 
python main.py -i ./POSCAR -p post -t dos

python main.py -i ./POSCAR -p pre -t PBE_band 
python main.py -i ./POSCAR -p post -t PBE_band

python main.py -i ./POSCAR -p pre -t elastic 
python main.py -i ./POSCAR -p post -t elastic

python main.py -i ./POSCAR -p pre -t absorption 
python main.py -i ./POSCAR -p post -t absorption

python main.py -i ./POSCAR -p pre -t bader
python main.py -i ./POSCAR -p post -t bader

python main.py -i ./POSCAR -p pre -t magnetic
python main.py -i ./POSCAR -p post -t magnetic
```
