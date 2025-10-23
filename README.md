# Materials Chemistry  Agent Tools
## 代码说明
自动化执行 LAMMPS 分子动力学模拟计算的工作流工具。将完整的 LAMMPS 计算过程分为三个标准化阶段：

前处理 (pre)：准备输入文件并检查计算参数

运行计算 (run)：提交 LAMMPS 计算任务

后处理 (post)：提取和分析计算结果

## 计算场景说明
支持的计算任务类型
该工作流支持以下 LAMMPS 计算任务：

任务类型	计算内容	典型应用场景

density	体系密度	我需要计算液态水的密度随温度的变化

ke	动能	我需要监测模拟过程中体系的动能波动

pe	势能	我需要计算蛋白质-配体复合物的结合势能

etotal	总能量	我需要验证能量守恒，检查模拟的稳定性

press	压力	我需要计算等温压缩过程中的体系压力
T	温度	我需要监控体系的温度平衡过程
msd	均方位移	我需要计算离子在电解质中的扩散系数
deff	扩散系数	我需要量化水分子的自扩散能力
CN	配位数	我需要分析金属熔体中原子的局部结构
rdf	径向分布函数	我需要研究液态金属的结构特征

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
