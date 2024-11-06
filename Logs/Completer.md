## 1. 2021-CVPR-Completer(Running logs)
[reference](https://github.com/XLearning-SCU/2021-CVPR-Completer)

time:2023-11-1

status:Running successfully

logs following like this :

跑完的数据集: Caltech101-20、Scene_15、LandUse_21

### dataset: Caltech101-20
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
2023-11-01 17:06:11 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=1984, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=1984, bias=True)
    (10): BatchNorm1d(1984, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-01 17:06:11 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-01 17:06:11 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-01 17:06:19 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 0.2803===> Reconstruction loss = 0.0261 ===> Dual prediction loss = 0.0167  ===> Contrastive loss = -4.4798e+02 ===> Loss = -4.4795e+02
2023-11-01 17:06:20 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6111, 'NMI': 0.6243, 'ARI': 0.5895, 'accuracy': 0.5951, 'precision': 0.4677, 'recall': 0.3902, 'f_measure': 0.4002}}
2023-11-01 17:06:27 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 0.2665===> Reconstruction loss = 0.0235 ===> Dual prediction loss = 0.0009  ===> Contrastive loss = -4.4799e+02 ===> Loss = -4.4796e+02
2023-11-01 17:06:28 - root - INFO: - view_concat {'kmeans': {'AMI': 0.7013, 'NMI': 0.7119, 'ARI': 0.8829, 'accuracy': 0.7594, 'precision': 0.5192, 'recall': 0.4538, 'f_measure': 0.4595}}
2023-11-01 17:06:35 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 0.2528===> Reconstruction loss = 0.0259 ===> Dual prediction loss = 0.0009  ===> Contrastive loss = -4.4827e+02 ===> Loss = -4.4825e+02
2023-11-01 17:06:36 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6956, 'NMI': 0.7062, 'ARI': 0.8756, 'accuracy': 0.7565, 'precision': 0.4984, 'recall': 0.4505, 'f_measure': 0.4446}}
2023-11-01 17:06:44 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 0.2416===> Reconstruction loss = 0.0227 ===> Dual prediction loss = 0.0009  ===> Contrastive loss = -4.4844e+02 ===> Loss = -4.4842e+02
2023-11-01 17:06:45 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6933, 'NMI': 0.704, 'ARI': 0.8805, 'accuracy': 0.7619, 'precision': 0.5129, 'recall': 0.4705, 'f_measure': 0.4618}}
2023-11-01 17:06:53 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 0.2374===> Reconstruction loss = 0.0201 ===> Dual prediction loss = 0.0009  ===> Contrastive loss = -4.4764e+02 ===> Loss = -4.4762e+02
2023-11-01 17:06:54 - root - INFO: - view_concat {'kmeans': {'AMI': 0.697, 'NMI': 0.7073, 'ARI': 0.8785, 'accuracy': 0.7649, 'precision': 0.4956, 'recall': 0.4666, 'f_measure': 0.457}}
2023-11-01 17:06:54 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=1984, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=1984, bias=True)
    (10): BatchNorm1d(1984, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-01 17:06:54 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-01 17:06:54 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-01 17:07:01 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 0.2822===> Reconstruction loss = 0.0264 ===> Dual prediction loss = 0.0193  ===> Contrastive loss = -4.4864e+02 ===> Loss = -4.4861e+02
2023-11-01 17:07:01 - root - INFO: - view_concat {'kmeans': {'AMI': 0.5865, 'NMI': 0.6006, 'ARI': 0.5848, 'accuracy': 0.5591, 'precision': 0.4953, 'recall': 0.388, 'f_measure': 0.4158}}
2023-11-01 17:07:09 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 0.2663===> Reconstruction loss = 0.0224 ===> Dual prediction loss = 0.0014  ===> Contrastive loss = -4.4936e+02 ===> Loss = -4.4933e+02
2023-11-01 17:07:10 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6296, 'NMI': 0.642, 'ARI': 0.5063, 'accuracy': 0.5637, 'precision': 0.4856, 'recall': 0.453, 'f_measure': 0.4484}}
2023-11-01 17:07:18 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 0.2585===> Reconstruction loss = 0.0225 ===> Dual prediction loss = 0.0008  ===> Contrastive loss = -4.4954e+02 ===> Loss = -4.4951e+02
2023-11-01 17:07:18 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6509, 'NMI': 0.6628, 'ARI': 0.6554, 'accuracy': 0.6366, 'precision': 0.492, 'recall': 0.474, 'f_measure': 0.4643}}
2023-11-01 17:07:26 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 0.2498===> Reconstruction loss = 0.0212 ===> Dual prediction loss = 0.0008  ===> Contrastive loss = -4.4863e+02 ===> Loss = -4.4860e+02
2023-11-01 17:07:26 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6539, 'NMI': 0.6656, 'ARI': 0.6614, 'accuracy': 0.6446, 'precision': 0.5295, 'recall': 0.4791, 'f_measure': 0.4772}}
2023-11-01 17:07:34 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 0.2299===> Reconstruction loss = 0.0203 ===> Dual prediction loss = 0.0013  ===> Contrastive loss = -4.4938e+02 ===> Loss = -4.4935e+02
2023-11-01 17:07:35 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6583, 'NMI': 0.6698, 'ARI': 0.6619, 'accuracy': 0.6412, 'precision': 0.4928, 'recall': 0.4724, 'f_measure': 0.4642}}
2023-11-01 17:07:35 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=1984, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=1984, bias=True)
    (10): BatchNorm1d(1984, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-01 17:07:35 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-01 17:07:35 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-01 17:07:42 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 0.2758===> Reconstruction loss = 0.0234 ===> Dual prediction loss = 0.0159  ===> Contrastive loss = -4.4793e+02 ===> Loss = -4.4790e+02
2023-11-01 17:07:43 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6258, 'NMI': 0.6383, 'ARI': 0.6861, 'accuracy': 0.635, 'precision': 0.4337, 'recall': 0.3927, 'f_measure': 0.3808}}
2023-11-01 17:07:51 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 0.2543===> Reconstruction loss = 0.0243 ===> Dual prediction loss = 0.0010  ===> Contrastive loss = -4.4827e+02 ===> Loss = -4.4824e+02
2023-11-01 17:07:51 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6683, 'NMI': 0.6791, 'ARI': 0.7231, 'accuracy': 0.6832, 'precision': 0.4583, 'recall': 0.4342, 'f_measure': 0.425}}
2023-11-01 17:07:59 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 0.2413===> Reconstruction loss = 0.0204 ===> Dual prediction loss = 0.0008  ===> Contrastive loss = -4.4816e+02 ===> Loss = -4.4814e+02
2023-11-01 17:07:59 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6981, 'NMI': 0.7071, 'ARI': 0.8811, 'accuracy': 0.7561, 'precision': 0.4343, 'recall': 0.4386, 'f_measure': 0.4063}}
2023-11-01 17:08:07 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 0.2318===> Reconstruction loss = 0.0202 ===> Dual prediction loss = 0.0009  ===> Contrastive loss = -4.4863e+02 ===> Loss = -4.4861e+02
2023-11-01 17:08:08 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6973, 'NMI': 0.7069, 'ARI': 0.8822, 'accuracy': 0.7565, 'precision': 0.4378, 'recall': 0.4374, 'f_measure': 0.4127}}
2023-11-01 17:08:16 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 0.2244===> Reconstruction loss = 0.0200 ===> Dual prediction loss = 0.0004  ===> Contrastive loss = -4.4846e+02 ===> Loss = -4.4843e+02
2023-11-01 17:08:16 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6986, 'NMI': 0.7079, 'ARI': 0.8773, 'accuracy': 0.7607, 'precision': 0.4324, 'recall': 0.445, 'f_measure': 0.4155}}
2023-11-01 17:08:17 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=1984, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=1984, bias=True)
    (10): BatchNorm1d(1984, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-01 17:08:17 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-01 17:08:17 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-01 17:08:23 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 0.2848===> Reconstruction loss = 0.0297 ===> Dual prediction loss = 0.0155  ===> Contrastive loss = -4.4715e+02 ===> Loss = -4.4712e+02
2023-11-01 17:08:24 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6114, 'NMI': 0.6244, 'ARI': 0.5949, 'accuracy': 0.5868, 'precision': 0.4782, 'recall': 0.4135, 'f_measure': 0.4079}}
2023-11-01 17:08:32 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 0.2594===> Reconstruction loss = 0.0271 ===> Dual prediction loss = 0.0025  ===> Contrastive loss = -4.4786e+02 ===> Loss = -4.4783e+02
2023-11-01 17:08:32 - root - INFO: - view_concat {'kmeans': {'AMI': 0.712, 'NMI': 0.7219, 'ARI': 0.8853, 'accuracy': 0.7615, 'precision': 0.4954, 'recall': 0.4726, 'f_measure': 0.453}}
2023-11-01 17:08:40 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 0.2307===> Reconstruction loss = 0.0205 ===> Dual prediction loss = 0.0007  ===> Contrastive loss = -4.4861e+02 ===> Loss = -4.4859e+02
2023-11-01 17:08:41 - root - INFO: - view_concat {'kmeans': {'AMI': 0.7138, 'NMI': 0.7236, 'ARI': 0.8829, 'accuracy': 0.7632, 'precision': 0.5257, 'recall': 0.4789, 'f_measure': 0.4659}}
2023-11-01 17:08:49 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 0.2237===> Reconstruction loss = 0.0202 ===> Dual prediction loss = 0.0012  ===> Contrastive loss = -4.4814e+02 ===> Loss = -4.4812e+02
2023-11-01 17:08:50 - root - INFO: - view_concat {'kmeans': {'AMI': 0.7159, 'NMI': 0.7254, 'ARI': 0.8839, 'accuracy': 0.7649, 'precision': 0.5005, 'recall': 0.4815, 'f_measure': 0.4576}}
2023-11-01 17:08:58 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 0.2113===> Reconstruction loss = 0.0196 ===> Dual prediction loss = 0.0010  ===> Contrastive loss = -4.4871e+02 ===> Loss = -4.4868e+02
2023-11-01 17:08:59 - root - INFO: - view_concat {'kmeans': {'AMI': 0.7151, 'NMI': 0.7248, 'ARI': 0.8811, 'accuracy': 0.7628, 'precision': 0.4859, 'recall': 0.4726, 'f_measure': 0.4478}}
2023-11-01 17:08:59 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=1984, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=1984, bias=True)
    (10): BatchNorm1d(1984, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-01 17:08:59 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-01 17:08:59 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-01 17:09:06 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 0.2877===> Reconstruction loss = 0.0316 ===> Dual prediction loss = 0.0152  ===> Contrastive loss = -4.4752e+02 ===> Loss = -4.4749e+02
2023-11-01 17:09:07 - root - INFO: - view_concat {'kmeans': {'AMI': 0.5804, 'NMI': 0.5947, 'ARI': 0.6632, 'accuracy': 0.6127, 'precision': 0.4126, 'recall': 0.3746, 'f_measure': 0.3764}}
2023-11-01 17:09:14 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 0.2666===> Reconstruction loss = 0.0226 ===> Dual prediction loss = 0.0012  ===> Contrastive loss = -4.4761e+02 ===> Loss = -4.4758e+02
2023-11-01 17:09:15 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6544, 'NMI': 0.666, 'ARI': 0.7037, 'accuracy': 0.6521, 'precision': 0.41, 'recall': 0.4054, 'f_measure': 0.3802}}
2023-11-01 17:09:22 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 0.2565===> Reconstruction loss = 0.0226 ===> Dual prediction loss = 0.0008  ===> Contrastive loss = -4.4781e+02 ===> Loss = -4.4778e+02
2023-11-01 17:09:23 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6827, 'NMI': 0.6934, 'ARI': 0.8791, 'accuracy': 0.7326, 'precision': 0.4102, 'recall': 0.4152, 'f_measure': 0.3781}}
2023-11-01 17:09:31 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 0.2471===> Reconstruction loss = 0.0194 ===> Dual prediction loss = 0.0005  ===> Contrastive loss = -4.4838e+02 ===> Loss = -4.4836e+02
2023-11-01 17:09:31 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6815, 'NMI': 0.6924, 'ARI': 0.8838, 'accuracy': 0.736, 'precision': 0.4063, 'recall': 0.4222, 'f_measure': 0.3884}}
2023-11-01 17:09:39 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 0.2346===> Reconstruction loss = 0.0195 ===> Dual prediction loss = 0.0005  ===> Contrastive loss = -4.4799e+02 ===> Loss = -4.4796e+02
2023-11-01 17:09:40 - root - INFO: - view_concat {'kmeans': {'AMI': 0.6671, 'NMI': 0.6785, 'ARI': 0.8384, 'accuracy': 0.6899, 'precision': 0.4228, 'recall': 0.4089, 'f_measure': 0.3813}}
2023-11-01 17:09:40 - root - INFO: - --------------------Training over--------------------
2023-11-01 17:09:40 - root - INFO: - ACC:[0.7649, 0.6412, 0.7607, 0.7628, 0.6899]
2023-11-01 17:09:40 - root - INFO: - NMI:[0.7073, 0.6698, 0.7079, 0.7248, 0.6785]
2023-11-01 17:09:40 - root - INFO: - ARI:[0.8785, 0.6619, 0.8773, 0.8811, 0.8384]
2023-11-01 17:09:40 - root - INFO: -  ACC 72.39 std 5.01 NMI 69.77 std 2.04 ARI 82.74 std 8.43
root@autodl-container-e6d91195fa-0bc38630:~/2021-CVPR-Completer# 
```


### dataset: :Scene_15
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
2023-11-02 14:48:26 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=20, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=20, bias=True)
    (10): BatchNorm1d(20, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 14:48:26 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 14:48:26 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 14:48:37 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 3.2137===> Reconstruction loss = 20.3053 ===> Dual prediction loss = 0.0290  ===> Contrastive loss = -8.0621e+02 ===> Loss = -8.0386e+02
2023-11-02 14:48:38 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4151, 'NMI': 0.4199, 'ARI': 0.2311, 'accuracy': 0.392, 'precision': 0.3844, 'recall': 0.3988, 'f_measure': 0.3744}}
2023-11-02 14:48:55 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 2.6852===> Reconstruction loss = 19.4147 ===> Dual prediction loss = 0.0049  ===> Contrastive loss = -8.0841e+02 ===> Loss = -8.0620e+02
2023-11-02 14:48:56 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4177, 'NMI': 0.4225, 'ARI': 0.2331, 'accuracy': 0.3902, 'precision': 0.381, 'recall': 0.398, 'f_measure': 0.3727}}
2023-11-02 14:49:13 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 2.2353===> Reconstruction loss = 18.5876 ===> Dual prediction loss = 0.0036  ===> Contrastive loss = -8.0989e+02 ===> Loss = -8.0780e+02
2023-11-02 14:49:14 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4198, 'NMI': 0.4246, 'ARI': 0.2388, 'accuracy': 0.392, 'precision': 0.3805, 'recall': 0.3993, 'f_measure': 0.3716}}
2023-11-02 14:49:31 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 1.8464===> Reconstruction loss = 17.8627 ===> Dual prediction loss = 0.0028  ===> Contrastive loss = -8.1123e+02 ===> Loss = -8.0926e+02
2023-11-02 14:49:31 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4188, 'NMI': 0.4236, 'ARI': 0.2356, 'accuracy': 0.3904, 'precision': 0.3794, 'recall': 0.3965, 'f_measure': 0.3726}}
2023-11-02 14:49:48 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 1.5275===> Reconstruction loss = 17.1648 ===> Dual prediction loss = 0.0031  ===> Contrastive loss = -8.1080e+02 ===> Loss = -8.0893e+02
2023-11-02 14:49:49 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4017, 'NMI': 0.4067, 'ARI': 0.215, 'accuracy': 0.3802, 'precision': 0.3617, 'recall': 0.3819, 'f_measure': 0.3538}}
2023-11-02 14:49:49 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=20, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=20, bias=True)
    (10): BatchNorm1d(20, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 14:49:49 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 14:49:49 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 14:50:00 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 3.2449===> Reconstruction loss = 20.3315 ===> Dual prediction loss = 0.0276  ===> Contrastive loss = -8.0559e+02 ===> Loss = -8.0323e+02
2023-11-02 14:50:01 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3785, 'NMI': 0.3837, 'ARI': 0.2048, 'accuracy': 0.3625, 'precision': 0.3533, 'recall': 0.3636, 'f_measure': 0.3424}}
2023-11-02 14:50:18 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 2.7083===> Reconstruction loss = 19.4025 ===> Dual prediction loss = 0.0047  ===> Contrastive loss = -8.0799e+02 ===> Loss = -8.0578e+02
2023-11-02 14:50:19 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4194, 'NMI': 0.4242, 'ARI': 0.2407, 'accuracy': 0.4027, 'precision': 0.3786, 'recall': 0.4069, 'f_measure': 0.3787}}
2023-11-02 14:50:36 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 2.3066===> Reconstruction loss = 18.6203 ===> Dual prediction loss = 0.0032  ===> Contrastive loss = -8.0942e+02 ===> Loss = -8.0733e+02
2023-11-02 14:50:37 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4182, 'NMI': 0.423, 'ARI': 0.2386, 'accuracy': 0.398, 'precision': 0.3832, 'recall': 0.4026, 'f_measure': 0.375}}
2023-11-02 14:50:54 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 1.9499===> Reconstruction loss = 17.8911 ===> Dual prediction loss = 0.0027  ===> Contrastive loss = -8.1108e+02 ===> Loss = -8.0910e+02
2023-11-02 14:50:55 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4191, 'NMI': 0.424, 'ARI': 0.239, 'accuracy': 0.4018, 'precision': 0.3897, 'recall': 0.4067, 'f_measure': 0.3792}}
2023-11-02 14:51:12 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 1.5959===> Reconstruction loss = 17.2206 ===> Dual prediction loss = 0.0026  ===> Contrastive loss = -8.1075e+02 ===> Loss = -8.0886e+02
2023-11-02 14:51:12 - root - INFO: - view_concat {'kmeans': {'AMI': 0.42, 'NMI': 0.4248, 'ARI': 0.2419, 'accuracy': 0.404, 'precision': 0.3868, 'recall': 0.4098, 'f_measure': 0.3793}}
2023-11-02 14:51:12 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=20, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=20, bias=True)
    (10): BatchNorm1d(20, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 14:51:12 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 14:51:12 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 14:51:24 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 3.2418===> Reconstruction loss = 20.0056 ===> Dual prediction loss = 0.0278  ===> Contrastive loss = -8.0538e+02 ===> Loss = -8.0306e+02
2023-11-02 14:51:25 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4227, 'NMI': 0.4275, 'ARI': 0.2423, 'accuracy': 0.4047, 'precision': 0.3782, 'recall': 0.4039, 'f_measure': 0.3782}}
2023-11-02 14:51:42 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 2.7188===> Reconstruction loss = 19.1578 ===> Dual prediction loss = 0.0052  ===> Contrastive loss = -8.0835e+02 ===> Loss = -8.0616e+02
2023-11-02 14:51:42 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4293, 'NMI': 0.434, 'ARI': 0.2495, 'accuracy': 0.4111, 'precision': 0.3843, 'recall': 0.408, 'f_measure': 0.3836}}
2023-11-02 14:52:00 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 2.3048===> Reconstruction loss = 18.3163 ===> Dual prediction loss = 0.0045  ===> Contrastive loss = -8.0900e+02 ===> Loss = -8.0694e+02
2023-11-02 14:52:01 - root - INFO: - view_concat {'kmeans': {'AMI': 0.429, 'NMI': 0.4337, 'ARI': 0.2505, 'accuracy': 0.41, 'precision': 0.3844, 'recall': 0.4066, 'f_measure': 0.381}}
2023-11-02 14:52:18 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 1.9013===> Reconstruction loss = 17.6305 ===> Dual prediction loss = 0.0028  ===> Contrastive loss = -8.1075e+02 ===> Loss = -8.0880e+02
2023-11-02 14:52:19 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4401, 'NMI': 0.4448, 'ARI': 0.2565, 'accuracy': 0.4074, 'precision': 0.3914, 'recall': 0.4167, 'f_measure': 0.3929}}
2023-11-02 14:52:37 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 1.5768===> Reconstruction loss = 16.9151 ===> Dual prediction loss = 0.0033  ===> Contrastive loss = -8.1009e+02 ===> Loss = -8.0824e+02
2023-11-02 14:52:38 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4274, 'NMI': 0.4321, 'ARI': 0.2378, 'accuracy': 0.39, 'precision': 0.3813, 'recall': 0.3902, 'f_measure': 0.3768}}
2023-11-02 14:52:38 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=20, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=20, bias=True)
    (10): BatchNorm1d(20, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 14:52:38 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 14:52:38 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 14:52:50 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 3.2211===> Reconstruction loss = 20.2730 ===> Dual prediction loss = 0.0269  ===> Contrastive loss = -8.0475e+02 ===> Loss = -8.0240e+02
2023-11-02 14:52:51 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4068, 'NMI': 0.4117, 'ARI': 0.2163, 'accuracy': 0.371, 'precision': 0.3646, 'recall': 0.3687, 'f_measure': 0.3502}}
2023-11-02 14:53:09 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 2.6629===> Reconstruction loss = 19.4287 ===> Dual prediction loss = 0.0052  ===> Contrastive loss = -8.0771e+02 ===> Loss = -8.0550e+02
2023-11-02 14:53:10 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4131, 'NMI': 0.418, 'ARI': 0.2211, 'accuracy': 0.3737, 'precision': 0.3533, 'recall': 0.3718, 'f_measure': 0.3504}}
2023-11-02 14:53:30 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 2.2316===> Reconstruction loss = 18.6029 ===> Dual prediction loss = 0.0045  ===> Contrastive loss = -8.0821e+02 ===> Loss = -8.0612e+02
2023-11-02 14:53:31 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4074, 'NMI': 0.4124, 'ARI': 0.214, 'accuracy': 0.3683, 'precision': 0.3488, 'recall': 0.3666, 'f_measure': 0.3423}}
2023-11-02 14:53:50 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 1.8554===> Reconstruction loss = 17.9299 ===> Dual prediction loss = 0.0029  ===> Contrastive loss = -8.0922e+02 ===> Loss = -8.0724e+02
2023-11-02 14:53:51 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4047, 'NMI': 0.4096, 'ARI': 0.2114, 'accuracy': 0.367, 'precision': 0.3539, 'recall': 0.3645, 'f_measure': 0.3469}}
2023-11-02 14:54:11 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 1.5378===> Reconstruction loss = 17.2247 ===> Dual prediction loss = 0.0022  ===> Contrastive loss = -8.1064e+02 ===> Loss = -8.0876e+02
2023-11-02 14:54:12 - root - INFO: - view_concat {'kmeans': {'AMI': 0.388, 'NMI': 0.3931, 'ARI': 0.1893, 'accuracy': 0.3561, 'precision': 0.3532, 'recall': 0.3562, 'f_measure': 0.3381}}
2023-11-02 14:54:12 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=20, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=128, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=20, bias=True)
    (10): BatchNorm1d(20, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 14:54:12 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=128, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 14:54:12 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 14:54:25 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 3.2510===> Reconstruction loss = 20.2398 ===> Dual prediction loss = 0.0259  ===> Contrastive loss = -8.0596e+02 ===> Loss = -8.0362e+02
2023-11-02 14:54:26 - root - INFO: - view_concat {'kmeans': {'AMI': 0.413, 'NMI': 0.4178, 'ARI': 0.2383, 'accuracy': 0.3991, 'precision': 0.3865, 'recall': 0.3999, 'f_measure': 0.3781}}
2023-11-02 14:54:47 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 2.7409===> Reconstruction loss = 19.3555 ===> Dual prediction loss = 0.0053  ===> Contrastive loss = -8.0763e+02 ===> Loss = -8.0542e+02
2023-11-02 14:54:48 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4104, 'NMI': 0.4153, 'ARI': 0.2296, 'accuracy': 0.3933, 'precision': 0.3818, 'recall': 0.3983, 'f_measure': 0.3735}}
2023-11-02 14:55:08 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 2.2452===> Reconstruction loss = 18.5113 ===> Dual prediction loss = 0.0030  ===> Contrastive loss = -8.0943e+02 ===> Loss = -8.0735e+02
2023-11-02 14:55:08 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4102, 'NMI': 0.4151, 'ARI': 0.2301, 'accuracy': 0.394, 'precision': 0.384, 'recall': 0.3985, 'f_measure': 0.3732}}
2023-11-02 14:55:29 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 1.9269===> Reconstruction loss = 17.7636 ===> Dual prediction loss = 0.0025  ===> Contrastive loss = -8.0993e+02 ===> Loss = -8.0796e+02
2023-11-02 14:55:30 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4112, 'NMI': 0.4161, 'ARI': 0.2306, 'accuracy': 0.3946, 'precision': 0.3823, 'recall': 0.3995, 'f_measure': 0.3742}}
2023-11-02 14:55:50 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 1.6041===> Reconstruction loss = 17.0361 ===> Dual prediction loss = 0.0020  ===> Contrastive loss = -8.1107e+02 ===> Loss = -8.0920e+02
2023-11-02 14:55:50 - root - INFO: - view_concat {'kmeans': {'AMI': 0.4101, 'NMI': 0.415, 'ARI': 0.2313, 'accuracy': 0.3938, 'precision': 0.382, 'recall': 0.3996, 'f_measure': 0.3725}}
2023-11-02 14:55:50 - root - INFO: - --------------------Training over--------------------
2023-11-02 14:55:50 - root - INFO: - ACC:[0.3802, 0.404, 0.39, 0.3561, 0.3938]
2023-11-02 14:55:50 - root - INFO: - NMI:[0.4067, 0.4248, 0.4321, 0.3931, 0.415]
2023-11-02 14:55:50 - root - INFO: - ARI:[0.215, 0.2419, 0.2378, 0.1893, 0.2313]
2023-11-02 14:55:50 - root - INFO: -  ACC 38.48 std 1.63 NMI 41.43 std 1.37 ARI 22.31 std 1.92
root@autodl-container-b72911863c-065c7124:~/2021-CVPR-Completer#
```


