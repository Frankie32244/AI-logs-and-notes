### DIVIDE 现在存在的几个问题
* 给的源码当中缺两个yaml文件，缺LandUse21 和 Reuters  两个yaml 文件，
* 论文只有一个数据集Scene.mat, 其它三个分别是Caltech101,LandUse21,Reuters 都要自己去下载并且提取特征 
 
### dataset : Scene15   missing_rate = 0   

！！！ 跑了5轮，随机种子分别设置成了0,1,2,3,4

```linux
root@autodl-container-534b4e910e-a60bb39b:~/2024-AAAI-DIVIDE# python main_train.py --config_file=config/Scene15.yaml

>> Start training 0-th initial, seed: 0,
Epoch: [49]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2876  data: 0.2629  max mem: 200
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0805  data: 0.0658  max mem: 200
Epoch: [49] Total time: 0:00:00 (0.0892 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4511 ARI = 0.2815 F = 0.3318 ACC = 0.4533
Epoch: [99]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2870  data: 0.2604  max mem: 200
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0810  data: 0.0651  max mem: 200
Epoch: [99] Total time: 0:00:00 (0.0901 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4598 ARI = 0.2874 F = 0.3368 ACC = 0.4526
Epoch: [149]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3034  data: 0.2713  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0868  data: 0.0679  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0955 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4754 ARI = 0.3006 F = 0.3499 ACC = 0.4388
Epoch: [199]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3272  data: 0.2946  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0931  data: 0.0737  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.1023 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4549 ARI = 0.2785 F = 0.3291 ACC = 0.4326

enable cudnn.deterministic, seed fixed: 1

>> Start training 1-th initial, seed: 1,
Epoch: [49]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.3424  data: 0.3127  max mem: 204
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0946  data: 0.0782  max mem: 204
Epoch: [49] Total time: 0:00:00 (0.1037 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4654 ARI = 0.2936 F = 0.3428 ACC = 0.4673
Epoch: [99]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.2901  data: 0.2652  max mem: 204
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0813  data: 0.0663  max mem: 204
Epoch: [99] Total time: 0:00:00 (0.0902 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4540 ARI = 0.2858 F = 0.3353 ACC = 0.4439
Epoch: [149]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3118  data: 0.2715  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0898  data: 0.0680  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0982 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4807 ARI = 0.3150 F = 0.3632 ACC = 0.4919
Epoch: [199]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3116  data: 0.2836  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0884  data: 0.0709  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.0973 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4710 ARI = 0.2940 F = 0.3450 ACC = 0.4685

enable cudnn.deterministic, seed fixed: 2

>> Start training 2-th initial, seed: 2,
Epoch: [49]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2974  data: 0.2719  max mem: 204
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0853  data: 0.0680  max mem: 204
Epoch: [49] Total time: 0:00:00 (0.0945 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4635 ARI = 0.2981 F = 0.3472 ACC = 0.4747
Epoch: [99]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3106  data: 0.2842  max mem: 204
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0872  data: 0.0711  max mem: 204
Epoch: [99] Total time: 0:00:00 (0.0959 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4595 ARI = 0.2887 F = 0.3383 ACC = 0.4758
Epoch: [149]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3078  data: 0.2811  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0874  data: 0.0703  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0961 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4652 ARI = 0.2996 F = 0.3483 ACC = 0.4401
Epoch: [199]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3154  data: 0.2845  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0917  data: 0.0712  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.1004 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4660 ARI = 0.2805 F = 0.3319 ACC = 0.4502

enable cudnn.deterministic, seed fixed: 3

>> Start training 3-th initial, seed: 3,
Epoch: [49]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.3049  data: 0.2756  max mem: 204
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0870  data: 0.0690  max mem: 204
Epoch: [49] Total time: 0:00:00 (0.0954 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4366 ARI = 0.2541 F = 0.3085 ACC = 0.3960
Epoch: [99]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3111  data: 0.2869  max mem: 204
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0889  data: 0.0718  max mem: 204
Epoch: [99] Total time: 0:00:00 (0.0977 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4689 ARI = 0.3005 F = 0.3488 ACC = 0.4778
Epoch: [149]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3200  data: 0.2913  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0911  data: 0.0729  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.0998 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4797 ARI = 0.3035 F = 0.3529 ACC = 0.4649
Epoch: [199]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3150  data: 0.2826  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0936  data: 0.0707  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.1021 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4915 ARI = 0.3133 F = 0.3630 ACC = 0.4954

enable cudnn.deterministic, seed fixed: 4

>> Start training 4-th initial, seed: 4,
Epoch: [49]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.2935  data: 0.2664  max mem: 204
Epoch: [49]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0102 (0.0102)  time: 0.0834  data: 0.0667  max mem: 204
Epoch: [49] Total time: 0:00:00 (0.0923 s / it)
Averaged stats: lr: 0.002000  loss: 0.0102 (0.0102)
Epoch 49 K-means: NMI = 0.4433 ARI = 0.2695 F = 0.3200 ACC = 0.4158
Epoch: [99]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3006  data: 0.2743  max mem: 204
Epoch: [99]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0851  data: 0.0686  max mem: 204
Epoch: [99] Total time: 0:00:00 (0.0941 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 99 K-means: NMI = 0.4710 ARI = 0.3123 F = 0.3602 ACC = 0.4907
Epoch: [149]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3338  data: 0.3020  max mem: 204
Epoch: [149]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0966  data: 0.0756  max mem: 204
Epoch: [149] Total time: 0:00:00 (0.1099 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 149 K-means: NMI = 0.4820 ARI = 0.3091 F = 0.3580 ACC = 0.4491
Epoch: [199]  [0/4]  eta: 0:00:01  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.3234  data: 0.2922  max mem: 204
Epoch: [199]  [3/4]  eta: 0:00:00  lr: 0.002000  loss: 0.0101 (0.0101)  time: 0.0926  data: 0.0731  max mem: 204
Epoch: [199] Total time: 0:00:00 (0.1014 s / it)
Averaged stats: lr: 0.002000  loss: 0.0101 (0.0101)
Epoch 199 K-means: NMI = 0.4904 ARI = 0.3238 F = 0.3714 ACC = 0.5012

Training time 0:06:41

Average K-means Result: ACC = 46.96(2.61) NMI = 47.48(1.42) ARI = 29.80(1.79)
```

