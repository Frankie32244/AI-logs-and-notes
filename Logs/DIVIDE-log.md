只可以跑Scene 和 Caltech101 两个数据集 ??
```linux
root@autodl-container-7c5d4696fb-c54fea2a:~# git clone https://github.com/XLearning-SCU/2024-AAAI-DIVIDE
Cloning into '2024-AAAI-DIVIDE'...
remote: Enumerating objects: 46, done.
remote: Counting objects: 100% (46/46), done.
remote: Compressing objects: 100% (39/39), done.
remote: Total 46 (delta 16), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (46/46), 181.37 KiB | 599.00 KiB/s, done.
Resolving deltas: 100% (16/16), done.
root@autodl-container-7c5d4696fb-c54fea2a:~# 
root@autodl-container-7c5d4696fb-c54fea2a:~# 
root@autodl-container-7c5d4696fb-c54fea2a:~# 
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
2024-AAAI-DIVIDE  CVCL  Pro-Imp  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# cd ls
bash: cd: ls: No such file or directory
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
CVCL  DIVIDE  Pro-Imp  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# cd DIVIDE/
root@autodl-container-7c5d4696fb-c54fea2a:~/DIVIDE# ls
README.md  config  dataset_loader.py  engine_train.py  figure  main_train.py  model.py  utils.py
root@autodl-container-7c5d4696fb-c54fea2a:~/DIVIDE# python main_train.py --config_file=config/Scene15.yaml

enable cudnn.deterministic, seed fixed: 0
Traceback (most recent call last):
  File "/root/miniconda3/lib/python3.12/site-packages/scipy/io/matlab/_mio.py", line 39, in _open_file
    return open(file_like, mode), True
           ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data/multiview/Scene_15.mat'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/root/DIVIDE/main_train.py", line 203, in <module>
    main(args)
  File "/root/DIVIDE/main_train.py", line 161, in main
    train_state = train_one_time(args, state_logger)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/DIVIDE/main_train.py", line 85, in train_one_time
    dataset = load_dataset(args)
              ^^^^^^^^^^^^^^^^^^
  File "/root/DIVIDE/dataset_loader.py", line 60, in load_dataset
    data, targets = load_mat(args)
                    ^^^^^^^^^^^^^^
  File "/root/DIVIDE/dataset_loader.py", line 15, in load_mat
    mat = sio.loadmat(os.path.join(args.data_path, 'Scene_15.mat'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
FileNotFoundError: [Errno 2] No such file or directory: 'data/multiview/Scene_15.mat'
root@autodl-container-7c5d4696fb-c54fea2a:~/DIVIDE# ls
DIVIDE  README.md  __pycache__  config  dataset_loader.py  engine_train.py  figure  main_train.py  model.py  utils.py
root@autodl-container-7c5d4696fb-c54fea2a:~/DIVIDE# python main_train.py --config_file=config/Scene15.yaml

enable cudnn.deterministic, seed fixed: 0
job dir: /root/DIVIDE
Batch size: 1024
Start time: 2024-10-26 18:47
Train parameters: Namespace(config_file='config/Scene15.yaml',
encoder_dim=[[20,
1024,
1024,
1024,
128],
[59,
1024,
1024,
1024,
128]],
embed_dim=128,
temperature=0.5,
start_rectify_epoch=100,
momentum=0.98,
drop_rate=0.2,
n_views=2,
n_classes=15,
batch_size=1024,
epochs=200,
warmup_epochs=20,
data_norm='standard',
train_time=5,
weight_decay=0,
lr=0.002,
dataset='Scene15',
missing_rate=0.0,
data_path='data/multiview',
device='cuda',
output_dir='DIVIDE/Scene15_msrt_0.0_tau_0.5_bs_1024_blr_0.0005',
print_freq=50,
start_epoch=0,
num_workers=8,
seed=0,
pin_mem=True,
blr=0.0005,
train_id=0,
n_sample=4485)
DIVIDE(
  (online_encoder): ModuleList(
    (0): FCN(
      (ffn): Sequential(
        (0): Linear(in_features=20, out_features=1024, bias=False)
        (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (2): ReLU()
        (3): Dropout(p=0.2, inplace=False)
        (4): Linear(in_features=1024, out_features=1024, bias=False)
        (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (6): ReLU()
        (7): Dropout(p=0.2, inplace=False)
        (8): Linear(in_features=1024, out_features=1024, bias=False)
        (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (10): ReLU()
        (11): Linear(in_features=1024, out_features=128, bias=False)
        (12): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
    )
    (1): FCN(
      (ffn): Sequential(
        (0): Linear(in_features=59, out_features=1024, bias=False)
        (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (2): ReLU()
        (3): Dropout(p=0.2, inplace=False)
        (4): Linear(in_features=1024, out_features=1024, bias=False)
        (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (6): ReLU()
        (7): Dropout(p=0.2, inplace=False)
        (8): Linear(in_features=1024, out_features=1024, bias=False)
        (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (10): ReLU()
        (11): Linear(in_features=1024, out_features=128, bias=False)
        (12): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
    )
  )
  (target_encoder): ModuleList(
    (0): FCN(
      (ffn): Sequential(
        (0): Linear(in_features=20, out_features=1024, bias=False)
        (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (2): ReLU()
        (3): Dropout(p=0.2, inplace=False)
        (4): Linear(in_features=1024, out_features=1024, bias=False)
        (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (6): ReLU()
        (7): Dropout(p=0.2, inplace=False)
        (8): Linear(in_features=1024, out_features=1024, bias=False)
        (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (10): ReLU()
        (11): Linear(in_features=1024, out_features=128, bias=False)
        (12): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
    )
    (1): FCN(
      (ffn): Sequential(
        (0): Linear(in_features=59, out_features=1024, bias=False)
        (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (2): ReLU()
        (3): Dropout(p=0.2, inplace=False)
        (4): Linear(in_features=1024, out_features=1024, bias=False)
        (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (6): ReLU()
        (7): Dropout(p=0.2, inplace=False)
        (8): Linear(in_features=1024, out_features=1024, bias=False)
        (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (10): ReLU()
        (11): Linear(in_features=1024, out_features=128, bias=False)
        (12): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
    )
  )
  (cross_view_decoder): ModuleList(
    (0-1): 2 x MLP(
      (mlp): Sequential(
        (0): Linear(in_features=128, out_features=512, bias=True)
        (1): ReLU()
        (2): Linear(in_features=512, out_features=128, bias=True)
      )
    )
  )
  (cl): ContrastiveLoss()
)
Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.99)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.002
    maximize: False
    weight_decay: 0
)
Data loaded: there are 4485 samples.

>> Start training 0-th initial, seed: 0,
Epoch: [49]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2378  data: 0.2117  max mem: 200
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0691  data: 0.0530  max mem: 200
Epoch: [49] Total time: 0:00:00 (0.0769 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4511 ARI = 0.2815 F = 0.3318 ACC = 0.4533
Epoch: [99]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2581  data: 0.2316  max mem: 200
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0738  data: 0.0579  max mem: 200
Epoch: [99] Total time: 0:00:00 (0.0816 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4598 ARI = 0.2874 F = 0.3368 ACC = 0.4526
Epoch: [149]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2730  data: 0.2438  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0777  data: 0.0610  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0854 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4754 ARI = 0.3006 F = 0.3499 ACC = 0.4388
Epoch: [199]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2460  data: 0.2119  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0737  data: 0.0530  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.0819 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4549 ARI = 0.2785 F = 0.3291 ACC = 0.4326

enable cudnn.deterministic, seed fixed: 1

>> Start training 1-th initial, seed: 1,
Epoch: [49]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2427  data: 0.2160  max mem: 204
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0715  data: 0.0552  max mem: 204
Epoch: [49] Total time: 0:00:00 (0.0795 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4654 ARI = 0.2936 F = 0.3428 ACC = 0.4673
Epoch: [99]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2404  data: 0.2147  max mem: 204
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0693  data: 0.0537  max mem: 204
Epoch: [99] Total time: 0:00:00 (0.0774 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4540 ARI = 0.2858 F = 0.3353 ACC = 0.4439
Epoch: [149]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2460  data: 0.2174  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0733  data: 0.0544  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0812 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4807 ARI = 0.3150 F = 0.3632 ACC = 0.4919
Epoch: [199]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2620  data: 0.2319  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0769  data: 0.0580  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.0851 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4710 ARI = 0.2940 F = 0.3450 ACC = 0.4685

enable cudnn.deterministic, seed fixed: 2

>> Start training 2-th initial, seed: 2,
Epoch: [49]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2458  data: 0.2226  max mem: 204
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0704  data: 0.0557  max mem: 204
Epoch: [49] Total time: 0:00:00 (0.0782 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4635 ARI = 0.2981 F = 0.3472 ACC = 0.4747
Epoch: [99]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2637  data: 0.2348  max mem: 204
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0751  data: 0.0587  max mem: 204
Epoch: [99] Total time: 0:00:00 (0.0829 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4595 ARI = 0.2887 F = 0.3383 ACC = 0.4758
Epoch: [149]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2573  data: 0.2266  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0757  data: 0.0567  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0840 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4652 ARI = 0.2996 F = 0.3483 ACC = 0.4401
Epoch: [199]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2551  data: 0.2233  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0748  data: 0.0559  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.0831 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4660 ARI = 0.2805 F = 0.3319 ACC = 0.4502

enable cudnn.deterministic, seed fixed: 3

>> Start training 3-th initial, seed: 3,
Epoch: [49]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2473  data: 0.2229  max mem: 204
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0710  data: 0.0558  max mem: 204
Epoch: [49] Total time: 0:00:00 (0.0792 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4366 ARI = 0.2541 F = 0.3085 ACC = 0.3960
Epoch: [99]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2473  data: 0.2191  max mem: 204
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0713  data: 0.0548  max mem: 204
Epoch: [99] Total time: 0:00:00 (0.0795 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4689 ARI = 0.3005 F = 0.3488 ACC = 0.4778
Epoch: [149]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2443  data: 0.2157  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0722  data: 0.0540  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0801 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4797 ARI = 0.3035 F = 0.3529 ACC = 0.4649
Epoch: [199]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2447  data: 0.2150  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0732  data: 0.0538  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.0813 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4915 ARI = 0.3133 F = 0.3630 ACC = 0.4954

enable cudnn.deterministic, seed fixed: 4

>> Start training 4-th initial, seed: 4,
Epoch: [49]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2501  data: 0.2249  max mem: 204
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0729  data: 0.0563  max mem: 204
Epoch: [49] Total time: 0:00:00 (0.0807 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4433 ARI = 0.2695 F = 0.3200 ACC = 0.4158
Epoch: [99]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2465  data: 0.2188  max mem: 204
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0721  data: 0.0547  max mem: 204
Epoch: [99] Total time: 0:00:00 (0.0805 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4710 ARI = 0.3123 F = 0.3602 ACC = 0.4907
Epoch: [149]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2556  data: 0.2315  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0757  data: 0.0579  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0838 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4820 ARI = 0.3091 F = 0.3580 ACC = 0.4491
Epoch: [199]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2489  data: 0.2211  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0776  data: 0.0592  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.0855 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4904 ARI = 0.3238 F = 0.3714 ACC = 0.5012

Training time 0:05:40

Average K-means Result: ACC = 46.96(2.61) NMI = 47.48(1.42) ARI = 29.80(1.79)
root@autodl-container-7c5d4696fb-c54fea2a:~/DIVIDE# 

```



