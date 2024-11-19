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


```linux
root@autodl-container-01d54ca695-bbf2e908:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# sh train.sh
train.sh: 26: 5-DeepAnimal: not found
====================================================================================
================================alignment rate: 0.5 ================================
====================================================================================
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.0833 , nmi= 0.0942 , ari= 0.0183 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4432 , nmi= 0.496 , ari= 0.2994 , loss= 0.4999931901693344
******** End, training time = 137.11 s ********
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.0823 , nmi= 0.0937 , ari= 0.021 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4406 , nmi= 0.4906 , ari= 0.2972 , loss= 0.49999313354492186
******** End, training time = 140.15 s ********
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.0748 , nmi= 0.0836 , ari= 0.0168 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.457 , nmi= 0.4944 , ari= 0.3053 , loss= 0.4999931246042252
******** End, training time = 142.46 s ********
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.076 , nmi= 0.0856 , ari= 0.0176 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4299 , nmi= 0.4863 , ari= 0.2934 , loss= 0.49999313354492186
******** End, training time = 137.69 s ********
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.0756 , nmi= 0.0836 , ari= 0.0161 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4477 , nmi= 0.4828 , ari= 0.293 , loss= 0.49999321699142457
******** End, training time = 143.46 s ********
====================================================================================
================================alignment rate: 1 ================================
====================================================================================





----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.0796 , nmi= 0.0899 , ari= 0.0199 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4632 , nmi= 0.5844 , ari= 0.3703 , loss= 0.4999812364578247
******** End, training time = 186.85 s ********
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.0765 , nmi= 0.0838 , ari= 0.0156 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4742 , nmi= 0.58 , ari= 0.3707 , loss= 0.4999811887741089
******** End, training time = 188.43 s ********
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.074 , nmi= 0.079 , ari= 0.0151 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4797 , nmi= 0.5833 , ari= 0.3724 , loss= 0.4999812334775925
******** End, training time = 181.72 s ********
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.0635 , nmi= 0.0724 , ari= 0.01 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4839 , nmi= 0.5872 , ari= 0.3776 , loss= 0.4999812215566635
******** End, training time = 183.66 s ********
----------------------Training with noisy_correspondence----------------------
******** Training begin ********
=======> Train epoch: 0/120
Clustering: acc= 0.0762 , nmi= 0.0869 , ari= 0.0168 , loss= 0.49999951422214506
=======> Train epoch: 120/120
Clustering: acc= 0.4806 , nmi= 0.5856 , ari= 0.3777 , loss= 0.49998125433921814
******** End, training time = 188.57 s ********
```
