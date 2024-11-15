
！！！！！！！  这是去年跑的log
```linux
root@autodl-container-588a499a63-54f942b1:~# ls
autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-588a499a63-54f942b1:~# git clone https://github.com/XLearning-SCU/2021-AAAI-CC
Cloning into '2021-AAAI-CC'...
remote: Enumerating objects: 83, done.
remote: Counting objects: 100% (35/35), done.
remote: Compressing objects: 100% (26/26), done.
remote: Total 83 (delta 21), reused 9 (delta 9), pack-reused 48 (from 1)
Receiving objects: 100% (83/83), 245.51 MiB | 15.39 MiB/s, done.
Resolving deltas: 100% (22/22), done.
Updating files: 100% (23/23), done.
root@autodl-container-588a499a63-54f942b1:~# cd 2021-AAAI-CC/
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# ls
Figures  LICENSE  README.md  cluster.py  config  datasets  evaluation  modules  save  train.py  train_STL10.py  utils
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# python train.py
Traceback (most recent call last):
  File "/root/2021-AAAI-CC/train.py", line 6, in <module>
    from modules import transform, resnet, network, contrastive_loss
  File "/root/2021-AAAI-CC/modules/transform.py", line 2, in <module>
    import cv2
ModuleNotFoundError: No module named 'cv2'
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# pip install cv2
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
ERROR: Could not find a version that satisfies the requirement cv2 (from versions: none)
ERROR: No matching distribution found for cv2
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# pip install opencv-python
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting opencv-python
  Downloading http://mirrors.aliyun.com/pypi/packages/3f/a4/d2537f47fd7fcfba966bd806e3ec18e7ee1681056d4b0a9c8d983983e4d5/opencv_python-4.10.0.84-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (62.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.5/62.5 MB 12.0 MB/s eta 0:00:00
Requirement already satisfied: numpy>=1.21.2 in /root/miniconda3/lib/python3.12/site-packages (from opencv-python) (1.26.4)
Installing collected packages: opencv-python
Successfully installed opencv-python-4.10.0.84
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# python train.py
Downloading https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz to ./datasets/cifar-10-python.tar.gz
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 170498071/170498071 [00:15<00:00, 10908505.59it/s]
Extracting ./datasets/cifar-10-python.tar.gz to ./datasets
Files already downloaded and verified
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# python cluster.py

Traceback (most recent call last):
  File "/root/2021-AAAI-CC/cluster.py", line 8, in <module>
    from evaluation import evaluation
  File "/root/2021-AAAI-CC/evaluation/evaluation.py", line 2, in <module>
    from sklearn import metrics
ModuleNotFoundError: No module named 'sklearn'
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# pip install sklearn 
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting sklearn
  Downloading http://mirrors.aliyun.com/pypi/packages/46/1c/395a83ee7b2d2ad7a05b453872053d41449564477c81dc356f720b16eac4/sklearn-0.0.post12.tar.gz (2.6 kB)
  Preparing metadata (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [15 lines of output]
      The 'sklearn' PyPI package is deprecated, use 'scikit-learn'
      rather than 'sklearn' for pip commands.
      
      Here is how to fix this error in the main use cases:
      - use 'pip install scikit-learn' rather than 'pip install sklearn'
      - replace 'sklearn' by 'scikit-learn' in your pip requirements files
        (requirements.txt, setup.py, setup.cfg, Pipfile, etc ...)
      - if the 'sklearn' package is used by one of your dependencies,
        it would be great if you take some time to track which package uses
        'sklearn' instead of 'scikit-learn' and report it to their issue tracker
      - as a last resort, set the environment variable
        SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True to avoid this error
      
      More information is available at
      https://github.com/scikit-learn/sklearn-pypi-package
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# python cluster.py
Traceback (most recent call last):
  File "/root/2021-AAAI-CC/cluster.py", line 8, in <module>
    from evaluation import evaluation
  File "/root/2021-AAAI-CC/evaluation/evaluation.py", line 2, in <module>
    from sklearn import metrics
ModuleNotFoundError: No module named 'sklearn'
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# pip install -U scikit-learn scipy matplotlib
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting scikit-learn
  Downloading http://mirrors.aliyun.com/pypi/packages/c6/29/044048c5e911373827c0e1d3051321b9183b2a4f8d4e2f11c08fcff83f13/scikit_learn-1.5.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.9/12.9 MB 15.6 MB/s eta 0:00:00
Collecting scipy
  Downloading http://mirrors.aliyun.com/pypi/packages/8e/ee/8a26858ca517e9c64f84b4c7734b89bda8e63bec85c3d2f432d225bb1886/scipy-1.14.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (40.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.8/40.8 MB 14.0 MB/s eta 0:00:00
Requirement already satisfied: matplotlib in /root/miniconda3/lib/python3.12/site-packages (3.9.0)
Collecting matplotlib
  Downloading http://mirrors.aliyun.com/pypi/packages/27/75/de5b9cd67648051cae40039da0c8cbc497a0d99acb1a1f3d087cd66d27b7/matplotlib-3.9.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 15.7 MB/s eta 0:00:00
Requirement already satisfied: numpy>=1.19.5 in /root/miniconda3/lib/python3.12/site-packages (from scikit-learn) (1.26.4)
Collecting joblib>=1.2.0 (from scikit-learn)
  Downloading http://mirrors.aliyun.com/pypi/packages/91/29/df4b9b42f2be0b623cbd5e2140cafcaa2bef0759a00b7b70104dcfe2fb51/joblib-1.4.2-py3-none-any.whl (301 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 301.8/301.8 kB 24.1 MB/s eta 0:00:00
Collecting threadpoolctl>=3.1.0 (from scikit-learn)
  Downloading http://mirrors.aliyun.com/pypi/packages/4b/2c/ffbf7a134b9ab11a67b0cf0726453cedd9c5043a4fe7a35d1cefa9a1bcfb/threadpoolctl-3.5.0-py3-none-any.whl (18 kB)
Requirement already satisfied: contourpy>=1.0.1 in /root/miniconda3/lib/python3.12/site-packages (from matplotlib) (1.2.1)
Requirement already satisfied: cycler>=0.10 in /root/miniconda3/lib/python3.12/site-packages (from matplotlib) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /root/miniconda3/lib/python3.12/site-packages (from matplotlib) (4.53.0)
Requirement already satisfied: kiwisolver>=1.3.1 in /root/miniconda3/lib/python3.12/site-packages (from matplotlib) (1.4.5)
Requirement already satisfied: packaging>=20.0 in /root/miniconda3/lib/python3.12/site-packages (from matplotlib) (23.2)
Requirement already satisfied: pillow>=8 in /root/miniconda3/lib/python3.12/site-packages (from matplotlib) (10.3.0)
Requirement already satisfied: pyparsing>=2.3.1 in /root/miniconda3/lib/python3.12/site-packages (from matplotlib) (3.1.2)
Requirement already satisfied: python-dateutil>=2.7 in /root/miniconda3/lib/python3.12/site-packages (from matplotlib) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /root/miniconda3/lib/python3.12/site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn, matplotlib
  Attempting uninstall: matplotlib
    Found existing installation: matplotlib 3.9.0
    Uninstalling matplotlib-3.9.0:
      Successfully uninstalled matplotlib-3.9.0
Successfully installed joblib-1.4.2 matplotlib-3.9.2 scikit-learn-1.5.2 scipy-1.14.1 threadpoolctl-3.5.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# python cluster.py
Traceback (most recent call last):
  File "/root/2021-AAAI-CC/cluster.py", line 8, in <module>
    from evaluation import evaluation
  File "/root/2021-AAAI-CC/evaluation/evaluation.py", line 3, in <module>
    from munkres import Munkres
ModuleNotFoundError: No module named 'munkres'
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# pip install munkres
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting munkres
  Downloading http://mirrors.aliyun.com/pypi/packages/90/ab/0301c945a704218bc9435f0e3c88884f6b19ef234d8899fb47ce1ccfd0c9/munkres-1.1.4-py2.py3-none-any.whl (7.0 kB)
Installing collected packages: munkres
Successfully installed munkres-1.1.4
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# python cluster.py
Files already downloaded and verified
Files already downloaded and verified
### Creating features from model ###
Step [0/120]     Computing features...
Step [20/120]    Computing features...
Step [40/120]    Computing features...
Step [60/120]    Computing features...
Step [80/120]    Computing features...
Step [100/120]   Computing features...
Features shape (60000,)
NMI = 0.0000 ARI = 0.0000 F = 0.3162 ACC = 0.1000
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# python train.py
Files already downloaded and verified
Files already downloaded and verified
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC# python cluster.py
Files already downloaded and verified
Files already downloaded and verified
### Creating features from model ###
Step [0/120]     Computing features...
Step [20/120]    Computing features...
Step [40/120]    Computing features...
Step [60/120]    Computing features...
Step [80/120]    Computing features...
Step [100/120]   Computing features...
Features shape (60000,)
NMI = 0.0000 ARI = 0.0000 F = 0.3162 ACC = 0.1000
root@autodl-container-588a499a63-54f942b1:~/2021-AAAI-CC#
```

