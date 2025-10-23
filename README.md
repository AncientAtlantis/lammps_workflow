# Materials Chemistry  Agent Tools
## 代码说明
自动化执行 LAMMPS 分子动力学模拟计算的工作流工具。将完整的 LAMMPS 计算过程分为三个标准化阶段：

前处理 (pre)：准备输入文件并检查计算参数

运行计算 (run)：提交 LAMMPS 计算任务

后处理 (post)：提取和分析计算结果

## 计算场景说明
该工作流支持以下 LAMMPS 计算任务：

density：体系密度，例如液态水的密度随时间的变化

ke：	体系动能，	监测模拟过程中体系的动能波动

pe：	体系势能，	监测模拟过程中体系的势能的波动

etotal：	体系总能量，	监测模拟过程中体系的势能的波动

press：	体系压力，	监测模拟过程中体系压力随时间的变化

T：	体系温度，	监测模拟过程中体系温度随时间的变化

msd：	体系均方位移，	给出模拟体系的均方位移的分量和总位移随时间变化

deff：	体系扩散系数，计算体系的扩散系数

CN：	体系配位数，	给出体系结构特征

rdf：	径向分布函数，	给出体系结构特征

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
## 场景示例
首先新建一个工作目录
```bash
mkdir lammps_sims 
cd lammps_sims
```
将准备好的输入文件放在工作目录下，执行
```bash
, msd, deff, CN, rdf

水分子动能计算：
python main.py -d . -i water_ke.in water.lmp -o log.lammps -t ke -p pre
python main.py -d . -i temp -o temp -t ke -p run
python main.py -d . -i temp -o log.lammps -t ke -p post

水分子势能计算：
python main.py -d . -i water_ke.in water.lmp -o log.lammps -t pe -p pre
python main.py -d . -i temp -o temp -t pe -p run
python main.py -d . -i temp -o log.lammps -t pe -p post

水分子总能量计算：
python main.py -d . -i water_ke.in water.lmp -o log.lammps -t etotal -p pre
python main.py -d . -i temp -o temp -t ke -p run
python main.py -d . -i temp -o log.lammps -t ke -p post

水分子压强计算：
python main.py -d . -i water_ke.in water.lmp -o log.lammps -t press -p pre
python main.py -d . -i temp -o temp -t press -p run
python main.py -d . -i temp -o log.lammps -t press -p post

水分子密度计算：
python main.py -d . -i water_ke.in water.lmp -o log.lammps -t density -p pre
python main.py -d . -i temp -o temp -t density -p run
python main.py -d . -i temp -o log.lammps -t density -p post

水分子温度计算：
python main.py -d . -i water_ke.in water.lmp -o log.lammps -t T -p pre
python main.py -d . -i temp -o temp -t T -p run
python main.py -d . -i temp -o log.lammps -t T -p post

水分子均方位移计算：
python main.py -d . -i water_ke.in water.lmp -o msd.data -t msd -p pre
python main.py -d . -i temp -o temp -t msd -p run
python main.py -d . -i temp -o msd.data -t msd -p post

水分子扩散系数计算：
python main.py -d . -i water_ke.in water.lmp -o msd.data -t deff -p pre
python main.py -d . -i temp -o msd.data -t deff -p run
python main.py -d . -i temp -o msd.data -t deff -p post

水分子径向分布函数计算：
python main.py -d . -i water_ke.in water.lmp -o rdf.data -t rdf -p pre
python main.py -d . -i temp -o temp -t rdf -p run
python main.py -d . -i temp -o rdf.data -t rdf -p post

水分子配位数计算：
python main.py -d . -i water_ke.in water.lmp -o rdf.data -t CN -p pre
python main.py -d . -i temp -o temp -t CN -p run
python main.py -d . -i temp -o rdf.data -t CN -p post
```
