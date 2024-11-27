## 1. 2021-CVPR-Completer(Running logs)
[reference](https://github.com/XLearning-SCU/2021-CVPR-Completer)

time:2023-11-1、2024-11-15

跑完的数据集: Caltech101-20,Scene_15,LandUse_21,Noisy Minist和原论文效果差不多。( complete:missing_rate = 0  incomplete missing_rate = 0.5 ) 

### dataset: Caltech101-20  missing_rate = 0.5   test_time = 5
```linux
root@autodl-container-e6d91195fa-0bc38630:~/2021-CVPR-Completer# python run.py --dataset 0 --devices 0 --print_num 100 --test_time 5
2023-11-01 17:06:09 - root - INFO: - Dataset:Caltech101-20
2023-11-01 17:06:09 - root - INFO: - Prediction={
2023-11-01 17:06:09 - root - INFO: -           arch1 = [128, 256, 128]
2023-11-01 17:06:09 - root - INFO: -           arch2 = [128, 256, 128]
2023-11-01 17:06:09 - root - INFO: - Autoencoder={
2023-11-01 17:06:09 - root - INFO: -           arch1 = [1984, 1024, 1024, 1024, 128]
2023-11-01 17:06:09 - root - INFO: -           arch2 = [512, 1024, 1024, 1024, 128]
2023-11-01 17:06:09 - root - INFO: -           activations1 = relu
2023-11-01 17:06:09 - root - INFO: -           activations2 = relu
2023-11-01 17:06:09 - root - INFO: -           batchnorm = True
2023-11-01 17:06:09 - root - INFO: - training={
2023-11-01 17:06:09 - root - INFO: -           seed = 4
2023-11-01 17:06:09 - root - INFO: -           missing_rate = 0.5
2023-11-01 17:06:09 - root - INFO: -           start_dual_prediction = 100
2023-11-01 17:06:09 - root - INFO: -           batch_size = 256
2023-11-01 17:06:09 - root - INFO: -           epoch = 500
2023-11-01 17:06:09 - root - INFO: -           lr = 0.0001
2023-11-01 17:06:09 - root - INFO: -           alpha = 9
2023-11-01 17:06:09 - root - INFO: -           lambda1 = 0.1
2023-11-01 17:06:09 - root - INFO: -           lambda2 = 0.1
2023-11-01 17:06:09 - root - INFO: - print_num = 100
2023-11-01 17:06:09 - root - INFO: - dataset = Caltech101-20
2023-11-01 17:09:40 - root - INFO: - --------------------Training over--------------------
2023-11-01 17:09:40 - root - INFO: - ACC:[0.7649, 0.6412, 0.7607, 0.7628, 0.6899]
2023-11-01 17:09:40 - root - INFO: - NMI:[0.7073, 0.6698, 0.7079, 0.7248, 0.6785]
2023-11-01 17:09:40 - root - INFO: - ARI:[0.8785, 0.6619, 0.8773, 0.8811, 0.8384]
2023-11-01 17:09:40 - root - INFO: -  ACC 72.39 std 5.01 NMI 69.77 std 2.04 ARI 82.74 std 8.43
root@autodl-container-e6d91195fa-0bc38630:~/2021-CVPR-Completer# 
```

### dataset: Caltech101-20  missing_rate = 0   test_time = 1

```linux
root@autodl-container-534b4e910e-a60bb39b:~/2021-CVPR-Completer# python run.py --dataset 0 --test_time 1
2024-11-15 10:28:16 - root - INFO: - Dataset:Caltech101-20
2024-11-15 10:28:16 - root - INFO: - Prediction={
2024-11-15 10:28:16 - root - INFO: -           arch1 = [128, 256, 128]
2024-11-15 10:28:16 - root - INFO: -           arch2 = [128, 256, 128]
2024-11-15 10:28:16 - root - INFO: - Autoencoder={
2024-11-15 10:28:16 - root - INFO: -           arch1 = [1984, 1024, 1024, 1024, 128]
2024-11-15 10:28:16 - root - INFO: -           arch2 = [512, 1024, 1024, 1024, 128]
2024-11-15 10:28:16 - root - INFO: -           activations1 = relu
2024-11-15 10:28:16 - root - INFO: -           activations2 = relu
2024-11-15 10:28:16 - root - INFO: -           batchnorm = True
2024-11-15 10:28:16 - root - INFO: - training={
2024-11-15 10:28:16 - root - INFO: -           seed = 4
2024-11-15 10:28:16 - root - INFO: -           missing_rate = 0
2024-11-15 10:28:16 - root - INFO: -           start_dual_prediction = 100
2024-11-15 10:28:16 - root - INFO: -           batch_size = 256
2024-11-15 10:28:16 - root - INFO: -           epoch = 500
2024-11-15 10:28:16 - root - INFO: -           lr = 0.0001
2024-11-15 10:28:16 - root - INFO: -           alpha = 9
2024-11-15 10:28:16 - root - INFO: -           lambda1 = 0.1
2024-11-15 10:28:16 - root - INFO: -           lambda2 = 0.1
2024-11-15 10:28:16 - root - INFO: - print_num = 100
2024-11-15 10:28:16 - root - INFO: - dataset = Caltech101-20
2024-11-15 10:29:35 - root - INFO: - --------------------Training over--------------------
2024-11-15 10:29:35 - root - INFO: - ACC:[0.7121]
2024-11-15 10:29:35 - root - INFO: - NMI:[0.6514]
2024-11-15 10:29:35 - root - INFO: - ARI:[0.7843]
2024-11-15 10:29:35 - root - INFO: -  ACC 71.21 std 0.00 NMI 65.14 std 0.00 ARI 78.43 std 0.00

```




### dataset:Scene_15    missing_rate = 0.5  test_time = 5
```linux
root@autodl-container-b72911863c-065c7124:~/2021-CVPR-Completer# python run.py --dataset 1 --devices 0 --print_num 100 --test_time 5
2023-11-02 14:48:21 - root - INFO: - Dataset:Scene_15
2023-11-02 14:48:21 - root - INFO: - Prediction={
2023-11-02 14:48:21 - root - INFO: -           arch1 = [128, 256, 128]
2023-11-02 14:48:21 - root - INFO: -           arch2 = [128, 256, 128]
2023-11-02 14:48:21 - root - INFO: - Autoencoder={
2023-11-02 14:48:21 - root - INFO: -           arch1 = [20, 1024, 1024, 1024, 128]
2023-11-02 14:48:21 - root - INFO: -           arch2 = [59, 1024, 1024, 1024, 128]
2023-11-02 14:48:21 - root - INFO: -           activations1 = relu
2023-11-02 14:48:21 - root - INFO: -           activations2 = relu
2023-11-02 14:48:21 - root - INFO: -           batchnorm = True
2023-11-02 14:48:21 - root - INFO: - training={
2023-11-02 14:48:21 - root - INFO: -           missing_rate = 0.5
2023-11-02 14:48:21 - root - INFO: -           seed = 8
2023-11-02 14:48:21 - root - INFO: -           start_dual_prediction = 100
2023-11-02 14:48:21 - root - INFO: -           batch_size = 256
2023-11-02 14:48:21 - root - INFO: -           epoch = 500
2023-11-02 14:48:21 - root - INFO: -           lr = 0.0001
2023-11-02 14:48:21 - root - INFO: -           alpha = 9
2023-11-02 14:48:21 - root - INFO: -           lambda1 = 0.1
2023-11-02 14:48:21 - root - INFO: -           lambda2 = 0.1
2023-11-02 14:48:21 - root - INFO: - print_num = 100
2023-11-02 14:48:21 - root - INFO: - dataset = Scene_15
2023-11-02 14:55:50 - root - INFO: - --------------------Training over--------------------
2023-11-02 14:55:50 - root - INFO: - ACC:[0.3802, 0.404, 0.39, 0.3561, 0.3938]
2023-11-02 14:55:50 - root - INFO: - NMI:[0.4067, 0.4248, 0.4321, 0.3931, 0.415]
2023-11-02 14:55:50 - root - INFO: - ARI:[0.215, 0.2419, 0.2378, 0.1893, 0.2313]
2023-11-02 14:55:50 - root - INFO: -  ACC 38.48 std 1.63 NMI 41.43 std 1.37 ARI 22.31 std 1.92
root@autodl-container-b72911863c-065c7124:~/2021-CVPR-Completer#
```

### dataset:Scene_15    missing_rate = 0  test_time = 1
```linux
root@autodl-container-534b4e910e-a60bb39b:~/2021-CVPR-Completer# python run.py --dataset 1 --test_time 1
2024-11-15 10:32:44 - root - INFO: - Dataset:Scene_15
2024-11-15 10:32:44 - root - INFO: - Prediction={
2024-11-15 10:32:44 - root - INFO: -           arch1 = [128, 256, 128]
2024-11-15 10:32:44 - root - INFO: -           arch2 = [128, 256, 128]
2024-11-15 10:32:44 - root - INFO: - Autoencoder={
2024-11-15 10:32:44 - root - INFO: -           arch1 = [20, 1024, 1024, 1024, 128]
2024-11-15 10:32:44 - root - INFO: -           arch2 = [59, 1024, 1024, 1024, 128]
2024-11-15 10:32:44 - root - INFO: -           activations1 = relu
2024-11-15 10:32:44 - root - INFO: -           activations2 = relu
2024-11-15 10:32:44 - root - INFO: -           batchnorm = True
2024-11-15 10:32:44 - root - INFO: - training={
2024-11-15 10:32:44 - root - INFO: -           missing_rate = 0
2024-11-15 10:32:44 - root - INFO: -           seed = 8
2024-11-15 10:32:44 - root - INFO: -           start_dual_prediction = 100
2024-11-15 10:32:44 - root - INFO: -           batch_size = 256
2024-11-15 10:32:44 - root - INFO: -           epoch = 500
2024-11-15 10:32:44 - root - INFO: -           lr = 0.0001
2024-11-15 10:32:44 - root - INFO: -           alpha = 9
2024-11-15 10:32:44 - root - INFO: -           lambda1 = 0.1
2024-11-15 10:32:44 - root - INFO: -           lambda2 = 0.1
2024-11-15 10:32:44 - root - INFO: - print_num = 100
2024-11-15 10:32:44 - root - INFO: - dataset = Scene_15
2024-11-15 10:34:58 - root - INFO: - --------------------Training over--------------------
2024-11-15 10:34:58 - root - INFO: - ACC:[0.3984]
2024-11-15 10:34:58 - root - INFO: - NMI:[0.4303]
2024-11-15 10:34:58 - root - INFO: - ARI:[0.2269]
2024-11-15 10:34:58 - root - INFO: -  ACC 39.84 std 0.00 NMI 43.03 std 0.00 ARI 22.69 std 0.00

```


### dataset:LandUse_21   missing_rate = 0.5  test_time = 1
```linux
root@autodl-container-534b4e910e-a60bb39b:~/2021-CVPR-Completer# python run.py --dataset 2 --test_time 1
2024-11-15 11:14:42 - root - INFO: - Dataset:LandUse_21
2024-11-15 11:14:42 - root - INFO: - Prediction={
2024-11-15 11:14:42 - root - INFO: -           arch1 = [128, 256, 128]
2024-11-15 11:14:42 - root - INFO: -           arch2 = [128, 256, 128]
2024-11-15 11:14:42 - root - INFO: - Autoencoder={
2024-11-15 11:14:42 - root - INFO: -           arch1 = [59, 1024, 1024, 1024, 64]
2024-11-15 11:14:42 - root - INFO: -           arch2 = [40, 1024, 1024, 1024, 64]
2024-11-15 11:14:42 - root - INFO: -           activations1 = relu
2024-11-15 11:14:42 - root - INFO: -           activations2 = relu
2024-11-15 11:14:42 - root - INFO: -           batchnorm = True
2024-11-15 11:14:42 - root - INFO: - training={
2024-11-15 11:14:42 - root - INFO: -           missing_rate = 0.5
2024-11-15 11:14:42 - root - INFO: -           seed = 3
2024-11-15 11:14:42 - root - INFO: -           start_dual_prediction = 100
2024-11-15 11:14:42 - root - INFO: -           epoch = 500
2024-11-15 11:14:42 - root - INFO: -           batch_size = 256
2024-11-15 11:14:42 - root - INFO: -           lr = 0.0001
2024-11-15 11:14:42 - root - INFO: -           alpha = 9
2024-11-15 11:14:42 - root - INFO: -           lambda1 = 0.1
2024-11-15 11:14:42 - root - INFO: -           lambda2 = 0.1
2024-11-15 11:14:42 - root - INFO: - print_num = 100
2024-11-15 11:14:42 - root - INFO: - dataset = LandUse_21
2024-11-15 11:15:23 - root - INFO: - --------------------Training over--------------------
2024-11-15 11:15:23 - root - INFO: - ACC:[0.2048]
2024-11-15 11:15:23 - root - INFO: - NMI:[0.2386]
2024-11-15 11:15:23 - root - INFO: - ARI:[0.0819]
2024-11-15 11:15:23 - root - INFO: -  ACC 20.48 std 0.00 NMI 23.86 std 0.00 ARI 8.19 std 0.00
```


### dataset:LandUse_21   missing_rate = 0  test_time = 5
```linux 
root@autodl-container-b72911863c-065c7124:~/2021-CVPR-Completer# python run.py --dataset 2 --devices 0 --print_num 100 --test_time 5
2023-11-02 14:56:29 - root - INFO: - Dataset:LandUse_21
2023-11-02 14:56:29 - root - INFO: - Prediction={
2023-11-02 14:56:29 - root - INFO: -           arch1 = [128, 256, 128]
2023-11-02 14:56:29 - root - INFO: -           arch2 = [128, 256, 128]
2023-11-02 14:56:29 - root - INFO: - Autoencoder={
2023-11-02 14:56:29 - root - INFO: -           arch1 = [59, 1024, 1024, 1024, 64]
2023-11-02 14:56:29 - root - INFO: -           arch2 = [40, 1024, 1024, 1024, 64]
2023-11-02 14:56:29 - root - INFO: -           activations1 = relu
2023-11-02 14:56:29 - root - INFO: -           activations2 = relu
2023-11-02 14:56:29 - root - INFO: -           batchnorm = True
2023-11-02 14:56:29 - root - INFO: - training={
2023-11-02 14:56:29 - root - INFO: -           missing_rate = 0
2023-11-02 14:56:29 - root - INFO: -           seed = 3
2023-11-02 14:56:29 - root - INFO: -           start_dual_prediction = 100
2023-11-02 14:56:29 - root - INFO: -           epoch = 500
2023-11-02 14:56:29 - root - INFO: -           batch_size = 256
2023-11-02 14:56:29 - root - INFO: -           lr = 0.0001
2023-11-02 14:56:29 - root - INFO: -           alpha = 9
2023-11-02 14:56:29 - root - INFO: -           lambda1 = 0.1
2023-11-02 14:56:29 - root - INFO: -           lambda2 = 0.1
2023-11-02 14:56:29 - root - INFO: - print_num = 100
2023-11-02 14:56:29 - root - INFO: - dataset = LandUse_21
2023-11-02 15:03:18 - root - INFO: - --------------------Training over--------------------
2023-11-02 15:03:18 - root - INFO: - ACC:[0.2405, 0.2695, 0.2571, 0.2505, 0.2505]
2023-11-02 15:03:18 - root - INFO: - NMI:[0.3215, 0.3324, 0.314, 0.324, 0.3263]
2023-11-02 15:03:18 - root - INFO: - ARI:[0.135, 0.1364, 0.1264, 0.1291, 0.1372]
2023-11-02 15:03:18 - root - INFO: -  ACC 25.36 std 0.95 NMI 32.36 std 0.60 ARI 13.28 std 0.43
root@autodl-container-b72911863c-065c7124:~/2021-CVPR-Completer#
```




### Noisy Minist   missing_rate = 0.5    test_time = 5
```linux
root@autodl-container-7c5d4696fb-c54fea2a:~/2021-CVPR-Completer-main# python run.py --dataset 3 --devices 0 --print_num 100 --test_time 5
2024-11-06 20:24:01 - root - INFO: - Dataset:NoisyMNIST
2024-11-06 20:24:01 - root - INFO: - Prediction={
2024-11-06 20:24:01 - root - INFO: -           arch1 = [128, 256, 128]
2024-11-06 20:24:01 - root - INFO: -           arch2 = [128, 256, 128]
2024-11-06 20:24:01 - root - INFO: - Autoencoder={
2024-11-06 20:24:01 - root - INFO: -           arch1 = [784, 1024, 1024, 1024, 64]
2024-11-06 20:24:01 - root - INFO: -           arch2 = [784, 1024, 1024, 1024, 64]
2024-11-06 20:24:01 - root - INFO: -           activations1 = relu
2024-11-06 20:24:01 - root - INFO: -           activations2 = relu
2024-11-06 20:24:01 - root - INFO: -           batchnorm = True
2024-11-06 20:24:01 - root - INFO: - training={
2024-11-06 20:24:01 - root - INFO: -           missing_rate = 0.5
2024-11-06 20:24:01 - root - INFO: -           seed = 0
2024-11-06 20:24:01 - root - INFO: -           start_dual_prediction = 100
2024-11-06 20:24:01 - root - INFO: -           epoch = 500
2024-11-06 20:24:01 - root - INFO: -           batch_size = 256
2024-11-06 20:24:01 - root - INFO: -           lr = 0.0001
2024-11-06 20:24:01 - root - INFO: -           alpha = 9
2024-11-06 20:24:01 - root - INFO: -           lambda1 = 0.1
2024-11-06 20:24:01 - root - INFO: -           lambda2 = 0.1
2024-11-06 20:24:01 - root - INFO: - print_num = 100
2024-11-06 20:24:01 - root - INFO: - dataset = NoisyMNIST
2024-11-06 20:49:57 - root - INFO: - --------------------Training over--------------------
2024-11-06 20:49:57 - root - INFO: - ACC:[0.8045, 0.7358, 0.8032, 0.7683, 0.7365]
2024-11-06 20:49:57 - root - INFO: - NMI:[0.7655, 0.7443, 0.7496, 0.739, 0.7228]
2024-11-06 20:49:57 - root - INFO: - ARI:[0.7217, 0.6574, 0.7081, 0.6599, 0.616]
2024-11-06 20:49:57 - root - INFO: -  ACC 76.97 std 3.03 NMI 74.42 std 1.39 ARI 67.26 std 3.81
root@autodl-container-7c5d4696fb-c54fea2a:~/2021-CVPR-Completer-main# 
```



### Noisy Minist   missing_rate = 0    test_time = 1
```linux
root@autodl-container-534b4e910e-a60bb39b:~/2021-CVPR-Completer# python run.py --dataset 3 --test_time 1
2024-11-15 10:42:36 - root - INFO: - Dataset:NoisyMNIST
2024-11-15 10:42:36 - root - INFO: - Prediction={
2024-11-15 10:42:36 - root - INFO: -           arch1 = [128, 256, 128]
2024-11-15 10:42:36 - root - INFO: -           arch2 = [128, 256, 128]
2024-11-15 10:42:36 - root - INFO: - Autoencoder={
2024-11-15 10:42:36 - root - INFO: -           arch1 = [784, 1024, 1024, 1024, 64]
2024-11-15 10:42:36 - root - INFO: -           arch2 = [784, 1024, 1024, 1024, 64]
2024-11-15 10:42:36 - root - INFO: -           activations1 = relu
2024-11-15 10:42:36 - root - INFO: -           activations2 = relu
2024-11-15 10:42:36 - root - INFO: -           batchnorm = True
2024-11-15 10:42:36 - root - INFO: - training={
2024-11-15 10:42:36 - root - INFO: -           missing_rate = 0
2024-11-15 10:42:36 - root - INFO: -           seed = 0
2024-11-15 10:42:36 - root - INFO: -           start_dual_prediction = 100
2024-11-15 10:42:36 - root - INFO: -           epoch = 500
2024-11-15 10:42:36 - root - INFO: -           batch_size = 256
2024-11-15 10:42:36 - root - INFO: -           lr = 0.0001
2024-11-15 10:42:36 - root - INFO: -           alpha = 9
2024-11-15 10:42:36 - root - INFO: -           lambda1 = 0.1
2024-11-15 10:42:36 - root - INFO: -           lambda2 = 0.1
2024-11-15 10:42:36 - root - INFO: - print_num = 100
2024-11-15 10:42:36 - root - INFO: - dataset = NoisyMNIST
2024-11-15 10:52:40 - root - INFO: - --------------------Training over--------------------
2024-11-15 10:52:40 - root - INFO: - ACC:[0.8433]
2024-11-15 10:52:40 - root - INFO: - NMI:[0.8621]
2024-11-15 10:52:40 - root - INFO: - ARI:[0.8024]
2024-11-15 10:52:40 - root - INFO: -  ACC 84.33 std 0.00 NMI 86.21 std 0.00 ARI 80.24 std 0.00
```


###  dataset scene_15 加了一个outlookattention 模块处理特征数据，和文章的效果差很多。 
```linux
2024-11-24 16:01:36 - root - INFO: - --------------------Training over--------------------
2024-11-24 16:01:36 - root - INFO: - ACC:[0.2196]
2024-11-24 16:01:36 - root - INFO: - NMI:[0.2012]
2024-11-24 16:01:36 - root - INFO: - ARI:[0.0857]
2024-11-24 16:01:36 - root - INFO: -  ACC 21.96 std 0.00 NMI 20.12 std 0.00 ARI 8.57 std 0.00
root@autodl-container-879242bf41-4f27cd59:~/2021-CVPR-Completer# 
```


###  dataset scene_15 加了一个efficientattention 模块处理特征数据，和文章的效果差很多。 

```
2024-11-26 12:07:34 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 0.1404===> Reconstruction loss = 0.1228 ===> Dual prediction loss = 0.0340  ===> Contrastive loss = -8.0739e+02 ===> Loss = -8.0736e+02
2024-11-26 12:07:35 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2685, 'NMI': 0.2747, 'ARI': 0.1206, 'accuracy': 0.2751, 'precision': 0.3065, 'recall': 0.2731, 'f_measure': 0.2602}}
2024-11-26 12:07:49 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 0.0934===> Reconstruction loss = 0.0793 ===> Dual prediction loss = 0.0015  ===> Contrastive loss = -8.1010e+02 ===> Loss = -8.1008e+02
2024-11-26 12:07:50 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2583, 'NMI': 0.2646, 'ARI': 0.1062, 'accuracy': 0.2731, 'precision': 0.3124, 'recall': 0.2746, 'f_measure': 0.2612}}
2024-11-26 12:08:04 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 0.0843===> Reconstruction loss = 0.0772 ===> Dual prediction loss = 0.0013  ===> Contrastive loss = -8.1013e+02 ===> Loss = -8.1012e+02
2024-11-26 12:08:05 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2721, 'NMI': 0.2784, 'ARI': 0.1225, 'accuracy': 0.2852, 'precision': 0.3409, 'recall': 0.2855, 'f_measure': 0.2798}}
2024-11-26 12:08:20 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 0.0877===> Reconstruction loss = 0.0736 ===> Dual prediction loss = 0.0013  ===> Contrastive loss = -8.1123e+02 ===> Loss = -8.1122e+02
2024-11-26 12:08:20 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2486, 'NMI': 0.255, 'ARI': 0.0959, 'accuracy': 0.2638, 'precision': 0.3024, 'recall': 0.2617, 'f_measure': 0.2579}}
2024-11-26 12:08:36 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 0.0837===> Reconstruction loss = 0.0716 ===> Dual prediction loss = 0.0011  ===> Contrastive loss = -8.1174e+02 ===> Loss = -8.1172e+02
2024-11-26 12:08:37 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2616, 'NMI': 0.2679, 'ARI': 0.1019, 'accuracy': 0.2702, 'precision': 0.3122, 'recall': 0.265, 'f_measure': 0.2597}}
2024-11-26 12:08:37 - root - INFO: - --------------------Training over--------------------
2024-11-26 12:08:37 - root - INFO: - ACC:[0.2702]
2024-11-26 12:08:37 - root - INFO: - NMI:[0.2679]
2024-11-26 12:08:37 - root - INFO: - ARI:[0.1019]
2024-11-26 12:08:37 - root - INFO: -  ACC 27.02 std 0.00 NMI 26.79 std 0.00 ARI 10.19 std 0.00
root@autodl-container-0c4b4cae70-1b2227a1:~/2021-CVPR-Completer#

```

### dataset scene_15 加了一个Knntattention 模块处理特征数据，和文章的效果差很多。 
```linux  
2024-11-26 15:20:24 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 2.0948===> Reconstruction loss = 2.4482 ===> Dual prediction loss = 0.0412  ===> Contrastive loss = -8.0818e+02 ===> Loss = -8.0773e+02
2024-11-26 15:20:25 - root - INFO: - view_concat {'kmeans': {'AMI': 0.1766, 'NMI': 0.1838, 'ARI': 0.0657, 'accuracy': 0.223, 'precision': 0.2667, 'recall': 0.2103, 'f_measure': 0.2086}}
2024-11-26 15:20:41 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 1.8932===> Reconstruction loss = 2.2442 ===> Dual prediction loss = 0.0021  ===> Contrastive loss = -8.1064e+02 ===> Loss = -8.1023e+02
2024-11-26 15:20:42 - root - INFO: - view_concat {'kmeans': {'AMI': 0.165, 'NMI': 0.1721, 'ARI': 0.07, 'accuracy': 0.2247, 'precision': 0.2716, 'recall': 0.2177, 'f_measure': 0.2203}}
2024-11-26 15:20:57 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 1.8053===> Reconstruction loss = 2.1733 ===> Dual prediction loss = 0.0015  ===> Contrastive loss = -8.1160e+02 ===> Loss = -8.1120e+02
2024-11-26 15:20:58 - root - INFO: - view_concat {'kmeans': {'AMI': 0.1509, 'NMI': 0.1584, 'ARI': 0.0332, 'accuracy': 0.2058, 'precision': 0.2718, 'recall': 0.1981, 'f_measure': 0.2108}}
2024-11-26 15:21:13 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 1.7377===> Reconstruction loss = 2.1286 ===> Dual prediction loss = 0.0014  ===> Contrastive loss = -8.1210e+02 ===> Loss = -8.1171e+02
2024-11-26 15:21:13 - root - INFO: - view_concat {'kmeans': {'AMI': 0.1748, 'NMI': 0.1819, 'ARI': 0.0698, 'accuracy': 0.2252, 'precision': 0.2712, 'recall': 0.2148, 'f_measure': 0.2205}}
2024-11-26 15:21:27 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 1.7014===> Reconstruction loss = 2.0836 ===> Dual prediction loss = 0.0012  ===> Contrastive loss = -8.1278e+02 ===> Loss = -8.1241e+02
2024-11-26 15:21:28 - root - INFO: - view_concat {'kmeans': {'AMI': 0.1724, 'NMI': 0.1795, 'ARI': 0.0726, 'accuracy': 0.2169, 'precision': 0.2569, 'recall': 0.2075, 'f_measure': 0.2089}}
2024-11-26 15:21:28 - root - INFO: - --------------------Training over--------------------
2024-11-26 15:21:28 - root - INFO: - ACC:[0.2169]
2024-11-26 15:21:28 - root - INFO: - NMI:[0.1795]
2024-11-26 15:21:28 - root - INFO: - ARI:[0.0726]
2024-11-26 15:21:28 - root - INFO: -  ACC 21.69 std 0.00 NMI 17.95 std 0.00 ARI 7.26 std 0.00


````

### dataset scene_15 加了一个LinAngularattention 模块处理特征数据，和文章的效果差一点点！！！感觉可以搞进去 
```linux
2024-11-26 16:13:10 - root - INFO: - --------------------Training over--------------------
2024-11-26 16:13:10 - root - INFO: - ACC:[0.359, 0.3266, 0.3721, 0.3547, 0.371]
2024-11-26 16:13:10 - root - INFO: - NMI:[0.3895, 0.3994, 0.3762, 0.397, 0.3807]
2024-11-26 16:13:10 - root - INFO: - ARI:[0.2049, 0.189, 0.1903, 0.2043, 0.1819]
2024-11-26 16:13:10 - root - INFO: -  ACC 35.67 std 1.65 NMI 38.86 std 0.90 ARI 19.41 std 0.91
```


### dataset scene_15 加了一个UFOattention 模块处理特征数据，和文章的效果差得巨多 
```linux
2024-11-26 19:34:00 - root - INFO: - --------------------Training over--------------------
2024-11-26 19:34:00 - root - INFO: - ACC:[0.1253, 0.1264, 0.1327, 0.1302, 0.1284, 0.1233, 0.1168, 0.1224, 0.1338, 0.1217]
2024-11-26 19:34:00 - root - INFO: - NMI:[0.0498, 0.048, 0.0628, 0.0661, 0.05, 0.0444, 0.0414, 0.0522, 0.0573, 0.0391]
2024-11-26 19:34:00 - root - INFO: - ARI:[0.0112, 0.0167, 0.0168, 0.0174, 0.0155, 0.0096, 0.0076, 0.0167, 0.0162, 0.0195]
2024-11-26 19:34:00 - root - INFO: -  ACC 12.61 std 0.50 NMI 5.11 std 0.83 ARI 1.47 std 0.37
root@autodl-container-824e4b9535-3ca58236:~/2021-CVPR-Completer# 
```

### dataset scene_15 加了一个LSKBlock 模块处理特征数据，和文章的效果几乎一样！！！
```linux
2024-11-26 20:41:12 - root - INFO: - --------------------Training over--------------------
2024-11-26 20:41:12 - root - INFO: - ACC:[0.3246, 0.4085, 0.3808, 0.3614, 0.3728]
2024-11-26 20:41:12 - root - INFO: - NMI:[0.3874, 0.4295, 0.4206, 0.3857, 0.4024]
2024-11-26 20:41:12 - root - INFO: - ARI:[0.1909, 0.2416, 0.2364, 0.212, 0.2129]
2024-11-26 20:41:12 - root - INFO: -  ACC 36.96 std 2.74 NMI 40.51 std 1.75 ARI 21.88 std 1.84
```

### dataset scene_15 加了一个MobileTv2Attention 模块处理特征数据，和文章的效果差很多
```linux
2024-11-26 20:54:03 - root - INFO: - --------------------Training over--------------------
2024-11-26 20:54:03 - root - INFO: - ACC:[0.1215]
2024-11-26 20:54:03 - root - INFO: - NMI:[0.0608]
2024-11-26 20:54:03 - root - INFO: - ARI:[0.0112]
2024-11-26 20:54:03 - root - INFO: -  ACC 12.15 std 0.00 NMI 6.08 std 0.00 ARI 1.12 std 0.00
root@autodl-container-824e4b9535-3ca58236:~/2021-CVPR-Completer# 
```


### dataset scene_15 加了一个MuseAttention 模块处理特征数据，和文章的效果差30%的样子
```linux
2024-11-26 21:37:37 - root - INFO: - --------------------Training over--------------------
2024-11-26 21:37:37 - root - INFO: - ACC:[0.32]
2024-11-26 21:37:37 - root - INFO: - NMI:[0.2894]
2024-11-26 21:37:37 - root - INFO: - ARI:[0.1075]
2024-11-26 21:37:37 - root - INFO: -  ACC 32.00 std 0.00 NMI 28.94 std 0.00 ARI 10.75 std 0.00
```


### dataset scene_15 加了一个ParNetAttention 模块处理特征数据，Scene-15.mat 没有什么大的改变


### dataset scene_15 加了一个PartialConv3 模块处理特征数据， missing rate = 0.5 和 missing rate = 0 效果都提升了5%左右
1. miss rate = 0.5 test-time = 5
```linux
2024-11-26 22:13:46 - root - INFO: - --------------------Training over--------------------
2024-11-26 22:13:46 - root - INFO: - ACC:[0.3924, 0.3864, 0.4013, 0.408, 0.4156]
2024-11-26 22:13:46 - root - INFO: - NMI:[0.4847, 0.4638, 0.4759, 0.4935, 0.4949]
2024-11-26 22:13:46 - root - INFO: - ARI:[0.299, 0.2743, 0.2852, 0.3028, 0.3043]
2024-11-26 22:13:46 - root - INFO: -  ACC 40.07 std 1.05 NMI 48.26 std 1.16 ARI 29.31 std 1.16
root@autodl-container-824e4b9535-3ca58236:~/2021-CVPR-Completer# 
```


2.miss rate = 0 test-time = 5
```linux
2024-11-26 22:30:20 - root - INFO: - --------------------Training over--------------------
2024-11-26 22:30:20 - root - INFO: - ACC:[0.3978, 0.4132, 0.4205, 0.4025, 0.4132]
2024-11-26 22:30:20 - root - INFO: - NMI:[0.4935, 0.487, 0.4874, 0.4908, 0.4916]
2024-11-26 22:30:20 - root - INFO: - ARI:[0.2989, 0.2901, 0.3043, 0.2879, 0.3057]
2024-11-26 22:30:20 - root - INFO: -  ACC 40.94 std 0.82 NMI 49.01 std 0.25 ARI 29.74 std 0.72
root@autodl-container-824e4b9535-3ca58236:~/2021-CVPR-Completer# 
```


### dataset scene_15 加了一个S2Attention 模块处理特征数据， missing rate = 0 效果差20% 的样子
```bash
2024-11-26 23:19:04 - root - INFO: - --------------------Training over--------------------
2024-11-26 23:19:04 - root - INFO: - ACC:[0.3739]
2024-11-26 23:19:04 - root - INFO: - NMI:[0.3617]
2024-11-26 23:19:04 - root - INFO: - ARI:[0.2151]
2024-11-26 23:19:04 - root - INFO: -  ACC 37.39 std 0.00 NMI 36.17 std 0.00 ARI 21.51 std 0.00
root@autodl-container-824e4b9535-3ca58236:~/2021-CVPR-Completer# 
```

### dataset scene_15 ScConv 缝不进去


### dataset scene_15 加了一个 Simam模块处理特征数据， missing rate = 0 test-time = 5 效果和文章差不太多
```bash
2024-11-27 11:07:04 - root - INFO: - --------------------Training over--------------------
2024-11-27 11:07:04 - root - INFO: - ACC:[0.367, 0.4078, 0.4045, 0.3971, 0.4234]
2024-11-27 11:07:04 - root - INFO: - NMI:[0.3871, 0.4401, 0.4346, 0.4396, 0.4409]
2024-11-27 11:07:04 - root - INFO: - ARI:[0.1701, 0.2434, 0.2412, 0.246, 0.2574]
2024-11-27 11:07:04 - root - INFO: -  ACC 40.00 std 1.86 NMI 42.85 std 2.08 ARI 23.16 std 3.13
root@autodl-container-824e4b9535-3ca58236:~/2021-CVPR-Completer# 
```

### dataset scene_15 跑了一个随机赋值的Scene-15,3个cell里面的所有数据都发生改变，由gpt随机赋值给它，赋值区间是0~1之间。
```bash
2024-11-27 11:16:54 - root - INFO: - --------------------Training over--------------------
2024-11-27 11:16:54 - root - INFO: - ACC:[0.0885]
2024-11-27 11:16:54 - root - INFO: - NMI:[0.0086]
2024-11-27 11:16:54 - root - INFO: - ARI:[-0.0001]
2024-11-27 11:16:54 - root - INFO: -  ACC 8.85 std 0.00 NMI 0.86 std 0.00 ARI -0.01 std 0.00
root@autodl-container-824e4b9535-3ca58236:~/2021-CVPR-Completer# 
```


### dataset scene_15 跑了一个随机赋值的Scene-15,第一个cell里面的所有数据都发生改变，由gpt随机赋值给它，赋值区间是0~1之间。
```bash
2024-11-27 14:42:23 - root - INFO: - --------------------Training over--------------------
2024-11-27 14:42:23 - root - INFO: - ACC:[0.2047]
2024-11-27 14:42:23 - root - INFO: - NMI:[0.2063]
2024-11-27 14:42:23 - root - INFO: - ARI:[0.1015]
2024-11-27 14:42:23 - root - INFO: -  ACC 20.47 std 0.00 NMI 20.63 std 0.00 ARI 10.15 std 0.00
```


### dataset scene_15 跑了一个随机赋值的Scene-15,第一个的cell里面的所有数值是0到1之间，随机赋值，第二个cell里面所有的数值0到2之间
```bash
2024-11-27 14:48:33 - root - INFO: - --------------------Training over--------------------
2024-11-27 14:48:33 - root - INFO: - ACC:[0.0894]
2024-11-27 14:48:33 - root - INFO: - NMI:[0.0068]
2024-11-27 14:48:33 - root - INFO: - ARI:[-0.0005]
2024-11-27 14:48:33 - root - INFO: -  ACC 8.94 std 0.00 NMI 0.68 std 0.00 ARI -0.05 std 0.00
```
