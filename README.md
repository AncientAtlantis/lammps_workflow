# Materials Chemistry  Agent Tools
## 新加了 弹性模量 吸收光谱 bader电荷三个模块

## 添加了临时 .vaspkit 配置文件
在 core/Function.py 中添加了 get_vaspkit_config 函数，用于获取 .vaspkit 配置文件
在32行
        project_root = str(Path("/root/aiagent/work_flow/vasp"))
把这个路径改成保存配置文件.vaspkit的目录
.vaspkit 文件 主要改下面两行

```
# 从默认的 AUTO_PLOT = .False. 改成 .True. 
AUTO_PLOT                     =     .TRUE.  
# 添加一个当前python的绝对路径
PYTHON_BIN = <python 的绝对路径>
```

## 用法
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

## 检查逻辑
现在relx之外的所有任务，都先检查relax目录下结果是否可用，可用则使用relax目录下结果，否则使用-i POSCAR或其他.cif .vasp文件
