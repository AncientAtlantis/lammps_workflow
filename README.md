# Materials Chemistry  Agent Tools
## 代码说明


## 计算场景说明

## 计算场景的情景

（例如：我需要计算xx的压力。我需要计算水的势能...）这样的。

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
