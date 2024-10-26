报错  ！！！ torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 

```linux
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
CVCL  DIVIDE  FCMI  Pro-Imp  RMCNC  SMILE  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# cd RMCNC/
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC# ls
2024-TKDE-RMCNC-main  2024-TKDE-RMCNC-main.zip
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC# cd 2024-TKDE-RMCNC-main
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main# ls
README.md  RMCNC_main
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main# ls
README.md  RMCNC_main
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main# cd RMCNC_main/
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# ls
'=1.18.2'   Clustering.py   __pycache__   data_loader.py   models.py   psp_data_loader.py   pvp_data_loader.py   readme.md   run_RMCNC.py   sure_inference.py   train.sh   train_NC.sh   utils.py
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# sh train.sh
====================================================================================
================================alignment rate: 0.5 ================================
====================================================================================
Traceback (most recent call last):
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 39, in _open_file
    return open(file_like, mode), True
           ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: './datasets/AWA-7view-10158sample.mat'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/root/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main/run_RMCNC.py", line 236, in <module>
    main()
  File "/root/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main/run_RMCNC.py", line 111, in main
    train_pair_loader, all_loader, divide_seed = loader_cl(args.batch_size, args.neg_prop, args.aligned_prop,
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main/data_loader.py", line 324, in loader_cl
    train_pairs, train_pair_labels, train_pair_real_labels, all_data, all_label, all_label_X, all_label_Y, label_aligned, divide_seed, mask = load_data(dataset, neg_prop, aligned_prop, complete_prop, is_noise)
                                                                                                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main/data_loader.py", line 19, in load_data
    mat = sio.loadmat('./datasets/' + dataset + '.mat')
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 225, in loadmat
    with _open_file_context(file_name, appendmat) as f:
  File "/root/miniconda3/lib/python3.12/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 17, in _open_file_context
    f, opened = _open_file(file_like, appendmat, mode)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 45, in _open_file
    return open(file_like, mode), True
           ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: './datasets/AWA-7view-10158sample.mat'
Traceback (most recent call last):
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 39, in _open_file
    return open(file_like, mode), True
           ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: './datasets/AWA-7view-10158sample.mat'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/root/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main/run_RMCNC.py", line 236, in <module>
    main()
  File "/root/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main/run_RMCNC.py", line 111, in main
    train_pair_loader, all_loader, divide_seed = loader_cl(args.batch_size, args.neg_prop, args.aligned_prop,
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main/data_loader.py", line 324, in loader_cl
    train_pairs, train_pair_labels, train_pair_real_labels, all_data, all_label, all_label_X, all_label_Y, label_aligned, divide_seed, mask = load_data(dataset, neg_prop, aligned_prop, complete_prop, is_noise)
                                                                                                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main/data_loader.py", line 19, in load_data
    mat = sio.loadmat('./datasets/' + dataset + '.mat')
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 225, in loadmat
    with _open_file_context(file_name, appendmat) as f:
  File "/root/miniconda3/lib/python3.12/contextlib.py", line 137, in __enter__
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# 
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# 
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# cd 
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
CVCL  DIVIDE  FCMI  Pro-Imp  RMCNC  SMILE  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# git clone https://github.com/XLearning-SCU/2022-IJCV-TCL
Cloning into '2022-IJCV-TCL'...
fatal: unable to access 'https://github.com/XLearning-SCU/2022-IJCV-TCL/': HTTP/2 stream 1 was not closed cleanly before end of the underlying stream
root@autodl-container-7c5d4696fb-c54fea2a:~# mkdir TCL
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
'2022-IJCV-TCL-main (1).zip'   CVCL   DIVIDE   FCMI   Pro-Imp   RMCNC   SMILE   Sure   TCL   autodl-pub   autodl-tmp   miniconda3   tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# cd TCL
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL# ls
'2022-IJCV-TCL-main (1).zip'
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL# ls
'2022-IJCV-TCL-main (1).zip'
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL# unzip 2022-IJCV-TCL-main\ \(1\).zip 
Archive:  2022-IJCV-TCL-main (1).zip
7e7c4e76cb569b995b5e0ffb88ffa21884cd926e
   creating: 2022-IJCV-TCL-main/
  inflating: 2022-IJCV-TCL-main/README.md  
   creating: 2022-IJCV-TCL-main/TextClustering/
   creating: 2022-IJCV-TCL-main/TextClustering/EDA/
 extracting: 2022-IJCV-TCL-main/TextClustering/EDA/__init__.py  
   creating: 2022-IJCV-TCL-main/TextClustering/EDA/__pycache__/
  inflating: 2022-IJCV-TCL-main/TextClustering/EDA/__pycache__/__init__.cpython-37.pyc  
  inflating: 2022-IJCV-TCL-main/TextClustering/EDA/__pycache__/augment.cpython-37.pyc  
  inflating: 2022-IJCV-TCL-main/TextClustering/EDA/__pycache__/eda.cpython-37.pyc  
  inflating: 2022-IJCV-TCL-main/TextClustering/EDA/augment.py  
  inflating: 2022-IJCV-TCL-main/TextClustering/EDA/eda.py  
  inflating: 2022-IJCV-TCL-main/TextClustering/README.md  
  inflating: 2022-IJCV-TCL-main/TextClustering/boost.py  
   creating: 2022-IJCV-TCL-main/TextClustering/datasets/
  inflating: 2022-IJCV-TCL-main/TextClustering/datasets/Biomedical.txt  
  inflating: 2022-IJCV-TCL-main/TextClustering/datasets/Biomedical_gnd.txt  
  inflating: 2022-IJCV-TCL-main/TextClustering/datasets/StackOverflow.txt  
  inflating: 2022-IJCV-TCL-main/TextClustering/datasets/StackOverflow_gnd.txt  
  inflating: 2022-IJCV-TCL-main/TextClustering/evaluation.py  
  inflating: 2022-IJCV-TCL-main/TextClustering/loss.py  
  inflating: 2022-IJCV-TCL-main/TextClustering/network.py  
  inflating: 2022-IJCV-TCL-main/TextClustering/train.py  
   creating: 2022-IJCV-TCL-main/TextClustering/utils/
  inflating: 2022-IJCV-TCL-main/TextClustering/utils/__init__.py  
   creating: 2022-IJCV-TCL-main/TextClustering/utils/__pycache__/
  inflating: 2022-IJCV-TCL-main/TextClustering/utils/__pycache__/__init__.cpython-37.pyc  
  inflating: 2022-IJCV-TCL-main/TextClustering/utils/__pycache__/cluster_utils.cpython-37.pyc  
  inflating: 2022-IJCV-TCL-main/TextClustering/utils/__pycache__/save_model.cpython-37.pyc  
  inflating: 2022-IJCV-TCL-main/TextClustering/utils/__pycache__/yaml_config_hook.cpython-37.pyc  
  inflating: 2022-IJCV-TCL-main/TextClustering/utils/cluster_utils.py  
  inflating: 2022-IJCV-TCL-main/TextClustering/utils/save_model.py  
  inflating: 2022-IJCV-TCL-main/TextClustering/utils/yaml_config_hook.py  
  inflating: 2022-IJCV-TCL-main/boost.py  
  inflating: 2022-IJCV-TCL-main/data.py  
  inflating: 2022-IJCV-TCL-main/engine.py  
  inflating: 2022-IJCV-TCL-main/evaluate.py  
  inflating: 2022-IJCV-TCL-main/loss.py  
  inflating: 2022-IJCV-TCL-main/misc.py  
  inflating: 2022-IJCV-TCL-main/model.py  
  inflating: 2022-IJCV-TCL-main/train.py  
  inflating: 2022-IJCV-TCL-main/transforms.py  
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL# ls
 2022-IJCV-TCL-main  '2022-IJCV-TCL-main (1).zip'
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL#  cd 2022-IJCV-TCL-main
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# ls
README.md  TextClustering  boost.py  data.py  engine.py  evaluate.py  loss.py  misc.py  model.py  train.py  transforms.py
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# OMP_NUM_THREADS=1 python -m torch.distributed.launch --nproc_per_node=4 train.py
/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py:183: FutureWarning: The module torch.distributed.launch is deprecated
and will be removed in future. Use torchrun.
Note that --use-env is set by default in torchrun.
If your script expects `--local-rank` argument to be set, please
change it to read from `os.environ['LOCAL_RANK']` instead. See 
https://pytorch.org/docs/stable/distributed.html#launch-utility for 
further instructions

  warnings.warn(
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
^CW1026 20:13:02.682000 139994841933632 torch/distributed/elastic/agent/server/api.py:741] Received 2 death signal, shutting down workers
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 198, in <module>
    main()
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 194, in main
    launch(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 179, in launch
    run(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/run.py", line 870, in run
    elastic_launch(
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 132, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 254, in launch_agent
    result = agent.run()
             ^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/elastic/metrics/api.py", line 123, in wrapper
    result = f(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/elastic/agent/server/api.py", line 733, in run
    result = self._invoke_run(role)
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/elastic/agent/server/api.py", line 876, in _invoke_run
    time.sleep(monitor_interval)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/elastic/multiprocessing/api.py", line 76, in _terminate_process_handler
    raise SignalException(f"Process {os.getpid()} got signal: {sigval}", sigval=sigval)
torch.distributed.elastic.multiprocessing.api.SignalException: Process 2037 got signal: 2
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# pip install --upgrade torchvision torchaudio
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Requirement already satisfied: torchvision in /root/miniconda3/lib/python3.12/site-packages (0.18.0+cu121)
Collecting torchvision
  Downloading http://mirrors.aliyun.com/pypi/packages/6c/4b/0627814c10b70b4032b68b454ada67cdec9c28c1d8d0ff54aad66602df9f/torchvision-0.20.0-cp312-cp312-manylinux1_x86_64.whl (7.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 12.8 MB/s eta 0:00:00
Collecting torchaudio
  Downloading http://mirrors.aliyun.com/pypi/packages/6d/b8/30849d2fa7ce60acc95df9c04ab42b6c12ba1ca968cb9fa6f64010cdc420/torchaudio-2.5.0-cp312-cp312-manylinux1_x86_64.whl (3.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 14.3 MB/s eta 0:00:00
Requirement already satisfied: numpy in /root/miniconda3/lib/python3.12/site-packages (from torchvision) (1.26.4)
Collecting torch==2.5.0 (from torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/ac/72/d610029ef5cdde3f3aa216e8e75c233b1a91b34af0fc47392b3aa928563a/torch-2.5.0-cp312-cp312-manylinux1_x86_64.whl (906.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 906.4/906.4 MB 3.0 MB/s eta 0:00:00
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /root/miniconda3/lib/python3.12/site-packages (from torchvision) (10.3.0)
Requirement already satisfied: filelock in /root/miniconda3/lib/python3.12/site-packages (from torch==2.5.0->torchvision) (3.14.0)
Requirement already satisfied: typing-extensions>=4.8.0 in /root/miniconda3/lib/python3.12/site-packages (from torch==2.5.0->torchvision) (4.12.1)
Requirement already satisfied: networkx in /root/miniconda3/lib/python3.12/site-packages (from torch==2.5.0->torchvision) (3.3)
Requirement already satisfied: jinja2 in /root/miniconda3/lib/python3.12/site-packages (from torch==2.5.0->torchvision) (3.1.4)
Requirement already satisfied: fsspec in /root/miniconda3/lib/python3.12/site-packages (from torch==2.5.0->torchvision) (2024.5.0)
Collecting nvidia-cuda-nvrtc-cu12==12.4.127 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/2c/14/91ae57cd4db3f9ef7aa99f4019cfa8d54cb4caa7e00975df6467e9725a9f/nvidia_cuda_nvrtc_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (24.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.6/24.6 MB 14.5 MB/s eta 0:00:00
Collecting nvidia-cuda-runtime-cu12==12.4.127 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/ea/27/1795d86fe88ef397885f2e580ac37628ed058a92ed2c39dc8eac3adf0619/nvidia_cuda_runtime_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (883 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 883.7/883.7 kB 18.6 MB/s eta 0:00:00
Collecting nvidia-cuda-cupti-cu12==12.4.127 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/67/42/f4f60238e8194a3106d06a058d494b18e006c10bb2b915655bd9f6ea4cb1/nvidia_cuda_cupti_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (13.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.8/13.8 MB 15.3 MB/s eta 0:00:00
Collecting nvidia-cudnn-cu12==9.1.0.70 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/9f/fd/713452cd72343f682b1c7b9321e23829f00b842ceaedcda96e742ea0b0b3/nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl (664.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 664.8/664.8 MB 3.9 MB/s eta 0:00:00
Collecting nvidia-cublas-cu12==12.4.5.8 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/ae/71/1c91302526c45ab494c23f61c7a84aa568b8c1f9d196efa5993957faf906/nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl (363.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 363.4/363.4 MB 6.0 MB/s eta 0:00:00
Collecting nvidia-cufft-cu12==11.2.1.3 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/27/94/3266821f65b92b3138631e9c8e7fe1fb513804ac934485a8d05776e1dd43/nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_x86_64.whl (211.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 211.5/211.5 MB 7.8 MB/s eta 0:00:00
Collecting nvidia-curand-cu12==10.3.5.147 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/8a/6d/44ad094874c6f1b9c654f8ed939590bdc408349f137f9b98a3a23ccec411/nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_x86_64.whl (56.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.3/56.3 MB 9.9 MB/s eta 0:00:00
Collecting nvidia-cusolver-cu12==11.6.1.9 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/3a/e1/5b9089a4b2a4790dfdea8b3a006052cfecff58139d5a4e34cb1a51df8d6f/nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_x86_64.whl (127.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 127.9/127.9 MB 9.6 MB/s eta 0:00:00
Collecting nvidia-cusparse-cu12==12.3.1.170 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/db/f7/97a9ea26ed4bbbfc2d470994b8b4f338ef663be97b8f677519ac195e113d/nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_x86_64.whl (207.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 207.5/207.5 MB 8.0 MB/s eta 0:00:00
Collecting nvidia-nccl-cu12==2.21.5 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/df/99/12cd266d6233f47d00daf3a72739872bdc10267d0383508b0b9c84a18bb6/nvidia_nccl_cu12-2.21.5-py3-none-manylinux2014_x86_64.whl (188.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 188.7/188.7 MB 8.3 MB/s eta 0:00:00
Collecting nvidia-nvtx-cu12==12.4.127 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/87/20/199b8713428322a2f22b722c62b8cc278cc53dffa9705d744484b5035ee9/nvidia_nvtx_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (99 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 99.1/99.1 kB 21.6 MB/s eta 0:00:00
Collecting nvidia-nvjitlink-cu12==12.4.127 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/ff/ff/847841bacfbefc97a00036e0fce5a0f086b640756dc38caea5e1bb002655/nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (21.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 21.1/21.1 MB 14.9 MB/s eta 0:00:00
Collecting triton==3.1.0 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/78/eb/65f5ba83c2a123f6498a3097746607e5b2f16add29e36765305e4ac7fdd8/triton-3.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (209.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 209.6/209.6 MB 7.6 MB/s eta 0:00:00
Requirement already satisfied: setuptools in /root/miniconda3/lib/python3.12/site-packages (from torch==2.5.0->torchvision) (69.5.1)
Collecting sympy==1.13.1 (from torch==2.5.0->torchvision)
  Downloading http://mirrors.aliyun.com/pypi/packages/b2/fe/81695a1aa331a842b582453b605175f419fe8540355886031328089d840a/sympy-1.13.1-py3-none-any.whl (6.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 15.9 MB/s eta 0:00:00
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /root/miniconda3/lib/python3.12/site-packages (from sympy==1.13.1->torch==2.5.0->torchvision) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in /root/miniconda3/lib/python3.12/site-packages (from jinja2->torch==2.5.0->torchvision) (2.1.5)
Installing collected packages: triton, sympy, nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, nvidia-cusparse-cu12, nvidia-cudnn-cu12, nvidia-cusolver-cu12, torch, torchvision, torchaudio
  Attempting uninstall: sympy
    Found existing installation: sympy 1.12.1
    Uninstalling sympy-1.12.1:
      Successfully uninstalled sympy-1.12.1
  Attempting uninstall: nvidia-nvtx-cu12
    Found existing installation: nvidia-nvtx-cu12 12.1.105
    Uninstalling nvidia-nvtx-cu12-12.1.105:
      Successfully uninstalled nvidia-nvtx-cu12-12.1.105
  Attempting uninstall: nvidia-nvjitlink-cu12
    Found existing installation: nvidia-nvjitlink-cu12 12.5.40
    Uninstalling nvidia-nvjitlink-cu12-12.5.40:
      Successfully uninstalled nvidia-nvjitlink-cu12-12.5.40
  Attempting uninstall: nvidia-nccl-cu12
    Found existing installation: nvidia-nccl-cu12 2.20.5
    Uninstalling nvidia-nccl-cu12-2.20.5:
      Successfully uninstalled nvidia-nccl-cu12-2.20.5
  Attempting uninstall: nvidia-curand-cu12
    Found existing installation: nvidia-curand-cu12 10.3.2.106
    Uninstalling nvidia-curand-cu12-10.3.2.106:
      Successfully uninstalled nvidia-curand-cu12-10.3.2.106
  Attempting uninstall: nvidia-cufft-cu12
    Found existing installation: nvidia-cufft-cu12 11.0.2.54
    Uninstalling nvidia-cufft-cu12-11.0.2.54:
      Successfully uninstalled nvidia-cufft-cu12-11.0.2.54
  Attempting uninstall: nvidia-cuda-runtime-cu12
    Found existing installation: nvidia-cuda-runtime-cu12 12.1.105
    Uninstalling nvidia-cuda-runtime-cu12-12.1.105:
      Successfully uninstalled nvidia-cuda-runtime-cu12-12.1.105
  Attempting uninstall: nvidia-cuda-nvrtc-cu12
    Found existing installation: nvidia-cuda-nvrtc-cu12 12.1.105
    Uninstalling nvidia-cuda-nvrtc-cu12-12.1.105:
      Successfully uninstalled nvidia-cuda-nvrtc-cu12-12.1.105
  Attempting uninstall: nvidia-cuda-cupti-cu12
    Found existing installation: nvidia-cuda-cupti-cu12 12.1.105
    Uninstalling nvidia-cuda-cupti-cu12-12.1.105:
      Successfully uninstalled nvidia-cuda-cupti-cu12-12.1.105
  Attempting uninstall: nvidia-cublas-cu12
    Found existing installation: nvidia-cublas-cu12 12.1.3.1
    Uninstalling nvidia-cublas-cu12-12.1.3.1:
      Successfully uninstalled nvidia-cublas-cu12-12.1.3.1
  Attempting uninstall: nvidia-cusparse-cu12
    Found existing installation: nvidia-cusparse-cu12 12.1.0.106
    Uninstalling nvidia-cusparse-cu12-12.1.0.106:
      Successfully uninstalled nvidia-cusparse-cu12-12.1.0.106
  Attempting uninstall: nvidia-cudnn-cu12
    Found existing installation: nvidia-cudnn-cu12 8.9.2.26
    Uninstalling nvidia-cudnn-cu12-8.9.2.26:
      Successfully uninstalled nvidia-cudnn-cu12-8.9.2.26
  Attempting uninstall: nvidia-cusolver-cu12
    Found existing installation: nvidia-cusolver-cu12 11.4.5.107
    Uninstalling nvidia-cusolver-cu12-11.4.5.107:
      Successfully uninstalled nvidia-cusolver-cu12-11.4.5.107
  Attempting uninstall: torch
    Found existing installation: torch 2.3.0+cu121
    Uninstalling torch-2.3.0+cu121:
      Successfully uninstalled torch-2.3.0+cu121
  Attempting uninstall: torchvision
    Found existing installation: torchvision 0.18.0+cu121
    Uninstalling torchvision-0.18.0+cu121:
      Successfully uninstalled torchvision-0.18.0+cu121
Successfully installed nvidia-cublas-cu12-12.4.5.8 nvidia-cuda-cupti-cu12-12.4.127 nvidia-cuda-nvrtc-cu12-12.4.127 nvidia-cuda-runtime-cu12-12.4.127 nvidia-cudnn-cu12-9.1.0.70 nvidia-cufft-cu12-11.2.1.3 nvidia-curand-cu12-10.3.5.147 nvidia-cusolver-cu12-11.6.1.9 nvidia-cusparse-cu12-12.3.1.170 nvidia-nccl-cu12-2.21.5 nvidia-nvjitlink-cu12-12.4.127 nvidia-nvtx-cu12-12.4.127 sympy-1.13.1 torch-2.5.0 torchaudio-2.5.0 torchvision-0.20.0 triton-3.1.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# OMP_NUM_THREADS=1 python -m torch.distributed.launch --nproc_per_node=4 train.py
/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py:208: FutureWarning: The module torch.distributed.launch is deprecated
and will be removed in future. Use torchrun.
Note that --use-env is set by default in torchrun.
If your script expects `--local-rank` argument to be set, please
change it to read from `os.environ['LOCAL_RANK']` instead. See 
https://pytorch.org/docs/stable/distributed.html#launch-utility for 
further instructions

  main()
Traceback (most recent call last):
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
        import miscimport misc

  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
        from torch._six import inffrom torch._six import inf

ModuleNotFoundErrorModuleNotFoundError: : No module named 'torch._six'No module named 'torch._six'

Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
W1026 20:21:50.813000 2215 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2217 closing signal SIGTERM
W1026 20:21:50.815000 2215 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2219 closing signal SIGTERM
W1026 20:21:50.816000 2215 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2220 closing signal SIGTERM
E1026 20:21:50.824000 2215 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 1 (pid: 2218) of binary: /root/miniconda3/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 208, in <module>
    main()
  File "/root/miniconda3/lib/python3.12/site-packages/typing_extensions.py", line 2853, in wrapper
    return arg(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 204, in main
    launch(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 189, in launch
    run(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/run.py", line 910, in run
    elastic_launch(
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
train.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2024-10-26_20:21:50
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 2218)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# pip install torch torchvision torchaudio
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Requirement already satisfied: torch in /root/miniconda3/lib/python3.12/site-packages (2.5.0)
Requirement already satisfied: torchvision in /root/miniconda3/lib/python3.12/site-packages (0.20.0)
Requirement already satisfied: torchaudio in /root/miniconda3/lib/python3.12/site-packages (2.5.0)
Requirement already satisfied: filelock in /root/miniconda3/lib/python3.12/site-packages (from torch) (3.14.0)
Requirement already satisfied: typing-extensions>=4.8.0 in /root/miniconda3/lib/python3.12/site-packages (from torch) (4.12.1)
Requirement already satisfied: networkx in /root/miniconda3/lib/python3.12/site-packages (from torch) (3.3)
Requirement already satisfied: jinja2 in /root/miniconda3/lib/python3.12/site-packages (from torch) (3.1.4)
Requirement already satisfied: fsspec in /root/miniconda3/lib/python3.12/site-packages (from torch) (2024.5.0)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch) (12.4.127)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch) (12.4.127)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch) (12.4.127)
Requirement already satisfied: nvidia-cudnn-cu12==9.1.0.70 in /root/miniconda3/lib/python3.12/site-packages (from torch) (9.1.0.70)
Requirement already satisfied: nvidia-cublas-cu12==12.4.5.8 in /root/miniconda3/lib/python3.12/site-packages (from torch) (12.4.5.8)
Requirement already satisfied: nvidia-cufft-cu12==11.2.1.3 in /root/miniconda3/lib/python3.12/site-packages (from torch) (11.2.1.3)
Requirement already satisfied: nvidia-curand-cu12==10.3.5.147 in /root/miniconda3/lib/python3.12/site-packages (from torch) (10.3.5.147)
Requirement already satisfied: nvidia-cusolver-cu12==11.6.1.9 in /root/miniconda3/lib/python3.12/site-packages (from torch) (11.6.1.9)
Requirement already satisfied: nvidia-cusparse-cu12==12.3.1.170 in /root/miniconda3/lib/python3.12/site-packages (from torch) (12.3.1.170)
Requirement already satisfied: nvidia-nccl-cu12==2.21.5 in /root/miniconda3/lib/python3.12/site-packages (from torch) (2.21.5)
Requirement already satisfied: nvidia-nvtx-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch) (12.4.127)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch) (12.4.127)
Requirement already satisfied: triton==3.1.0 in /root/miniconda3/lib/python3.12/site-packages (from torch) (3.1.0)
Requirement already satisfied: setuptools in /root/miniconda3/lib/python3.12/site-packages (from torch) (69.5.1)
Requirement already satisfied: sympy==1.13.1 in /root/miniconda3/lib/python3.12/site-packages (from torch) (1.13.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /root/miniconda3/lib/python3.12/site-packages (from sympy==1.13.1->torch) (1.3.0)
Requirement already satisfied: numpy in /root/miniconda3/lib/python3.12/site-packages (from torchvision) (1.26.4)
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /root/miniconda3/lib/python3.12/site-packages (from torchvision) (10.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in /root/miniconda3/lib/python3.12/site-packages (from jinja2->torch) (2.1.5)
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# OMP_NUM_THREADS=1 python -m torch.distributed.launch --nproc_per_node=4 train.py
/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py:208: FutureWarning: The module torch.distributed.launch is deprecated
and will be removed in future. Use torchrun.
Note that --use-env is set by default in torchrun.
If your script expects `--local-rank` argument to be set, please
change it to read from `os.environ['LOCAL_RANK']` instead. See 
https://pytorch.org/docs/stable/distributed.html#launch-utility for 
further instructions

  main()
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 5, in <module>
    import misc
  File "/root/TCL/2022-IJCV-TCL-main/misc.py", line 21, in <module>
    from torch._six import inf
ModuleNotFoundError: No module named 'torch._six'
W1026 20:22:46.969000 2239 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2242 closing signal SIGTERM
W1026 20:22:46.971000 2239 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2243 closing signal SIGTERM
E1026 20:22:47.004000 2239 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 2 (pid: 2244) of binary: /root/miniconda3/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 208, in <module>
    main()
  File "/root/miniconda3/lib/python3.12/site-packages/typing_extensions.py", line 2853, in wrapper
    return arg(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 204, in main
    launch(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 189, in launch
    run(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/run.py", line 910, in run
    elastic_launch(
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
train.py FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2024-10-26_20:22:46
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 3 (local_rank: 3)
  exitcode  : 1 (pid: 2245)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2024-10-26_20:22:46
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 2244)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# OMP_NUM_THREADS=1 python -m torch.distributed.launch --nproc_per_node=4 train.py
/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py:208: FutureWarning: The module torch.distributed.launch is deprecated
and will be removed in future. Use torchrun.
Note that --use-env is set by default in torchrun.
If your script expects `--local-rank` argument to be set, please
change it to read from `os.environ['LOCAL_RANK']` instead. See 
https://pytorch.org/docs/stable/distributed.html#launch-utility for 
further instructions

  main()
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 12, in <module>
    from model import get_resnet, Network
  File "/root/TCL/2022-IJCV-TCL-main/model.py", line 5, in <module>
    from timm.models.layers import trunc_normal_
ModuleNotFoundError: No module named 'timm'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 12, in <module>
    from model import get_resnet, Network
  File "/root/TCL/2022-IJCV-TCL-main/model.py", line 5, in <module>
    from timm.models.layers import trunc_normal_
ModuleNotFoundError: No module named 'timm'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 12, in <module>
    from model import get_resnet, Network
  File "/root/TCL/2022-IJCV-TCL-main/model.py", line 5, in <module>
    from timm.models.layers import trunc_normal_
ModuleNotFoundError: No module named 'timm'
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 12, in <module>
    from model import get_resnet, Network
  File "/root/TCL/2022-IJCV-TCL-main/model.py", line 5, in <module>
    from timm.models.layers import trunc_normal_
ModuleNotFoundError: No module named 'timm'
W1026 20:25:50.746000 2313 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2315 closing signal SIGTERM
W1026 20:25:50.746000 2313 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2318 closing signal SIGTERM
E1026 20:25:50.779000 2313 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 1 (pid: 2316) of binary: /root/miniconda3/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 208, in <module>
    main()
  File "/root/miniconda3/lib/python3.12/site-packages/typing_extensions.py", line 2853, in wrapper
    return arg(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 204, in main
    launch(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 189, in launch
    run(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/run.py", line 910, in run
    elastic_launch(
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
train.py FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2024-10-26_20:25:50
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 2317)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2024-10-26_20:25:50
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 2316)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# pip install timm
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting timm
  Downloading http://mirrors.aliyun.com/pypi/packages/77/f7/144d69d921fba82baa8498e279d782a12a13694f45ff74d1777bc3231ffe/timm-1.0.11-py3-none-any.whl (2.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 10.7 MB/s eta 0:00:00
Requirement already satisfied: torch in /root/miniconda3/lib/python3.12/site-packages (from timm) (2.5.0)
Requirement already satisfied: torchvision in /root/miniconda3/lib/python3.12/site-packages (from timm) (0.20.0)
Requirement already satisfied: pyyaml in /root/miniconda3/lib/python3.12/site-packages (from timm) (6.0.1)
Collecting huggingface_hub (from timm)
  Downloading http://mirrors.aliyun.com/pypi/packages/d7/4d/017d8d7cff5100092da8ea19139bcb1965bbadcbb5ddd0480e2badc299e8/huggingface_hub-0.26.1-py3-none-any.whl (447 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 447.4/447.4 kB 26.3 MB/s eta 0:00:00
Collecting safetensors (from timm)
  Downloading http://mirrors.aliyun.com/pypi/packages/d9/40/a6f75ea449a9647423ec8b6f72c16998d35aa4b43cb38536ac060c5c7bf5/safetensors-0.4.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (434 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 434.8/434.8 kB 22.2 MB/s eta 0:00:00
Requirement already satisfied: filelock in /root/miniconda3/lib/python3.12/site-packages (from huggingface_hub->timm) (3.14.0)
Requirement already satisfied: fsspec>=2023.5.0 in /root/miniconda3/lib/python3.12/site-packages (from huggingface_hub->timm) (2024.5.0)
Requirement already satisfied: packaging>=20.9 in /root/miniconda3/lib/python3.12/site-packages (from huggingface_hub->timm) (23.2)
Requirement already satisfied: requests in /root/miniconda3/lib/python3.12/site-packages (from huggingface_hub->timm) (2.31.0)
Requirement already satisfied: tqdm>=4.42.1 in /root/miniconda3/lib/python3.12/site-packages (from huggingface_hub->timm) (4.66.2)
Requirement already satisfied: typing-extensions>=3.7.4.3 in /root/miniconda3/lib/python3.12/site-packages (from huggingface_hub->timm) (4.12.1)
Requirement already satisfied: networkx in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (3.3)
Requirement already satisfied: jinja2 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (3.1.4)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (12.4.127)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (12.4.127)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (12.4.127)
Requirement already satisfied: nvidia-cudnn-cu12==9.1.0.70 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (9.1.0.70)
Requirement already satisfied: nvidia-cublas-cu12==12.4.5.8 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (12.4.5.8)
Requirement already satisfied: nvidia-cufft-cu12==11.2.1.3 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (11.2.1.3)
Requirement already satisfied: nvidia-curand-cu12==10.3.5.147 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (10.3.5.147)
Requirement already satisfied: nvidia-cusolver-cu12==11.6.1.9 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (11.6.1.9)
Requirement already satisfied: nvidia-cusparse-cu12==12.3.1.170 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (12.3.1.170)
Requirement already satisfied: nvidia-nccl-cu12==2.21.5 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (2.21.5)
Requirement already satisfied: nvidia-nvtx-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (12.4.127)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.4.127 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (12.4.127)
Requirement already satisfied: triton==3.1.0 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (3.1.0)
Requirement already satisfied: setuptools in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (69.5.1)
Requirement already satisfied: sympy==1.13.1 in /root/miniconda3/lib/python3.12/site-packages (from torch->timm) (1.13.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /root/miniconda3/lib/python3.12/site-packages (from sympy==1.13.1->torch->timm) (1.3.0)
Requirement already satisfied: numpy in /root/miniconda3/lib/python3.12/site-packages (from torchvision->timm) (1.26.4)
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /root/miniconda3/lib/python3.12/site-packages (from torchvision->timm) (10.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in /root/miniconda3/lib/python3.12/site-packages (from jinja2->torch->timm) (2.1.5)
Requirement already satisfied: charset-normalizer<4,>=2 in /root/miniconda3/lib/python3.12/site-packages (from requests->huggingface_hub->timm) (2.0.4)
Requirement already satisfied: idna<4,>=2.5 in /root/miniconda3/lib/python3.12/site-packages (from requests->huggingface_hub->timm) (3.7)
Requirement already satisfied: urllib3<3,>=1.21.1 in /root/miniconda3/lib/python3.12/site-packages (from requests->huggingface_hub->timm) (2.1.0)
Requirement already satisfied: certifi>=2017.4.17 in /root/miniconda3/lib/python3.12/site-packages (from requests->huggingface_hub->timm) (2024.2.2)
Installing collected packages: safetensors, huggingface_hub, timm
Successfully installed huggingface_hub-0.26.1 safetensors-0.4.5 timm-1.0.11
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# OMP_NUM_THREADS=1 python -m torch.distributed.launch --nproc_per_node=4 train.py
/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py:208: FutureWarning: The module torch.distributed.launch is deprecated
and will be removed in future. Use torchrun.
Note that --use-env is set by default in torchrun.
If your script expects `--local-rank` argument to be set, please
change it to read from `os.environ['LOCAL_RANK']` instead. See 
https://pytorch.org/docs/stable/distributed.html#launch-utility for 
further instructions

  main()
/root/miniconda3/lib/python3.12/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
/root/miniconda3/lib/python3.12/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 14, in <module>
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 14, in <module>
    from loss import InstanceLoss, ClusterLoss
  File "/root/TCL/2022-IJCV-TCL-main/loss.py", line 5, in <module>
    from loss import InstanceLoss, ClusterLoss
    import diffdist
  File "/root/TCL/2022-IJCV-TCL-main/loss.py", line 5, in <module>
ModuleNotFoundError: No module named 'diffdist'
    import diffdist
ModuleNotFoundError: No module named 'diffdist'
/root/miniconda3/lib/python3.12/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 14, in <module>
    from loss import InstanceLoss, ClusterLoss
  File "/root/TCL/2022-IJCV-TCL-main/loss.py", line 5, in <module>
    import diffdist
ModuleNotFoundError: No module named 'diffdist'
/root/miniconda3/lib/python3.12/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
Traceback (most recent call last):
  File "/root/TCL/2022-IJCV-TCL-main/train.py", line 14, in <module>
    from loss import InstanceLoss, ClusterLoss
  File "/root/TCL/2022-IJCV-TCL-main/loss.py", line 5, in <module>
    import diffdist
ModuleNotFoundError: No module named 'diffdist'
W1026 20:26:43.868000 2338 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2341 closing signal SIGTERM
W1026 20:26:43.869000 2338 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2344 closing signal SIGTERM
E1026 20:26:43.902000 2338 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 1 (pid: 2342) of binary: /root/miniconda3/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 208, in <module>
    main()
  File "/root/miniconda3/lib/python3.12/site-packages/typing_extensions.py", line 2853, in wrapper
    return arg(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 204, in main
    launch(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 189, in launch
    run(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/run.py", line 910, in run
    elastic_launch(
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
train.py FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2024-10-26_20:26:43
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 2343)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2024-10-26_20:26:43
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 2342)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# pip install diffdist
Looking in indexes: http://mirrors.aliyun.com/pypi/simple
Collecting diffdist
  Downloading http://mirrors.aliyun.com/pypi/packages/b6/ec/f4e8855bd10f030f391cfad51dd52b37ce9017af25b3e80a67ca80d5d14e/diffdist-0.1.tar.gz (4.6 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: diffdist
  Building wheel for diffdist (setup.py) ... done
  Created wheel for diffdist: filename=diffdist-0.1-py3-none-any.whl size=6536 sha256=1d0edf5c88cfc78c6522ae7dcef8ee5f3e27f00e20e368f2d621eadc961aedff
  Stored in directory: /root/.cache/pip/wheels/30/32/a6/3d10f437e1fc22d8cc1d37282e933e10dfbffb27335ff5b60e
Successfully built diffdist
Installing collected packages: diffdist
Successfully installed diffdist-0.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# OMP_NUM_THREADS=1 python -m torch.distributed.launch --nproc_per_node=4 train.py
/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py:208: FutureWarning: The module torch.distributed.launch is deprecated
and will be removed in future. Use torchrun.
Note that --use-env is set by default in torchrun.
If your script expects `--local-rank` argument to be set, please
change it to read from `os.environ['LOCAL_RANK']` instead. See 
https://pytorch.org/docs/stable/distributed.html#launch-utility for 
further instructions

  main()
/root/miniconda3/lib/python3.12/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
/root/miniconda3/lib/python3.12/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
/root/miniconda3/lib/python3.12/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
/root/miniconda3/lib/python3.12/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
usage: TCL [--batch_size BATCH_SIZE] [--epochs EPOCHS] [--model MODEL] [--feat_dim FEAT_DIM] [--ins_temp INS_TEMP] [--clu_temp CLU_TEMP] [--weight_decay WEIGHT_DECAY] [--lr LR]
           [--data_path DATA_PATH] [--dataset {CIFAR-10,CIFAR-100,ImageNet-10,ImageNet}] [--nb_cluster NB_CLUSTER] [--output_dir OUTPUT_DIR] [--device DEVICE] [--seed SEED] [--resume RESUME]
           [--start_epoch N] [--save_freq SAVE_FREQ] [--eval_freq EVAL_FREQ] [--num_workers NUM_WORKERS] [--pin_mem] [--dist_eval] [--world_size WORLD_SIZE] [--local_rank LOCAL_RANK] [--dist_on_itp]
           [--dist_url DIST_URL]
TCL: error: unrecognized arguments: --local-rank=1
usage: TCL [--batch_size BATCH_SIZE] [--epochs EPOCHS] [--model MODEL] [--feat_dim FEAT_DIM] [--ins_temp INS_TEMP] [--clu_temp CLU_TEMP] [--weight_decay WEIGHT_DECAY] [--lr LR]
           [--data_path DATA_PATH] [--dataset {CIFAR-10,CIFAR-100,ImageNet-10,ImageNet}] [--nb_cluster NB_CLUSTER] [--output_dir OUTPUT_DIR] [--device DEVICE] [--seed SEED] [--resume RESUME]
           [--start_epoch N] [--save_freq SAVE_FREQ] [--eval_freq EVAL_FREQ] [--num_workers NUM_WORKERS] [--pin_mem] [--dist_eval] [--world_size WORLD_SIZE] [--local_rank LOCAL_RANK] [--dist_on_itp]
           [--dist_url DIST_URL]
TCL: error: unrecognized arguments: --local-rank=2
usage: TCL [--batch_size BATCH_SIZE] [--epochs EPOCHS] [--model MODEL] [--feat_dim FEAT_DIM] [--ins_temp INS_TEMP] [--clu_temp CLU_TEMP] [--weight_decay WEIGHT_DECAY] [--lr LR]
           [--data_path DATA_PATH] [--dataset {CIFAR-10,CIFAR-100,ImageNet-10,ImageNet}] [--nb_cluster NB_CLUSTER] [--output_dir OUTPUT_DIR] [--device DEVICE] [--seed SEED] [--resume RESUME]
           [--start_epoch N] [--save_freq SAVE_FREQ] [--eval_freq EVAL_FREQ] [--num_workers NUM_WORKERS] [--pin_mem] [--dist_eval] [--world_size WORLD_SIZE] [--local_rank LOCAL_RANK] [--dist_on_itp]
           [--dist_url DIST_URL]
TCL: error: unrecognized arguments: --local-rank=0
usage: TCL [--batch_size BATCH_SIZE] [--epochs EPOCHS] [--model MODEL] [--feat_dim FEAT_DIM] [--ins_temp INS_TEMP] [--clu_temp CLU_TEMP] [--weight_decay WEIGHT_DECAY] [--lr LR]
           [--data_path DATA_PATH] [--dataset {CIFAR-10,CIFAR-100,ImageNet-10,ImageNet}] [--nb_cluster NB_CLUSTER] [--output_dir OUTPUT_DIR] [--device DEVICE] [--seed SEED] [--resume RESUME]
           [--start_epoch N] [--save_freq SAVE_FREQ] [--eval_freq EVAL_FREQ] [--num_workers NUM_WORKERS] [--pin_mem] [--dist_eval] [--world_size WORLD_SIZE] [--local_rank LOCAL_RANK] [--dist_on_itp]
           [--dist_url DIST_URL]
TCL: error: unrecognized arguments: --local-rank=3
W1026 20:27:25.955000 2360 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2363 closing signal SIGTERM
W1026 20:27:25.956000 2360 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 2366 closing signal SIGTERM
E1026 20:27:26.020000 2360 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 2) local_rank: 1 (pid: 2364) of binary: /root/miniconda3/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 208, in <module>
    main()
  File "/root/miniconda3/lib/python3.12/site-packages/typing_extensions.py", line 2853, in wrapper
    return arg(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 204, in main
    launch(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launch.py", line 189, in launch
    run(args)
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/run.py", line 910, in run
    elastic_launch(
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
train.py FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2024-10-26_20:27:25
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 2 (local_rank: 2)
  exitcode  : 2 (pid: 2365)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2024-10-26_20:27:25
  host      : autodl-container-7c5d4696fb-c54fea2a
  rank      : 1 (local_rank: 1)
  exitcode  : 2 (pid: 2364)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
root@autodl-container-7c5d4696fb-c54fea2a:~/TCL/2022-IJCV-TCL-main# 
```
