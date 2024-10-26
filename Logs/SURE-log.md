```linux
root@autodl-container-6c9146b5fb-f8b84f48:~# git clone https://github.com/XLearning-SCU/2022-TPAMI-SURE
Cloning into '2022-TPAMI-SURE'...
remote: Enumerating objects: 49, done.
remote: Counting objects: 100% (49/49), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 49 (delta 18), reused 25 (delta 9), pack-reused 0 (from 0)
Receiving objects: 100% (49/49), 7.20 MiB | 6.41 MiB/s, done.
Resolving deltas: 100% (18/18), done.
root@autodl-container-6c9146b5fb-f8b84f48:~# cd 2022-TPAMI-SURE/
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# ls
Clustering.py  README.md  data_loader.py  datasets  models.py  psp_data_loader.py  pvp_data_loader.py  run.py  sure_inference.py  utils.py
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# touch models.py 
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# cat models.py 
import torch.nn as nn
import torch


class SUREfcNoisyMNIST(nn.Module):
    def __init__(self):
        super(SUREfcNoisyMNIST, self).__init__()
        self.encoder0 = nn.Sequential(
            nn.Linear(784, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.encoder1 = nn.Sequential(
            nn.Linear(784, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.decoder0 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 784))
        self.decoder1 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 784))


    def forward(self, x0, x1):
        h0 = self.encoder0(x0.view(x0.size()[0], -1))
        h1 = self.encoder1(x1.view(x1.size()[0], -1))
        union = torch.cat([h0, h1], 1)
        z0 = self.decoder0(union)
        z1 = self.decoder1(union)
        return h0, h1, z0, z1


class SUREfcCaltech(nn.Module):
    def __init__(self):
        super(SUREfcCaltech, self).__init__()
        self.encoder0 = nn.Sequential(
            nn.Linear(1984, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.encoder1 = nn.Sequential(
            nn.Linear(512, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )
        self.decoder0 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 1984))
        self.decoder1 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 512))

    def forward(self, x0, x1):
        h0 = self.encoder0(x0.view(x0.size()[0], -1))
        h1 = self.encoder1(x1.view(x1.size()[0], -1))
        union = torch.cat([h0, h1], 1)
        z0 = self.decoder0(union)
        z1 = self.decoder1(union)
        return h0, h1, z0, z1


class SUREfcScene(nn.Module):  # 20, 59
    def __init__(self):
        super(SUREfcScene, self).__init__()
        self.encoder0 = nn.Sequential(
            nn.Linear(20, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.encoder1 = nn.Sequential(
            nn.Linear(59, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.decoder0 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 20))
        self.decoder1 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 59))

    def forward(self, x0, x1):
        h0 = self.encoder0(x0)
        h1 = self.encoder1(x1)
        union = torch.cat([h0, h1], 1)
        z0 = self.decoder0(union)
        z1 = self.decoder1(union)
        return h0, h1, z0, z1


class SUREfcReuters(nn.Module):
    def __init__(self):
        super(SUREfcReuters, self).__init__()
        self.encoder0 = nn.Sequential(
            nn.Linear(10, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.encoder1 = nn.Sequential(
            nn.Linear(10, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )
        self.decoder0 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 10))
        self.decoder1 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 10))

    def forward(self, x0, x1):
        h0 = self.encoder0(x0.view(x0.size()[0], -1))
        h1 = self.encoder1(x1.view(x1.size()[0], -1))
        union = torch.cat([h0, h1], 1)
        z0 = self.decoder0(union)
        z1 = self.decoder1(union)
        return h0, h1, z0, z1


class SUREfcMNISTUSPS(nn.Module):
    def __init__(self):
        super(SUREfcMNISTUSPS, self).__init__()
        self.encoder0 = nn.Sequential(
            nn.Linear(784, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.encoder1 = nn.Sequential(
            nn.Linear(256, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.decoder0 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 784))
        self.decoder1 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 256))


    def forward(self, x0, x1):
        h0 = self.encoder0(x0.view(x0.size()[0], -1))
        h1 = self.encoder1(x1.view(x1.size()[0], -1))
        union = torch.cat([h0, h1], 1)
        z0 = self.decoder0(union)
        z1 = self.decoder1(union)
        return h0, h1, z0, z1


class SUREfcDeepCaltech(nn.Module):
    def __init__(self):
        super(SUREfcDeepCaltech, self).__init__()
        self.encoder0 = nn.Sequential(
            nn.Linear(4096, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )

        self.encoder1 = nn.Sequential(
            nn.Linear(4096, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 10),
            nn.BatchNorm1d(10),
            nn.ReLU(True)
        )
        self.decoder0 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 4096))
        self.decoder1 = nn.Sequential(nn.Linear(20, 1024), nn.ReLU(), nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(),
                                      nn.Dropout(0.2), nn.Linear(1024, 1024), nn.ReLU(), nn.Dropout(0.2),
                                      nn.Linear(1024, 4096))

    def forward(self, x0, x1):
        h0 = self.encoder0(x0.view(x0.size()[0], -1))
        h1 = self.encoder0(x1.view(x1.size()[0], -1))
        union = torch.cat([h0, h1], 1)
        z0 = self.decoder0(union)
        z1 = self.decoder0(union)
        return h0, h1, z0, z1


class SUREfcDeepAnimal(nn.Module):
    def __init__(self):
        super(SUREfcDeepAnimal, self).__init__()
        self.encoder0 = nn.Sequential(
            nn.Linear(4096, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(True),
            nn.Dropout(0.2),
            nn.Linear(1024, 1024),
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# ls
Clustering.py  README.md  data_loader.py  datasets  models.py  psp_data_loader.py  pvp_data_loader.py  run.py  sure_inference.py  utils.py
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
Traceback (most recent call last):
  File "/root/2022-TPAMI-SURE/run.py", line 11, in <module>
    from Clustering import Clustering
  File "/root/2022-TPAMI-SURE/Clustering.py", line 6, in <module>
    import sklearn.metrics as metrics
ModuleNotFoundError: No module named 'sklearn'
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# pip install -U scikit-learn scipy matplotlib
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting scikit-learn
  Downloading http://mirrors.aliyun.com/pypi/packages/c6/29/044048c5e911373827c0e1d3051321b9183b2a4f8d4e2f11c08fcff83f13/scikit_learn-1.5.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.9/12.9 MB 16.0 MB/s eta 0:00:00
Collecting scipy
  Downloading http://mirrors.aliyun.com/pypi/packages/8e/ee/8a26858ca517e9c64f84b4c7734b89bda8e63bec85c3d2f432d225bb1886/scipy-1.14.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (40.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.8/40.8 MB 14.0 MB/s eta 0:00:00
Requirement already satisfied: matplotlib in /root/miniconda3/lib/python3.12/site-packages (3.9.0)
Collecting matplotlib
  Downloading http://mirrors.aliyun.com/pypi/packages/27/75/de5b9cd67648051cae40039da0c8cbc497a0d99acb1a1f3d087cd66d27b7/matplotlib-3.9.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 16.0 MB/s eta 0:00:00
Requirement already satisfied: numpy>=1.19.5 in /root/miniconda3/lib/python3.12/site-packages (from scikit-learn) (1.26.4)
Collecting joblib>=1.2.0 (from scikit-learn)
  Downloading http://mirrors.aliyun.com/pypi/packages/91/29/df4b9b42f2be0b623cbd5e2140cafcaa2bef0759a00b7b70104dcfe2fb51/joblib-1.4.2-py3-none-any.whl (301 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 301.8/301.8 kB 44.0 MB/s eta 0:00:00
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
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
Traceback (most recent call last):
  File "/root/2022-TPAMI-SURE/run.py", line 11, in <module>
    from Clustering import Clustering
  File "/root/2022-TPAMI-SURE/Clustering.py", line 8, in <module>
    from munkres import Munkres
ModuleNotFoundError: No module named 'munkres'
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# pip install munkres
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting munkres
  Downloading http://mirrors.aliyun.com/pypi/packages/90/ab/0301c945a704218bc9435f0e3c88884f6b19ef234d8899fb47ce1ccfd0c9/munkres-1.1.4-py2.py3-none-any.whl (7.0 kB)
Installing collected packages: munkres
Successfully installed munkres-1.1.4
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=2, aligned_prop=0.5, complete_prop=0.5)
==========
Traceback (most recent call last):
  File "/root/2022-TPAMI-SURE/run.py", line 255, in <module>
    main()
  File "/root/2022-TPAMI-SURE/run.py", line 184, in main
    train_pair_loader, all_loader, divide_seed = loader(args.batch_size, args.neg_prop, args.aligned_prop,
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 232, in loader
    divide_seed, mask = load_data(dataset, neg_prop, aligned_prop, complete_prop, is_noise)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 58, in load_data
    train_idx, test_idx = TT_split(len(label), 1 - aligned_prop, divide_seed)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/utils.py", line 28, in TT_split
    train_num = np.ceil((1-test_prop) * n_all).astype(np.int)
                                                      ^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/numpy/__init__.py", line 324, in __getattr__
    raise AttributeError(__former_attrs__[attr])
AttributeError: module 'numpy' has no attribute 'int'.
`np.int` was a deprecated alias for the builtin `int`. To avoid this error in existing code, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations. Did you mean: 'inf'?
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=2, aligned_prop=0.5, complete_prop=0.5)
==========
Traceback (most recent call last):
  File "/root/2022-TPAMI-SURE/run.py", line 255, in <module>
    main()
  File "/root/2022-TPAMI-SURE/run.py", line 184, in main
    train_pair_loader, all_loader, divide_seed = loader(args.batch_size, args.neg_prop, args.aligned_prop,
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 232, in loader
    divide_seed, mask = load_data(dataset, neg_prop, aligned_prop, complete_prop, is_noise)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 58, in load_data
    train_idx, test_idx = TT_split(len(label), 1 - aligned_prop, divide_seed)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/utils.py", line 28, in TT_split
    train_num = np.ceil((1-test_prop) * n_all).astype(np.int)
                                                      ^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/numpy/__init__.py", line 324, in __getattr__
    raise AttributeError(__former_attrs__[attr])
AttributeError: module 'numpy' has no attribute 'int'.
`np.int` was a deprecated alias for the builtin `int`. To avoid this error in existing code, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations. Did you mean: 'inf'?
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
Traceback (most recent call last):
  File "/root/2022-TPAMI-SURE/run.py", line 13, in <module>
    from data_loader import loader
  File "/root/2022-TPAMI-SURE/data_loader.py", line 4, in <module>
    from utils import TT_split, normalize
  File "/root/2022-TPAMI-SURE/utils.py", line 28
    train_num = np.ceil((1-test_prop) * n_all).astype(np.int_
                                                     ^
SyntaxError: '(' was never closed
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=2, aligned_prop=0.5, complete_prop=0.5)
==========
Traceback (most recent call last):
  File "/root/2022-TPAMI-SURE/run.py", line 255, in <module>
    main()
  File "/root/2022-TPAMI-SURE/run.py", line 184, in main
    train_pair_loader, all_loader, divide_seed = loader(args.batch_size, args.neg_prop, args.aligned_prop,
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 232, in loader
    divide_seed, mask = load_data(dataset, neg_prop, aligned_prop, complete_prop, is_noise)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 77, in load_data
    test_mask = get_sn(2, len(test_label), 1 - complete_prop)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 168, in get_sn
    matrix_iter = (randint(0, 100, size=(alldata_len, view_num)) < int(ratio * 100)).astype(np.int)
                                                                                            ^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/numpy/__init__.py", line 324, in __getattr__
    raise AttributeError(__former_attrs__[attr])
AttributeError: module 'numpy' has no attribute 'int'.
`np.int` was a deprecated alias for the builtin `int`. To avoid this error in existing code, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations. Did you mean: 'inf'?
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=2, aligned_prop=0.5, complete_prop=0.5)
==========
Traceback (most recent call last):
  File "/root/2022-TPAMI-SURE/run.py", line 255, in <module>
    main()
  File "/root/2022-TPAMI-SURE/run.py", line 184, in main
    train_pair_loader, all_loader, divide_seed = loader(args.batch_size, args.neg_prop, args.aligned_prop,
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 232, in loader
    divide_seed, mask = load_data(dataset, neg_prop, aligned_prop, complete_prop, is_noise)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 77, in load_data
    test_mask = get_sn(2, len(test_label), 1 - complete_prop)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2022-TPAMI-SURE/data_loader.py", line 169, in get_sn
    a = np.sum(((matrix_iter + view_preserve) > 1).astype(np.int))
                                                          ^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/numpy/__init__.py", line 324, in __getattr__
    raise AttributeError(__former_attrs__[attr])
AttributeError: module 'numpy' has no attribute 'int'.
`np.int` was a deprecated alias for the builtin `int`. To avoid this error in existing code, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations. Did you mean: 'inf'?
root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=2, aligned_prop=0.5, complete_prop=0.5)
==========
noise rate of the constructed neg. pairs is  0.07
----------------------Training with noisy_negatives----------------------
******** Training begin ********
=======> Train epoch: 0/80
margin = 5
dist: P = 2.38, N = 2.45, TN = 2.45, FN = 2.5; ncl_loss: 4.0, ver_loss:4.38, time = 3.79 s
/root/2022-TPAMI-SURE/sure_inference.py:171: UserWarning: This overload of addmm_ is deprecated:
        addmm_(Number beta, Number alpha, Tensor mat1, Tensor mat2)
Consider using one of the following signatures instead:
        addmm_(Tensor mat1, Tensor mat2, *, Number beta, Number alpha) (Triggered internally at ../torch/csrc/utils/python_arg_parser.cpp:1578.)
  dist.addmm_(1, -2, x, y.t())
Clustering: acc=0.1889, nmi=0.0999, ari=0.0387
=======> Train epoch: 1/80
dist: P = 3.16, N = 3.5, TN = 3.51, FN = 3.35; ncl_loss: 1.66, ver_loss:0.52, time = 5.88 s
Clustering: acc=0.2936, nmi=0.2369, ari=0.1364
=======> Train epoch: 2/80
dist: P = 3.48, N = 3.93, TN = 3.95, FN = 3.71; ncl_loss: 1.11, ver_loss:0.19, time = 5.61 s
Clustering: acc=0.2776, nmi=0.2274, ari=0.1276
=======> Train epoch: 3/80
dist: P = 3.63, N = 4.17, TN = 4.19, FN = 3.89; ncl_loss: 0.88, ver_loss:0.16, time = 5.4 s
Clustering: acc=0.2566, nmi=0.2179, ari=0.114
=======> Train epoch: 4/80
^CTraceback (most recent call last):
  File "/root/2022-TPAMI-SURE/run.py", line 255, in <module>
    main()
  File "/root/2022-TPAMI-SURE/run.py", line 230, in main
    train(train_pair_loader, model, [criterion_ncl, criterion_mse], optimizer, epoch, args)
  File "/root/2022-TPAMI-SURE/run.py", line 112, in train
    loss.backward()
  File "/root/miniconda3/lib/python3.12/site-packages/torch/_tensor.py", line 525, in backward
    torch.autograd.backward(
  File "/root/miniconda3/lib/python3.12/site-packages/torch/autograd/__init__.py", line 267, in backward
    _engine_run_backward(
  File "/root/miniconda3/lib/python3.12/site-packages/torch/autograd/graph.py", line 744, in _engine_run_backward
    return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

root@autodl-container-6c9146b5fb-f8b84f48:~/2022-TPAMI-SURE# 
```
