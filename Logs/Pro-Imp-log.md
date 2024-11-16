NoisyMNIST
Reuters
Cub
MNIST-USPS

以上这几个数据集在configure.py 里面没有配置跑不了一点，除非自己来配置。

### dataset : Scene_15  missing_rate = 0.5
```linux
root@autodl-container-7c5d4696fb-c54fea2a:~/Pro-Imp/2023-IJCAI-ProImp-main# python run.py --dataset 0 --devices 0 --print_num 50 --test_time 1
2024-10-26 18:22:53 - root - INFO: - Dataset:Scene_15
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

### dataset : Scene_15  missing_rate = 0
```linux
2024-11-16 15:32:17 - root - INFO: - Epoch : 50/150 ===> Learing Rate = 0.0010===> Ins loss = 2.8840e+01 ===> Clu loss = 0.0000e+00 ===> Loss = 2.8840e+01
0.0035320676
2024-11-16 15:32:19 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4433, 'NMI': 0.4479, 'ARI': 0.2729, 'accuracy': 0.4499, 'precision': 0.4359, 'recall': 0.4508, 'f_measure': 0.4359}}
2024-11-16 15:32:45 - root - INFO: - Epoch : 100/150 ===> Learing Rate = 0.0010===> Ins loss = 2.8466e+01 ===> Clu loss = 1.4931e+01 ===> Loss = 4.3397e+01
0.012406256
2024-11-16 15:32:47 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4451, 'NMI': 0.4497, 'ARI': 0.2678, 'accuracy': 0.4308, 'precision': 0.433, 'recall': 0.4344, 'f_measure': 0.4262}}
2024-11-16 15:33:13 - root - INFO: - Epoch : 150/150 ===> Learing Rate = 0.0010===> Ins loss = 2.8210e+01 ===> Clu loss = 1.4920e+01 ===> Loss = 4.3129e+01
0.013962765
2024-11-16 15:33:15 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4502, 'NMI': 0.4547, 'ARI': 0.2741, 'accuracy': 0.4453, 'precision': 0.4426, 'recall': 0.443, 'f_measure': 0.4396}}
2024-11-16 15:33:15 - root - INFO: - --------------------Training over--------------------
2024-11-16 15:33:15 - root - INFO: - ACC:[0.4453]
2024-11-16 15:33:15 - root - INFO: - NMI:[0.4547]
2024-11-16 15:33:15 - root - INFO: - ARI:[0.2741]
2024-11-16 15:33:15 - root - INFO: -  ACC 44.53 std 0.00 NMI 45.47 std 0.00 ARI 27.41 std 0.00
```


```linux  Dataset:cub_googlenet  missing_rate = 0
root@autodl-container-534b4e910e-a60bb39b:~/Pro-Imp/2023-IJCAI-ProImp-main# python run.py --dataset 4 --devices 0 --print_num 50 --test_time 1
2024-11-16 15:36:44 - root - INFO: - Dataset:cub_googlenet
2024-11-16 15:36:48 - root - INFO: - Epoch : 50/150 ===> Learing Rate = 0.0010===> Ins loss = 5.6179e+00 ===> Clu loss = 0.0000e+00 ===> Loss = 5.6179e+00
0.25920653
2024-11-16 15:36:48 - root - INFO: - view_concat {'kmeans': {'AMI': 0.7336, 'NMI': 0.742, 'ARI': 0.5994, 'accuracy': 0.6883, 'precision': 0.6746, 'recall': 0.6883, 'f_measure': 0.6602}}
2024-11-16 15:36:51 - root - INFO: - Epoch : 100/150 ===> Learing Rate = 0.0010===> Ins loss = 5.4923e+00 ===> Clu loss = 2.5564e+00 ===> Loss = 8.0487e+00
0.35264543
2024-11-16 15:36:51 - root - INFO: - view_concat {'kmeans': {'AMI': 0.7469, 'NMI': 0.7548, 'ARI': 0.6432, 'accuracy': 0.74, 'precision': 0.7111, 'recall': 0.74, 'f_measure': 0.7169}}
2024-11-16 15:36:54 - root - INFO: - Epoch : 150/150 ===> Learing Rate = 0.0010===> Ins loss = 5.4308e+00 ===> Clu loss = 2.5569e+00 ===> Loss = 7.9877e+00
0.36583042
2024-11-16 15:36:54 - root - INFO: - view_concat {'kmeans': {'AMI': 0.7447, 'NMI': 0.7525, 'ARI': 0.6614, 'accuracy': 0.8183, 'precision': 0.8222, 'recall': 0.8183, 'f_measure': 0.816}}
2024-11-16 15:36:54 - root - INFO: - --------------------Training over--------------------
2024-11-16 15:36:54 - root - INFO: - ACC:[0.8183]
2024-11-16 15:36:54 - root - INFO: - NMI:[0.7525]
2024-11-16 15:36:54 - root - INFO: - ARI:[0.6614]
2024-11-16 15:36:54 - root - INFO: -  ACC 81.83 std 0.00 NMI 75.25 std 0.00 ARI 66.14 std 0.00
```
