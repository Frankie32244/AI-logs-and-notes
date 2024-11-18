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