### dataset : Caltech101   missing_rate = 0 
！！！！！！ 需要这个数据集2view-caltech101-8677sample.mat，而不是Caltech101
```linux
root@autodl-container-534b4e910e-a60bb39b:~/2024-AAAI-DIVIDE# python main_train.py --config_file=config/Caltech101.yaml

enable cudnn.deterministic, seed fixed: 1
job dir: /root/2024-AAAI-DIVIDE
Batch size: 1024
Start time: 2024-11-18 14:59
Train parameters: Namespace(config_file='config/Caltech101.yaml',
encoder_dim=[[4096,
1024,
1024,
1024,
128],
[4096,
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
n_classes=101,
batch_size=1024,
epochs=200,
warmup_epochs=20,
data_norm='standard',
train_time=5,
weight_decay=0,
lr=0.002,
dataset='Caltech101',
missing_rate=0.0,
data_path='data/multiview',
device='cuda',
output_dir='DIVIDE/Caltech101_msrt_0.0_tau_0.5_bs_1024_blr_0.0005',
print_freq=50,
start_epoch=0,
num_workers=8,
seed=1,
pin_mem=True,
blr=0.0005,
min_blr=0.0005,
train_id=0,
n_sample=8677)

>> Start training 0-th initial, seed: 1,
Epoch: [49]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.5676  data: 0.5397  max mem: 358
Epoch: [49]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0858  data: 0.0675  max mem: 358
Epoch: [49] Total time: 0:00:00 (0.0925 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 49 K-means: NMI = 0.7894 ARI = 0.3827 F = 0.4338 ACC = 0.5527
Epoch: [99]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.5126  data: 0.4847  max mem: 358
Epoch: [99]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0771  data: 0.0606  max mem: 358
Epoch: [99] Total time: 0:00:00 (0.0827 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 99 K-means: NMI = 0.7985 ARI = 0.3883 F = 0.4424 ACC = 0.5540
Epoch: [149]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.5117  data: 0.4850  max mem: 362
Epoch: [149]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0794  data: 0.0607  max mem: 362
Epoch: [149] Total time: 0:00:00 (0.0848 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 149 K-means: NMI = 0.8249 ARI = 0.4833 F = 0.5217 ACC = 0.6385
Epoch: [199]  [0/8]  eta: 0:00:03  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.4405  data: 0.4154  max mem: 362
Epoch: [199]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0771  data: 0.0584  max mem: 362
Epoch: [199] Total time: 0:00:00 (0.0835 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 199 K-means: NMI = 0.8283 ARI = 0.4998 F = 0.5335 ACC = 0.6286

enable cudnn.deterministic, seed fixed: 2

>> Start training 1-th initial, seed: 2,
Epoch: [49]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.5086  data: 0.4797  max mem: 362
Epoch: [49]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0773  data: 0.0600  max mem: 362
Epoch: [49] Total time: 0:00:00 (0.0832 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 49 K-means: NMI = 0.7923 ARI = 0.3720 F = 0.4262 ACC = 0.5447
Epoch: [99]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.5339  data: 0.5119  max mem: 362
Epoch: [99]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0793  data: 0.0640  max mem: 362
Epoch: [99] Total time: 0:00:00 (0.0849 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 99 K-means: NMI = 0.8040 ARI = 0.3833 F = 0.4380 ACC = 0.5578
Epoch: [149]  [0/8]  eta: 0:00:03  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.4554  data: 0.4286  max mem: 362
Epoch: [149]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0803  data: 0.0601  max mem: 362
Epoch: [149] Total time: 0:00:00 (0.0863 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 149 K-means: NMI = 0.8288 ARI = 0.4964 F = 0.5354 ACC = 0.6203
Epoch: [199]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.5450  data: 0.5173  max mem: 362
Epoch: [199]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0833  data: 0.0647  max mem: 362
Epoch: [199] Total time: 0:00:00 (0.0894 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 199 K-means: NMI = 0.8310 ARI = 0.5122 F = 0.5453 ACC = 0.6160

enable cudnn.deterministic, seed fixed: 3

>> Start training 2-th initial, seed: 3,
Epoch: [49]  [0/8]  eta: 0:00:03  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.4491  data: 0.4255  max mem: 362
Epoch: [49]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0764  data: 0.0574  max mem: 362
Epoch: [49] Total time: 0:00:00 (0.0820 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 49 K-means: NMI = 0.7866 ARI = 0.3800 F = 0.4311 ACC = 0.5383
Epoch: [99]  [0/8]  eta: 0:00:03  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.4470  data: 0.4223  max mem: 362
Epoch: [99]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0747  data: 0.0573  max mem: 362
Epoch: [99] Total time: 0:00:00 (0.0802 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 99 K-means: NMI = 0.7872 ARI = 0.3579 F = 0.4130 ACC = 0.5269
Epoch: [149]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.5297  data: 0.5067  max mem: 362
Epoch: [149]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0826  data: 0.0634  max mem: 362
Epoch: [149] Total time: 0:00:00 (0.0884 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 149 K-means: NMI = 0.8189 ARI = 0.4704 F = 0.5105 ACC = 0.6094
Epoch: [199]  [0/8]  eta: 0:00:03  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.4670  data: 0.4375  max mem: 362
Epoch: [199]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0797  data: 0.0604  max mem: 362
Epoch: [199] Total time: 0:00:00 (0.0855 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 199 K-means: NMI = 0.8231 ARI = 0.4949 F = 0.5282 ACC = 0.6095

enable cudnn.deterministic, seed fixed: 4

>> Start training 3-th initial, seed: 4,
Epoch: [49]  [0/8]  eta: 0:00:03  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.4748  data: 0.4577  max mem: 362
Epoch: [49]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0770  data: 0.0612  max mem: 362
Epoch: [49] Total time: 0:00:00 (0.0828 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 49 K-means: NMI = 0.7816 ARI = 0.3553 F = 0.4091 ACC = 0.5338
Epoch: [99]  [0/8]  eta: 0:00:03  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.4434  data: 0.4194  max mem: 362
Epoch: [99]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0763  data: 0.0584  max mem: 362
Epoch: [99] Total time: 0:00:00 (0.0824 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 99 K-means: NMI = 0.7900 ARI = 0.3600 F = 0.4135 ACC = 0.5358
Epoch: [149]  [0/8]  eta: 0:00:05  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.6722  data: 0.6490  max mem: 362
Epoch: [149]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.1078  data: 0.0881  max mem: 362
Epoch: [149] Total time: 0:00:00 (0.1152 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 149 K-means: NMI = 0.8193 ARI = 0.4667 F = 0.5052 ACC = 0.6135
Epoch: [199]  [0/8]  eta: 0:00:05  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.7202  data: 0.6957  max mem: 362
Epoch: [199]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.1052  data: 0.0870  max mem: 362
Epoch: [199] Total time: 0:00:00 (0.1129 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 199 K-means: NMI = 0.8270 ARI = 0.4912 F = 0.5249 ACC = 0.6211

enable cudnn.deterministic, seed fixed: 5

>> Start training 4-th initial, seed: 5,
Epoch: [49]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.5312  data: 0.5013  max mem: 362
Epoch: [49]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0800  data: 0.0627  max mem: 362
Epoch: [49] Total time: 0:00:00 (0.0872 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 49 K-means: NMI = 0.7893 ARI = 0.3848 F = 0.4378 ACC = 0.5490
Epoch: [99]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.5287  data: 0.5032  max mem: 362
Epoch: [99]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0855  data: 0.0680  max mem: 362
Epoch: [99] Total time: 0:00:00 (0.0920 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 99 K-means: NMI = 0.7905 ARI = 0.3578 F = 0.4097 ACC = 0.5435
Epoch: [149]  [0/8]  eta: 0:00:03  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.4492  data: 0.4260  max mem: 362
Epoch: [149]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.0792  data: 0.0603  max mem: 362
Epoch: [149] Total time: 0:00:00 (0.0852 s / it)
Averaged stats: lr: 0.002000  loss: 0.0099 (0.0099)
Epoch 149 K-means: NMI = 0.8252 ARI = 0.4844 F = 0.5223 ACC = 0.6289
Epoch: [199]  [0/8]  eta: 0:00:04  lr: 0.002000  loss: 0.0099 (0.0099)  time: 0.5092  data: 0.4853  max mem: 362
Epoch: [199]  [7/8]  eta: 0:00:00  lr: 0.002000  loss: 0.0098 (0.0098)  time: 0.0808  data: 0.0620  max mem: 362
Epoch: [199] Total time: 0:00:00 (0.0863 s / it)
Averaged stats: lr: 0.002000  loss: 0.0098 (0.0098)
Epoch 199 K-means: NMI = 0.8305 ARI = 0.5101 F = 0.5433 ACC = 0.6302

Training time 0:12:46

Average K-means Result: ACC = 62.11(0.77) NMI = 82.80(0.28) ARI = 50.16(0.83)
```