### dataset:LandUse_21
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
2023-11-02 14:56:36 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=59, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=64, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=64, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=59, bias=True)
    (10): BatchNorm1d(59, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 14:56:36 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=64, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=64, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 14:56:36 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 14:56:49 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 16.8702===> Reconstruction loss = 8.7381 ===> Dual prediction loss = 0.1021  ===> Contrastive loss = -6.8968e+02 ===> Loss = -6.8712e+02
2023-11-02 14:56:50 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2747, 'NMI': 0.2997, 'ARI': 0.1281, 'accuracy': 0.2295, 'precision': 0.2321, 'recall': 0.2295, 'f_measure': 0.2152}}
2023-11-02 14:57:09 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 15.9567===> Reconstruction loss = 7.9439 ===> Dual prediction loss = 0.0197  ===> Contrastive loss = -6.9260e+02 ===> Loss = -6.9021e+02
2023-11-02 14:57:10 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2929, 'NMI': 0.3172, 'ARI': 0.1375, 'accuracy': 0.241, 'precision': 0.2515, 'recall': 0.241, 'f_measure': 0.2302}}
2023-11-02 14:57:30 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 15.3459===> Reconstruction loss = 7.2656 ===> Dual prediction loss = 0.0144  ===> Contrastive loss = -6.9578e+02 ===> Loss = -6.9352e+02
2023-11-02 14:57:30 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2955, 'NMI': 0.3197, 'ARI': 0.132, 'accuracy': 0.2352, 'precision': 0.2492, 'recall': 0.2352, 'f_measure': 0.2258}}
2023-11-02 14:57:50 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 14.4990===> Reconstruction loss = 6.5730 ===> Dual prediction loss = 0.0165  ===> Contrastive loss = -6.9551e+02 ===> Loss = -6.9340e+02
2023-11-02 14:57:51 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2967, 'NMI': 0.3207, 'ARI': 0.1394, 'accuracy': 0.2386, 'precision': 0.2392, 'recall': 0.2386, 'f_measure': 0.2259}}
2023-11-02 14:58:11 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 14.2221===> Reconstruction loss = 6.0274 ===> Dual prediction loss = 0.0164  ===> Contrastive loss = -6.9606e+02 ===> Loss = -6.9404e+02
2023-11-02 14:58:11 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2976, 'NMI': 0.3215, 'ARI': 0.135, 'accuracy': 0.2405, 'precision': 0.252, 'recall': 0.2405, 'f_measure': 0.2292}}
2023-11-02 14:58:11 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=59, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=64, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=64, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=59, bias=True)
    (10): BatchNorm1d(59, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 14:58:11 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=64, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=64, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 14:58:11 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 14:58:24 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 16.7383===> Reconstruction loss = 8.6969 ===> Dual prediction loss = 0.1160  ===> Contrastive loss = -6.8999e+02 ===> Loss = -6.8744e+02
2023-11-02 14:58:25 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3008, 'NMI': 0.3247, 'ARI': 0.1363, 'accuracy': 0.2705, 'precision': 0.2884, 'recall': 0.2705, 'f_measure': 0.2662}}
2023-11-02 14:58:45 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 16.2016===> Reconstruction loss = 7.9494 ===> Dual prediction loss = 0.0234  ===> Contrastive loss = -6.9277e+02 ===> Loss = -6.9035e+02
2023-11-02 14:58:46 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3033, 'NMI': 0.3269, 'ARI': 0.1476, 'accuracy': 0.2848, 'precision': 0.2865, 'recall': 0.2848, 'f_measure': 0.2748}}
2023-11-02 14:59:03 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 15.5951===> Reconstruction loss = 7.3075 ===> Dual prediction loss = 0.0191  ===> Contrastive loss = -6.9464e+02 ===> Loss = -6.9235e+02
2023-11-02 14:59:03 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2993, 'NMI': 0.3232, 'ARI': 0.1385, 'accuracy': 0.2729, 'precision': 0.2891, 'recall': 0.2729, 'f_measure': 0.2681}}
2023-11-02 14:59:19 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 14.9737===> Reconstruction loss = 6.6343 ===> Dual prediction loss = 0.0160  ===> Contrastive loss = -6.9522e+02 ===> Loss = -6.9306e+02
2023-11-02 14:59:19 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3005, 'NMI': 0.3243, 'ARI': 0.1352, 'accuracy': 0.2686, 'precision': 0.2818, 'recall': 0.2686, 'f_measure': 0.2627}}
2023-11-02 14:59:34 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 14.1739===> Reconstruction loss = 6.0300 ===> Dual prediction loss = 0.0161  ===> Contrastive loss = -6.9648e+02 ===> Loss = -6.9446e+02
2023-11-02 14:59:35 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3089, 'NMI': 0.3324, 'ARI': 0.1364, 'accuracy': 0.2695, 'precision': 0.3014, 'recall': 0.2695, 'f_measure': 0.2753}}
2023-11-02 14:59:35 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=59, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=64, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=64, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=59, bias=True)
    (10): BatchNorm1d(59, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 14:59:35 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=64, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=64, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 14:59:35 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 14:59:45 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 17.0453===> Reconstruction loss = 8.8089 ===> Dual prediction loss = 0.1144  ===> Contrastive loss = -6.9041e+02 ===> Loss = -6.8782e+02
2023-11-02 14:59:46 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2638, 'NMI': 0.2893, 'ARI': 0.1068, 'accuracy': 0.239, 'precision': 0.258, 'recall': 0.239, 'f_measure': 0.2281}}
2023-11-02 15:00:01 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 16.2087===> Reconstruction loss = 8.0304 ===> Dual prediction loss = 0.0202  ===> Contrastive loss = -6.9321e+02 ===> Loss = -6.9078e+02
2023-11-02 15:00:01 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2913, 'NMI': 0.3155, 'ARI': 0.1274, 'accuracy': 0.261, 'precision': 0.2877, 'recall': 0.261, 'f_measure': 0.2608}}
2023-11-02 15:00:17 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 15.3340===> Reconstruction loss = 7.2621 ===> Dual prediction loss = 0.0154  ===> Contrastive loss = -6.9554e+02 ===> Loss = -6.9328e+02
2023-11-02 15:00:17 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2931, 'NMI': 0.3173, 'ARI': 0.1276, 'accuracy': 0.2571, 'precision': 0.2805, 'recall': 0.2571, 'f_measure': 0.2557}}
2023-11-02 15:00:33 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 14.6563===> Reconstruction loss = 6.6330 ===> Dual prediction loss = 0.0161  ===> Contrastive loss = -6.9496e+02 ===> Loss = -6.9283e+02
2023-11-02 15:00:33 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2918, 'NMI': 0.3163, 'ARI': 0.1282, 'accuracy': 0.26, 'precision': 0.2835, 'recall': 0.26, 'f_measure': 0.2541}}
2023-11-02 15:00:49 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 14.0378===> Reconstruction loss = 6.0611 ===> Dual prediction loss = 0.0153  ===> Contrastive loss = -6.9638e+02 ===> Loss = -6.9437e+02
2023-11-02 15:00:49 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2893, 'NMI': 0.314, 'ARI': 0.1264, 'accuracy': 0.2571, 'precision': 0.2725, 'recall': 0.2571, 'f_measure': 0.2472}}
2023-11-02 15:00:49 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=59, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=64, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=64, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=59, bias=True)
    (10): BatchNorm1d(59, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 15:00:49 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=64, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=64, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 15:00:49 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 15:00:59 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 16.8927===> Reconstruction loss = 8.6315 ===> Dual prediction loss = 0.1140  ===> Contrastive loss = -6.8966e+02 ===> Loss = -6.8711e+02
2023-11-02 15:01:00 - root - INFO: - view_concat {'kmeans': {'AMI': 0.298, 'NMI': 0.3219, 'ARI': 0.1194, 'accuracy': 0.251, 'precision': 0.2686, 'recall': 0.251, 'f_measure': 0.2455}}
2023-11-02 15:01:15 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 16.1114===> Reconstruction loss = 7.8441 ===> Dual prediction loss = 0.0185  ===> Contrastive loss = -6.9351e+02 ===> Loss = -6.9111e+02
2023-11-02 15:01:16 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3021, 'NMI': 0.326, 'ARI': 0.1286, 'accuracy': 0.2519, 'precision': 0.2787, 'recall': 0.2519, 'f_measure': 0.2489}}
2023-11-02 15:01:31 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 15.2614===> Reconstruction loss = 7.2145 ===> Dual prediction loss = 0.0206  ===> Contrastive loss = -6.9363e+02 ===> Loss = -6.9138e+02
2023-11-02 15:01:32 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2979, 'NMI': 0.3221, 'ARI': 0.1307, 'accuracy': 0.2505, 'precision': 0.2672, 'recall': 0.2505, 'f_measure': 0.2445}}
2023-11-02 15:01:47 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 14.6574===> Reconstruction loss = 6.6282 ===> Dual prediction loss = 0.0169  ===> Contrastive loss = -6.9559e+02 ===> Loss = -6.9346e+02
2023-11-02 15:01:48 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3009, 'NMI': 0.3246, 'ARI': 0.1341, 'accuracy': 0.25, 'precision': 0.271, 'recall': 0.25, 'f_measure': 0.2479}}
2023-11-02 15:02:03 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 14.0633===> Reconstruction loss = 6.0339 ===> Dual prediction loss = 0.0126  ===> Contrastive loss = -6.9682e+02 ===> Loss = -6.9481e+02
2023-11-02 15:02:03 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2996, 'NMI': 0.324, 'ARI': 0.1291, 'accuracy': 0.2505, 'precision': 0.2628, 'recall': 0.2505, 'f_measure': 0.2374}}
2023-11-02 15:02:03 - root - INFO: - Autoencoder(
  (_encoder): Sequential(
    (0): Linear(in_features=59, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=64, bias=True)
    (10): Softmax(dim=1)
  )
  (_decoder): Sequential(
    (0): Linear(in_features=64, out_features=1024, bias=True)
    (1): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=1024, out_features=1024, bias=True)
    (4): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=1024, out_features=1024, bias=True)
    (7): BatchNorm1d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
    (9): Linear(in_features=1024, out_features=59, bias=True)
    (10): BatchNorm1d(59, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU()
  )
)
2023-11-02 15:02:03 - root - INFO: - Prediction(
  (_encoder): Sequential(
    (0): Linear(in_features=64, out_features=128, bias=True)
    (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=128, out_features=256, bias=True)
    (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=256, out_features=128, bias=True)
    (7): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU()
  )
  (_decoder): Sequential(
    (0): Linear(in_features=128, out_features=256, bias=True)
    (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU()
    (3): Linear(in_features=256, out_features=128, bias=True)
    (4): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU()
    (6): Linear(in_features=128, out_features=64, bias=True)
    (7): Softmax(dim=1)
  )
)
2023-11-02 15:02:03 - root - INFO: - Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    eps: 1e-08
    lr: 0.0001
    maximize: False
    weight_decay: 0
)
2023-11-02 15:02:14 - root - INFO: - Epoch : 100/500 ===> Reconstruction loss = 16.7340===> Reconstruction loss = 8.8048 ===> Dual prediction loss = 0.1167  ===> Contrastive loss = -6.9037e+02 ===> Loss = -6.8781e+02
2023-11-02 15:02:14 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2928, 'NMI': 0.3171, 'ARI': 0.1339, 'accuracy': 0.2467, 'precision': 0.2616, 'recall': 0.2467, 'f_measure': 0.2378}}
2023-11-02 15:02:30 - root - INFO: - Epoch : 200/500 ===> Reconstruction loss = 16.0838===> Reconstruction loss = 7.9961 ===> Dual prediction loss = 0.0216  ===> Contrastive loss = -6.9205e+02 ===> Loss = -6.8964e+02
2023-11-02 15:02:30 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3012, 'NMI': 0.3251, 'ARI': 0.1369, 'accuracy': 0.2543, 'precision': 0.2692, 'recall': 0.2543, 'f_measure': 0.2486}}
2023-11-02 15:02:46 - root - INFO: - Epoch : 300/500 ===> Reconstruction loss = 15.4530===> Reconstruction loss = 7.2951 ===> Dual prediction loss = 0.0195  ===> Contrastive loss = -6.9362e+02 ===> Loss = -6.9135e+02
2023-11-02 15:02:46 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3064, 'NMI': 0.3301, 'ARI': 0.139, 'accuracy': 0.2529, 'precision': 0.2684, 'recall': 0.2529, 'f_measure': 0.2464}}
2023-11-02 15:03:02 - root - INFO: - Epoch : 400/500 ===> Reconstruction loss = 14.8351===> Reconstruction loss = 6.6193 ===> Dual prediction loss = 0.0171  ===> Contrastive loss = -6.9416e+02 ===> Loss = -6.9201e+02
2023-11-02 15:03:02 - root - INFO: - view_concat {'kmeans': {'AMI': 0.2957, 'NMI': 0.3199, 'ARI': 0.1351, 'accuracy': 0.2495, 'precision': 0.2656, 'recall': 0.2495, 'f_measure': 0.2418}}
2023-11-02 15:03:17 - root - INFO: - Epoch : 500/500 ===> Reconstruction loss = 14.1125===> Reconstruction loss = 5.9898 ===> Dual prediction loss = 0.0147  ===> Contrastive loss = -6.9628e+02 ===> Loss = -6.9427e+02
2023-11-02 15:03:18 - root - INFO: - view_concat {'kmeans': {'AMI': 0.3024, 'NMI': 0.3263, 'ARI': 0.1372, 'accuracy': 0.2505, 'precision': 0.2705, 'recall': 0.2505, 'f_measure': 0.244}}
2023-11-02 15:03:18 - root - INFO: - --------------------Training over--------------------
2023-11-02 15:03:18 - root - INFO: - ACC:[0.2405, 0.2695, 0.2571, 0.2505, 0.2505]
2023-11-02 15:03:18 - root - INFO: - NMI:[0.3215, 0.3324, 0.314, 0.324, 0.3263]
2023-11-02 15:03:18 - root - INFO: - ARI:[0.135, 0.1364, 0.1264, 0.1291, 0.1372]
2023-11-02 15:03:18 - root - INFO: -  ACC 25.36 std 0.95 NMI 32.36 std 0.60 ARI 13.28 std 0.43
root@autodl-container-b72911863c-065c7124:~/2021-CVPR-Completer#
```