！！！！！！！！！！！ 
/cofigure/configure.yaml  文件当中start_epoch 需要改到0 再开始训练
但是我发现训练一轮的时间很长，1个epoch 需要2分钟左右，1000个epoch 就需要2000分钟，需要十几个小时。

> python train.py 


```
root@autodl-container-534b4e910e-a60bb39b:~/2021-AAAI-CC# python train.py
Files already downloaded and verified
Files already downloaded and verified
Step [0/468]     loss_instance: 5.523750305175781        loss_cluster: 2.9808597564697266
Step [50/468]    loss_instance: 4.907449245452881        loss_cluster: 2.586517095565796
Step [100/468]   loss_instance: 4.844895362854004        loss_cluster: 2.5611791610717773
Step [150/468]   loss_instance: 4.774590015411377        loss_cluster: 2.5887885093688965
Step [200/468]   loss_instance: 4.849625587463379        loss_cluster: 2.5469326972961426
Step [250/468]   loss_instance: 4.811999797821045        loss_cluster: 2.595579147338867
Step [300/468]   loss_instance: 4.610802173614502        loss_cluster: 2.4863321781158447
Step [350/468]   loss_instance: 4.591360569000244        loss_cluster: 2.474429130554199
Step [400/468]   loss_instance: 4.545931339263916        loss_cluster: 2.448517084121704
Step [450/468]   loss_instance: 4.425240516662598        loss_cluster: 2.4327850341796875
Epoch [0/1000]   Loss: 7.331314488353892
Step [0/468]     loss_instance: 4.506473064422607        loss_cluster: 2.4271185398101807
Step [50/468]    loss_instance: 4.500378608703613        loss_cluster: 2.4493887424468994
Step [100/468]   loss_instance: 4.484992027282715        loss_cluster: 2.4481515884399414
Step [150/468]   loss_instance: 4.5482048988342285       loss_cluster: 2.4968349933624268
Step [200/468]   loss_instance: 4.486989498138428        loss_cluster: 2.4759232997894287
Step [250/468]   loss_instance: 4.423585891723633        loss_cluster: 2.3898727893829346
Step [300/468]   loss_instance: 4.385447025299072        loss_cluster: 2.398859977722168
Step [350/468]   loss_instance: 4.407721042633057        loss_cluster: 2.411796808242798
Step [400/468]   loss_instance: 4.375770568847656        loss_cluster: 2.4007091522216797
Step [450/468]   loss_instance: 4.377002239227295        loss_cluster: 2.3889784812927246
Epoch [1/1000]   Loss: 6.961500413397438
Step [0/468]     loss_instance: 4.466317176818848        loss_cluster: 2.4228262901306152
Step [50/468]    loss_instance: 4.392653942108154        loss_cluster: 2.4096972942352295
Step [100/468]   loss_instance: 4.35814094543457         loss_cluster: 2.3752377033233643
Step [150/468]   loss_instance: 4.413210868835449        loss_cluster: 2.405458927154541
Step [200/468]   loss_instance: 4.3442182540893555       loss_cluster: 2.332319974899292
Step [250/468]   loss_instance: 4.406662464141846        loss_cluster: 2.38960599899292
Step [300/468]   loss_instance: 4.468982219696045        loss_cluster: 2.4320876598358154
Step [350/468]   loss_instance: 4.407156944274902        loss_cluster: 2.3590478897094727
Step [400/468]   loss_instance: 4.369258403778076        loss_cluster: 2.39176869392395
Step [450/468]   loss_instance: 4.3565239906311035       loss_cluster: 2.369015693664551
Epoch [2/1000]   Loss: 6.80619607725714
Step [0/468]     loss_instance: 4.364185810089111        loss_cluster: 2.417112112045288
Step [50/468]    loss_instance: 4.449417591094971        loss_cluster: 2.37086820602417
Step [100/468]   loss_instance: 4.443105220794678        loss_cluster: 2.409438133239746
Step [150/468]   loss_instance: 4.308730602264404        loss_cluster: 2.306596040725708
Step [200/468]   loss_instance: 4.414360523223877        loss_cluster: 2.4157931804656982
Step [250/468]   loss_instance: 4.307351589202881        loss_cluster: 2.347630500793457
Step [300/468]   loss_instance: 4.347302436828613        loss_cluster: 2.3354532718658447
Step [350/468]   loss_instance: 4.371107578277588        loss_cluster: 2.3644540309906006
Step [400/468]   loss_instance: 4.333224773406982        loss_cluster: 2.3797836303710938
Step [450/468]   loss_instance: 4.350967884063721        loss_cluster: 2.31973934173584
Epoch [3/1000]   Loss: 6.703831605422191
Step [0/468]     loss_instance: 4.3671393394470215       loss_cluster: 2.378864049911499
Step [50/468]    loss_instance: 4.234332084655762        loss_cluster: 2.3302388191223145
Step [100/468]   loss_instance: 4.393280982971191        loss_cluster: 2.362544536590576
Step [150/468]   loss_instance: 4.265163421630859        loss_cluster: 2.3143067359924316
Step [200/468]   loss_instance: 4.254357814788818        loss_cluster: 2.338102340698242
Step [250/468]   loss_instance: 4.256413459777832        loss_cluster: 2.340421676635742
Step [300/468]   loss_instance: 4.272576332092285        loss_cluster: 2.3394534587860107
Step [350/468]   loss_instance: 4.34993314743042         loss_cluster: 2.387589931488037
Step [400/468]   loss_instance: 4.334082126617432        loss_cluster: 2.335824966430664
Step [450/468]   loss_instance: 4.210085868835449        loss_cluster: 2.300955057144165
Epoch [4/1000]   Loss: 6.629261066770961
Step [0/468]     loss_instance: 4.297388076782227        loss_cluster: 2.359909772872925
Step [50/468]    loss_instance: 4.214735984802246        loss_cluster: 2.3144936561584473
Step [100/468]   loss_instance: 4.275135040283203        loss_cluster: 2.359938859939575
Step [150/468]   loss_instance: 4.24873161315918         loss_cluster: 2.277681589126587
Step [200/468]   loss_instance: 4.386613368988037        loss_cluster: 2.320652723312378
Step [250/468]   loss_instance: 4.277464389801025        loss_cluster: 2.336599826812744
Step [300/468]   loss_instance: 4.179553031921387        loss_cluster: 2.2430803775787354
Step [350/468]   loss_instance: 4.296618938446045        loss_cluster: 2.3451545238494873
Step [400/468]   loss_instance: 4.372502326965332        loss_cluster: 2.3660330772399902
```
 
！！！！训练几轮之后的效果去进行聚类,效果比文章当中的差很多。


```linux
root@autodl-container-534b4e910e-a60bb39b:~/2021-AAAI-CC# python cluster.py 
Files already downloaded and verified
Files already downloaded and verified
/root/2021-AAAI-CC/cluster.py:116: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  model.load_state_dict(torch.load(model_fp, map_location=device.type)['net'])
### Creating features from model ###
Step [0/120]     Computing features...
Step [20/120]    Computing features...
Step [40/120]    Computing features...
Step [60/120]    Computing features...
Step [80/120]    Computing features...
Step [100/120]   Computing features...
Features shape (60000,)
NMI = 0.1708 ARI = 0.0933 F = 0.1908 ACC = 0.2658
```


！！！！！！！！！！由于训练这个模型时间较长，先暂时放弃这个模型。
