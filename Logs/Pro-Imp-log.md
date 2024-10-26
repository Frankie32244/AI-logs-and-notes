```linux
root@autodl-container-7c5d4696fb-c54fea2a:~# history 
    1  history 
root@autodl-container-7c5d4696fb-c54fea2a:~# 
root@autodl-container-7c5d4696fb-c54fea2a:~# 
root@autodl-container-7c5d4696fb-c54fea2a:~# 
root@autodl-container-7c5d4696fb-c54fea2a:~# cd ..
root@autodl-container-7c5d4696fb-c54fea2a:/# ls
bin  boot  cuda-keyring_1.0-1_all.deb  dev  etc  home  init  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@autodl-container-7c5d4696fb-c54fea2a:/# cd var
root@autodl-container-7c5d4696fb-c54fea2a:/var# ls
backups  cache  lib  local  lock  log  mail  opt  run  spool  tmp
root@autodl-container-7c5d4696fb-c54fea2a:/var# cd log 
root@autodl-container-7c5d4696fb-c54fea2a:/var/log# ls
alternatives.log  apt  bootstrap.log  btmp  dpkg.log  faillog  fontconfig.log  journal  lastlog  private  wtmp
root@autodl-container-7c5d4696fb-c54fea2a:/var/log# cd ../..
root@autodl-container-7c5d4696fb-c54fea2a:/# ls
bin  boot  cuda-keyring_1.0-1_all.deb  dev  etc  home  init  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@autodl-container-7c5d4696fb-c54fea2a:/# cd home
root@autodl-container-7c5d4696fb-c54fea2a:/home# ls
root@autodl-container-7c5d4696fb-c54fea2a:/home# cd ..
root@autodl-container-7c5d4696fb-c54fea2a:/# cd ~
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
Pro-Imp  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# cd Pro
bash: cd: Pro: No such file or directory
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
Pro-Imp  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# cd Pro-Imp/
root@autodl-container-7c5d4696fb-c54fea2a:~/Pro-Imp# ls
2023-IJCAI-ProImp-main  2023-IJCAI-ProImp-main.zip
root@autodl-container-7c5d4696fb-c54fea2a:~/Pro-Imp# cd 2023-IJCAI-ProImp-main
root@autodl-container-7c5d4696fb-c54fea2a:~/Pro-Imp/2023-IJCAI-ProImp-main# ls
LICENSE  README.md  __pycache__  configure.py  data  datasets.py  evaluation.py  figs  get_mask.py  model.py  run.py  util.py
root@autodl-container-7c5d4696fb-c54fea2a:~/Pro-Imp/2023-IJCAI-ProImp-main# python run.py --dataset 0 --devices 0 --print_num 50 --test_time 1
2024-10-26 18:22:53 - root - INFO: - Dataset:Scene_15
2024-10-26 18:22:53 - root - INFO: - Autoencoder={
2024-10-26 18:22:53 - root - INFO: -           arch1 = [20, 1024, 1024, 1024, 256]
2024-10-26 18:22:53 - root - INFO: -           arch2 = [59, 1024, 1024, 1024, 256]
2024-10-26 18:22:53 - root - INFO: -           activations1 = relu
2024-10-26 18:22:53 - root - INFO: -           activations2 = relu
2024-10-26 18:22:53 - root - INFO: -           batchnorm = True
2024-10-26 18:22:53 - root - INFO: - training={
2024-10-26 18:22:53 - root - INFO: -           missing_rate = 0.5
2024-10-26 18:22:53 - root - INFO: -           seed = 0
2024-10-26 18:22:53 - root - INFO: -           batch_size = 1024
2024-10-26 18:22:53 - root - INFO: -           epoch = 150
2024-10-26 18:22:53 - root - INFO: -           lr = 0.001
2024-10-26 18:22:53 - root - INFO: -           num = 15
2024-10-26 18:22:53 - root - INFO: -           dim = 256
2024-10-26 18:22:53 - root - INFO: -           pretrain_epoch = 50
2024-10-26 18:22:53 - root - INFO: - print_num = 50
2024-10-26 18:22:53 - root - INFO: - dataset = Scene_15
2024-10-26 18:22:53 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=20, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Dropout(p=0.2, inplace=False)
    (4): Linear(in_features=1024, out_features=1024, bias=True)
    (5): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (6): ReLU()
    (7): Dropout(p=0.2, inplace=False)
    (8): Linear(in_features=1024, out_features=1024, bias=True)
    (9): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (10): ReLU()
    (11): Linear(in_features=1024, out_features=256, bias=True)
  )
)
2024-10-26 18:22:53 - root - INFO: - dual_attention(
  (norm1): LayerNorm((256,), eps=1e-05, elementwise_affine=True)
  (norm2): LayerNorm((256,), eps=1e-05, elementwise_affine=True)
  (soft): Softmax(dim=-1)
  (ins): InstanceLoss(
    (criterion): CrossEntropyLoss()
  )
  (pro): PrototypeLoss(
    (criterion): CrossEntropyLoss()
  )
  (cross_img): cross_attn(
    (q_proj): Linear(in_features=256, out_features=256, bias=True)
    (k_proj): Linear(in_features=256, out_features=256, bias=True)
    (v_proj1): Linear(in_features=256, out_features=256, bias=True)
    (v_proj2): Linear(in_features=256, out_features=256, bias=True)
    (norm1): LayerNorm((256,), eps=1e-05, elementwise_affine=True)
    (norm2): LayerNorm((256,), eps=1e-05, elementwise_affine=True)
    (proj_z): Identity()
    (proj_c): Identity()
  )
  (cross_txt): cross_attn(
    (q_proj): Linear(in_features=256, out_features=256, bias=True)
    (k_proj): Linear(in_features=256, out_features=256, bias=True)
    (v_proj1): Linear(in_features=256, out_features=256, bias=True)
    (v_proj2): Linear(in_features=256, out_features=256, bias=True)
    (norm1): LayerNorm((256,), eps=1e-05, elementwise_affine=True)
    (norm2): LayerNorm((256,), eps=1e-05, elementwise_affine=True)
    (proj_z): Identity()
    (proj_c): Identity()
  )
  (proj_c): Identity()
  (proj_z): Linear(in_features=256, out_features=256, bias=True)
  (prototype_token_1): Linear(in_features=256, out_features=15, bias=False)
  (prototype_token_2): Linear(in_features=256, out_features=15, bias=False)
  (projector_rep): Sequential(
    (0): Linear(in_features=256, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU(inplace=True)
    (3): Linear(in_features=256, out_features=256, bias=True)
  )
  (projector_prototype): Identity()
  (projector1): Sequential(
    (0): Linear(in_features=256, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU(inplace=True)
    (3): Linear(in_features=256, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=256, bias=True)
  )
  (projector2): Sequential(
    (0): Linear(in_features=256, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU(inplace=True)
    (3): Linear(in_features=256, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=256, bias=True)
  )
)
2024-10-26 18:22:53 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.001
    maximize: False
    weight_decay: 0
)
2024-10-26 18:23:08 - root - INFO: - Epoch : 50/150 ===> Learing Rate = 0.0010===> Ins loss = 1.6542e+01 ===> Clu loss = 0.0000e+00 ===> Loss = 1.6542e+01
-0.016242959
2024-10-26 18:23:11 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4147, 'NMI': 0.4195, 'ARI': 0.2346, 'accuracy': 0.3795, 'precision': 0.3687, 'recall': 0.3774, 'f_measure': 0.3691}}
2024-10-26 18:23:23 - root - INFO: - Epoch : 100/150 ===> Learing Rate = 0.0010===> Ins loss = 1.6305e+01 ===> Clu loss = 8.9628e+00 ===> Loss = 2.5268e+01
-0.0042240242
2024-10-26 18:23:25 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4346, 'NMI': 0.4393, 'ARI': 0.2565, 'accuracy': 0.4127, 'precision': 0.4063, 'recall': 0.4127, 'f_measure': 0.3998}}
2024-10-26 18:23:37 - root - INFO: - Epoch : 150/150 ===> Learing Rate = 0.0010===> Ins loss = 1.6110e+01 ===> Clu loss = 8.9503e+00 ===> Loss = 2.5060e+01
-0.0013364896
2024-10-26 18:23:39 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4204, 'NMI': 0.4251, 'ARI': 0.2414, 'accuracy': 0.3969, 'precision': 0.3908, 'recall': 0.3972, 'f_measure': 0.3853}}
2024-10-26 18:23:39 - root - INFO: - --------------------Training over--------------------
2024-10-26 18:23:39 - root - INFO: - ACC:[0.3969]
2024-10-26 18:23:39 - root - INFO: - NMI:[0.4251]
2024-10-26 18:23:39 - root - INFO: - ARI:[0.2414]
2024-10-26 18:23:39 - root - INFO: -  ACC 39.69 std 0.00 NMI 42.51 std 0.00 ARI 24.14 std 0.00
```
