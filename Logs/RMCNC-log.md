数据集报错 ???   FileNotFoundError: [Errno 2] No such file or directory: './datasets/AWA-7view-10158sample.mat'

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
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 17, in _open_file_context
    f, opened = _open_file(file_like, appendmat, mode)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 45, in _open_file
    return open(file_like, mode), True
           ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: './datasets/AWA-7view-10158sample.mat'
^C
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# 

```
