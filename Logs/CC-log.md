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