2024-10-30 跑的一个结果

```linux
root@autodl-container-04e2498428-551163cf:~/2024-AAAI-DIVIDE# tar -czvf folder.tar.gz ./
./
./.git/
./.git/branches/
./.git/hooks/
./.git/hooks/applypatch-msg.sample
./.git/hooks/commit-msg.sample
./.git/hooks/fsmonitor-watchman.sample
./.git/hooks/post-update.sample
./.git/hooks/pre-applypatch.sample
./.git/hooks/pre-commit.sample
./.git/hooks/pre-merge-commit.sample
./.git/hooks/pre-push.sample
./.git/hooks/pre-rebase.sample
./.git/hooks/pre-receive.sample
./.git/hooks/prepare-commit-msg.sample
./.git/hooks/push-to-checkout.sample
./.git/hooks/update.sample
./.git/info/
./.git/info/exclude
./.git/logs/
./.git/logs/refs/
./.git/logs/refs/heads/
./.git/logs/refs/heads/main
./.git/logs/refs/remotes/
./.git/logs/refs/remotes/origin/
./.git/logs/refs/remotes/origin/HEAD
./.git/logs/HEAD
./.git/objects/
./.git/objects/info/
./.git/objects/pack/
./.git/objects/pack/pack-e2449f3ec7d096bc0373eb8406af43c329d4c910.idx
./.git/objects/pack/pack-e2449f3ec7d096bc0373eb8406af43c329d4c910.pack
./.git/refs/
./.git/refs/heads/
./.git/refs/heads/main
./.git/refs/remotes/
./.git/refs/remotes/origin/
./.git/refs/remotes/origin/HEAD
./.git/refs/tags/
./.git/HEAD
./.git/config
./.git/description
./.git/index
./.git/packed-refs
./.ipynb_checkpoints/
./.ipynb_checkpoints/main_train-checkpoint.py
./.ipynb_checkpoints/model-checkpoint.py
./DIVIDE/
./DIVIDE/Scene15_msrt_0.0_tau_0.5_bs_1024_blr_0.0005/
./DIVIDE/Scene15_msrt_0.0_tau_0.5_bs_1024_blr_0.0005/visualize/
./DIVIDE/Scene15_msrt_0.0_tau_0.5_bs_1024_blr_0.0005/log_train.txt
./__pycache__/
./__pycache__/dataset_loader.cpython-312.pyc
./__pycache__/engine_train.cpython-312.pyc
./__pycache__/model.cpython-312.pyc
./__pycache__/utils.cpython-312.pyc
./config/
./config/Caltech101.yaml
./config/Scene15.yaml
./data/
./data/.ipynb_checkpoints/
./data/multiview/
./data/multiview/Scene_15.mat
./figure/
./figure/Overview.png
./ge/
./ge/.ipynb_checkpoints/
./ge/.ipynb_checkpoints/alias-checkpoint.py
./ge/.ipynb_checkpoints/utils-checkpoint.py
./ge/__pycache__/
./ge/__pycache__/__init__.cpython-312.pyc
./ge/__pycache__/alias.cpython-312.pyc
./ge/__pycache__/utils.cpython-312.pyc
./ge/__pycache__/walker.cpython-312.pyc
./ge/models/
./ge/models/.ipynb_checkpoints/
./ge/models/.ipynb_checkpoints/line-checkpoint.py
./ge/models/__pycache__/
./ge/models/__pycache__/__init__.cpython-312.pyc
./ge/models/__pycache__/deepwalk.cpython-312.pyc
./ge/models/__pycache__/line.cpython-312.pyc
./ge/models/__pycache__/node2vec.cpython-312.pyc
./ge/models/__pycache__/sdne.cpython-312.pyc
./ge/models/__pycache__/struc2vec.cpython-312.pyc
./ge/models/__init__.py
./ge/models/deepwalk.py
./ge/models/line.py
./ge/models/node2vec.py
./ge/models/sdne.py
./ge/models/struc2vec.py
./ge/__init__.py
./ge/alias.py
./ge/classify.py
./ge/utils.py
./ge/walker.py
./README.md
./dataset_loader.py
./engine_train.py
./main_train.py
./model.py
./utils.py
tar: .: file changed as we read it
root@autodl-container-04e2498428-551163cf:~/2024-AAAI-DIVIDE# python main_train.py --config_file=config/Scene15.yaml
2024-10-30 15:24:48.302198: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2024-10-30 15:24:48.318121: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1730273088.340289    1310 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1730273088.345988    1310 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2024-10-30 15:24:48.365651: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.

enable cudnn.deterministic, seed fixed: 0
job dir: /root/2024-AAAI-DIVIDE
Batch size: 1024
Start time: 2024-10-30 15:24
Train parameters: Namespace(config_file='config/Scene15.yaml',
encoder_dim=[[20,
1024,
1024,
1024,
128],
[59,
1024,
1024,
1024,
128]],
embed_dim=128,
temperature=0.5,
start_rectify_epoch=100,
momentum=0.98,
drop_rate=0.2,
n_views=2,
n_classes=15,
batch_size=1024,
epochs=200,
warmup_epochs=20,
data_norm='standard',
train_time=5,
weight_decay=0,
lr=0.002,
dataset='Scene15',
missing_rate=0.0,
data_path='data/multiview',
device='cuda',
output_dir='DIVIDE/Scene15_msrt_0.0_tau_0.5_bs_1024_blr_0.0005',
print_freq=50,
start_epoch=0,
num_workers=8,
seed=0,
pin_mem=True,
blr=0.0005,
train_id=0,
n_sample=4485)
DIVIDE(
  (online_encoder): ModuleList(
    (0): FCN(
      (ffn): Sequential(
        (0): Linear(in_features=20, out_features=1024, bias=False)
        (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (2): ReLU()
        (3): Dropout(p=0.2, inplace=False)
        (4): Linear(in_features=1024, out_features=1024, bias=False)
        (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (6): ReLU()
        (7): Dropout(p=0.2, inplace=False)
        (8): Linear(in_features=1024, out_features=1024, bias=False)
        (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (10): ReLU()
        (11): Linear(in_features=1024, out_features=128, bias=False)
        (12): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
    )
    (1): FCN(
      (ffn): Sequential(
        (0): Linear(in_features=59, out_features=1024, bias=False)
        (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (2): ReLU()
        (3): Dropout(p=0.2, inplace=False)
        (4): Linear(in_features=1024, out_features=1024, bias=False)
        (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (6): ReLU()
        (7): Dropout(p=0.2, inplace=False)
        (8): Linear(in_features=1024, out_features=1024, bias=False)
        (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (10): ReLU()
        (11): Linear(in_features=1024, out_features=128, bias=False)
        (12): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
    )
  )
  (target_encoder): ModuleList(
    (0): FCN(
      (ffn): Sequential(
        (0): Linear(in_features=20, out_features=1024, bias=False)
        (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (2): ReLU()
        (3): Dropout(p=0.2, inplace=False)
        (4): Linear(in_features=1024, out_features=1024, bias=False)
        (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (6): ReLU()
        (7): Dropout(p=0.2, inplace=False)
        (8): Linear(in_features=1024, out_features=1024, bias=False)
        (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (10): ReLU()
        (11): Linear(in_features=1024, out_features=128, bias=False)
        (12): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
    )
    (1): FCN(
      (ffn): Sequential(
        (0): Linear(in_features=59, out_features=1024, bias=False)
        (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (2): ReLU()
        (3): Dropout(p=0.2, inplace=False)
        (4): Linear(in_features=1024, out_features=1024, bias=False)
        (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (6): ReLU()
        (7): Dropout(p=0.2, inplace=False)
        (8): Linear(in_features=1024, out_features=1024, bias=False)
        (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        (10): ReLU()
        (11): Linear(in_features=1024, out_features=128, bias=False)
        (12): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=True)
      )
    )
  )
  (cross_view_decoder): ModuleList(
    (0-1): 2 x MLP(
      (mlp): Sequential(
        (0): Linear(in_features=128, out_features=512, bias=True)
        (1): ReLU()
        (2): Linear(in_features=512, out_features=128, bias=True)
      )
    )
  )
  (cl): ContrastiveLoss()
)
Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.99)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.002
    maximize: False
    weight_decay: 0
)
Data loaded: there are 4485 samples.

>> Start training 0-th initial, seed: 0,
Epoch: [49]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2210  data: 0.1936  max mem: 200
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0689  data: 0.0485  max mem: 200
Epoch: [49] Total time: 0:00:00 (0.0781 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4520 ARI = 0.2785 F = 0.3293 ACC = 0.4433
Epoch: [99]  [0/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2245  data: 0.1968  max mem: 200
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0719  data: 0.0493  max mem: 200
Epoch: [99] Total time: 0:00:00 (0.0824 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4507 ARI = 0.2844 F = 0.3340 ACC = 0.4319
Traceback (most recent call last):
  File "/root/2024-AAAI-DIVIDE/main_train.py", line 203, in <module>
    main(args)
  File "/root/2024-AAAI-DIVIDE/main_train.py", line 161, in main
    train_state = train_one_time(args, state_logger)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2024-AAAI-DIVIDE/main_train.py", line 132, in train_one_time
    train_state = train_one_epoch(
                  ^^^^^^^^^^^^^^^^
  File "/root/2024-AAAI-DIVIDE/engine_train.py", line 40, in train_one_epoch
    loss = model(samples, mmt, epoch < args.start_rectify_epoch)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2024-AAAI-DIVIDE/model.py", line 35, in forward
    mp = [self.kernel_affinity(z_t[i]) for i in range(self.n_views)]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/2024-AAAI-DIVIDE/model.py", line 55, in kernel_affinity
    model = LINE(G, embedding_size=1024, order='second')  # 初始化 LINE 模型，选择‘second’阶关系
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/2024-AAAI-DIVIDE/ge/models/line.py", line 75, in __init__
    self._gen_sampling_table()
  File "/root/2024-AAAI-DIVIDE/ge/models/line.py", line 110, in _gen_sampling_table
    norm_prob = [float(math.pow(node_degree[j], power)) / total_sum for j in range(num_nodes)]
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~
ZeroDivisionError: float division by zero
root@autodl-container-04e2498428-551163cf:~/2024-AAAI-DIVIDE# 
```
