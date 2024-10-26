3080Ti 显卡 跑的话需要更改 ./Utils/PathPresettingOperator.get_dataset_path  该文件夹下的配置
```linux
root@autodl-container-7c5d4696fb-c54fea2a:~# git clone https://github.com/XLearning-SCU/2023-TPAMI-SMILE
Cloning into '2023-TPAMI-SMILE'...
remote: Enumerating objects: 148, done.
remote: Counting objects: 100% (148/148), done.
remote: Compressing objects: 100% (98/98), done.
remote: Total 148 (delta 42), reused 148 (delta 42), pack-reused 0 (from 0)
Receiving objects: 100% (148/148), 1.40 MiB | 2.65 MiB/s, done.
Resolving deltas: 100% (42/42), done.
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
CVCL  DIVIDE  Pro-Imp  SMILE  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# cd SMILE/
root@autodl-container-7c5d4696fb-c54fea2a:~/SMILE# ls
Clustering.py  DistComput.py  Exp3.png  LICENSE  QuickConfig  Temp.py   _AutoLauncher.py  _Utils             evaluate.py  loss.py  models.py           pvp_data_loader.py  sure_inference.py
DataSetMaster  Exp2.png       Fig2.png  Net.py   README.md    Temp.txt  _MainLauncher.py  classification.py  figures      main.py  psp_data_loader.py  run.py              utils.py
root@autodl-container-7c5d4696fb-c54fea2a:~/SMILE# python main.py --dataset NoisyMNIST30000 --seed 9116  --aligned_prop 1 --complete_prop 1
/root/SMILE/_Utils/DirectoryOperator.py:89: SyntaxWarning: invalid escape sequence '\]'
  """
Traceback (most recent call last):
  File "/root/SMILE/main.py", line 3, in <module>
    from DataSetMaster import dataset_master
  File "/root/SMILE/DataSetMaster/dataset_master.py", line 6, in <module>
    from DataSetMaster.data_loader import get_dataset_fair_clustering_mouxin, get_sn
  File "/root/SMILE/DataSetMaster/data_loader.py", line 17, in <module>
    from _MainLauncher import path_operator
  File "/root/SMILE/_MainLauncher.py", line 7, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
root@autodl-container-7c5d4696fb-c54fea2a:~/SMILE# pip install pandas
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting pandas
  Downloading http://mirrors.aliyun.com/pypi/packages/38/f8/d8fddee9ed0d0c0f4a2132c1dfcf0e3e53265055da8df952a53e7eaf178c/pandas-2.2.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.7/12.7 MB 7.1 MB/s eta 0:00:00
Requirement already satisfied: numpy>=1.26.0 in /root/miniconda3/lib/python3.12/site-packages (from pandas) (1.26.4)
Requirement already satisfied: python-dateutil>=2.8.2 in /root/miniconda3/lib/python3.12/site-packages (from pandas) (2.9.0.post0)
Collecting pytz>=2020.1 (from pandas)
  Downloading http://mirrors.aliyun.com/pypi/packages/11/c3/005fcca25ce078d2cc29fd559379817424e94885510568bc1bc53d7d5846/pytz-2024.2-py2.py3-none-any.whl (508 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 508.0/508.0 kB 12.2 MB/s eta 0:00:00
Collecting tzdata>=2022.7 (from pandas)
  Downloading http://mirrors.aliyun.com/pypi/packages/a6/ab/7e5f53c3b9d14972843a647d8d7a853969a58aecc7559cb3267302c94774/tzdata-2024.2-py2.py3-none-any.whl (346 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 346.6/346.6 kB 25.5 MB/s eta 0:00:00
Requirement already satisfied: six>=1.5 in /root/miniconda3/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
Installing collected packages: pytz, tzdata, pandas
Successfully installed pandas-2.2.3 pytz-2024.2 tzdata-2024.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-7c5d4696fb-c54fea2a:~/SMILE# python main.py --dataset NoisyMNIST30000 --seed 9116  --aligned_prop 1 --complete_prop 1
Traceback (most recent call last):
  File "/root/SMILE/main.py", line 3, in <module>
    from DataSetMaster import dataset_master
  File "/root/SMILE/DataSetMaster/dataset_master.py", line 6, in <module>
    from DataSetMaster.data_loader import get_dataset_fair_clustering_mouxin, get_sn
  File "/root/SMILE/DataSetMaster/data_loader.py", line 17, in <module>
    from _MainLauncher import path_operator
  File "/root/SMILE/_MainLauncher.py", line 10, in <module>
    import _Utils.ConfigOperator as ConfigOperator
  File "/root/SMILE/_Utils/ConfigOperator.py", line 4, in <module>
    from easydict import EasyDict
ModuleNotFoundError: No module named 'easydict'
root@autodl-container-7c5d4696fb-c54fea2a:~/SMILE# pip install easydict
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting easydict
  Downloading http://mirrors.aliyun.com/pypi/packages/05/ec/fa6963f1198172c2b75c9ab6ecefb3045991f92f75f5eb41b6621b198123/easydict-1.13-py3-none-any.whl (6.8 kB)
Installing collected packages: easydict
Successfully installed easydict-1.13
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-7c5d4696fb-c54fea2a:~/SMILE# python main.py --dataset NoisyMNIST30000 --seed 9116  --aligned_prop 1 --complete_prop 1
Traceback (most recent call last):
  File "/root/SMILE/main.py", line 3, in <module>
    from DataSetMaster import dataset_master
  File "/root/SMILE/DataSetMaster/dataset_master.py", line 6, in <module>
    from DataSetMaster.data_loader import get_dataset_fair_clustering_mouxin, get_sn
  File "/root/SMILE/DataSetMaster/data_loader.py", line 17, in <module>
    from _MainLauncher import path_operator
  File "/root/SMILE/_MainLauncher.py", line 17, in <module>
    path_operator = PathPresettingOperator.PathOperator(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/SMILE/_Utils/PathPresettingOperator.py", line 54, in __init__
    raise NotImplementedError("Unknown Gpu '{}'".format(current_gpu))
NotImplementedError: Unknown Gpu 'NVIDIA GeForce RTX 3080 Ti'
root@autodl-container-7c5d4696fb-c54fea2a:~/SMILE# python main.py --dataset NoisyMNIST30000 --seed 9116  --aligned_prop 1 --complete_prop 1
```
