## 1. 2021-CVPR-Completer(Running logs)
[reference](https://github.com/XLearning-SCU/2021-CVPR-Completer)

time:2023-11-1、2024-11-15

跑完的数据集: Caltech101-20、Scene_15、LandUse_21，和原论文效果差不多。

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

### dataset: Caltech101-20  missing_rate = 0 test_time = 1

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




### dataset: :Scene_15    missing_rate = 0.5  test_time = 5
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


#### Noisy Minist   missing_rate = 0.5    test_time = 5
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



#### Noisy Minist   missing_rate = 0    test_time = 5
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
