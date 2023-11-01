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
