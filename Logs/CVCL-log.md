```linux
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL# ls
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL# git clone https://github.com/chenjie20/CVCL/tree/master
Cloning into 'master'...
fatal: repository 'https://github.com/chenjie20/CVCL/tree/master/' not found
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL# git clone https://github.com/chenjie20/CVCL
Cloning into 'CVCL'...
remote: Enumerating objects: 67, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 67 (delta 7), reused 7 (delta 7), pack-reused 57 (from 1)
Receiving objects: 100% (67/67), 264.32 MiB | 13.34 MiB/s, done.
Resolving deltas: 100% (14/14), done.
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL# ls
CVCL
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL# cd CVCL/
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL/CVCL# ls
README.md  dataprocessing.py  datasets  layers.py  loss.py  main.py  metrics.py  models  models.py  requirements.txt  utils.py
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL/CVCL# python main.py --help
usage: main.py [-h] [--load_model LOAD_MODEL] [--save_model SAVE_MODEL] [--db {MSRCv1,MNIST-USPS,COIL20,scene,hand,Fashion,BDGP}] [--seed SEED] [--mse_epochs MSE_EPOCHS] [--con_epochs CON_EPOCHS]
               [-lr LEARNING_RATE] [--weight_decay WEIGHT_DECAY] [--temperature_l TEMPERATURE_L] [--batch_size BATCH_SIZE] [--normalized NORMALIZED] [--gpu GPU]

CVCLNet

options:
  -h, --help            show this help message and exit
  --load_model LOAD_MODEL
                        Testing if True or training.
  --save_model SAVE_MODEL
                        Saving the model after training.
  --db {MSRCv1,MNIST-USPS,COIL20,scene,hand,Fashion,BDGP}
                        dataset name
  --seed SEED           Initializing random seed.
  --mse_epochs MSE_EPOCHS
                        Number of epochs to pre-training.
  --con_epochs CON_EPOCHS
                        Number of epochs to fine-tuning.
  -lr LEARNING_RATE, --learning_rate LEARNING_RATE
                        Initializing learning rate.
  --weight_decay WEIGHT_DECAY
                        Initializing weight decay.
  --temperature_l TEMPERATURE_L
  --batch_size BATCH_SIZE
                        The total number of samples must be evenly divisible by batch_size.
  --normalized NORMALIZED
  --gpu GPU             GPU device idx.
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL/CVCL# python main.py
==========
Args:Namespace(load_model=False, save_model=False, db='MSRCv1', seed=10, mse_epochs=200, con_epochs=100, learning_rate=0.0005, weight_decay=0.0, temperature_l=1.0, batch_size=100, normalized=False, gpu='0')
==========
Pre-training, epoch 0, Loss:0.0302424
Pre-training, epoch 10, Loss:0.0122847
Pre-training, epoch 20, Loss:0.0089409
Pre-training, epoch 30, Loss:0.0065791
Pre-training, epoch 40, Loss:0.0056540
Pre-training, epoch 50, Loss:0.0048400
Pre-training, epoch 60, Loss:0.0042397
Pre-training, epoch 70, Loss:0.0038784
Pre-training, epoch 80, Loss:0.0035452
Pre-training, epoch 90, Loss:0.0032895
Pre-training, epoch 100, Loss:0.0030691
Pre-training, epoch 110, Loss:0.0029663
Pre-training, epoch 120, Loss:0.0028710
Pre-training, epoch 130, Loss:0.0027247
Pre-training, epoch 140, Loss:0.0025988
Pre-training, epoch 150, Loss:0.0025269
Pre-training, epoch 160, Loss:0.0024670
Pre-training, epoch 170, Loss:0.0023518
Pre-training, epoch 180, Loss:0.0023264
Pre-training, epoch 190, Loss:0.0022479
Pre-training, epoch 199, Loss:0.0021532
Pre-training finished.
Total time elapsed: 11.6974s
Contrastive_train, epoch 0 loss:0.0039743
Contrastive_train, epoch 10 loss:-0.0005119
Contrastive_train, epoch 20 loss:-0.0018443
Contrastive_train, epoch 30 loss:-0.0021433
Contrastive_train, epoch 40 loss:-0.0025992
Contrastive_train, epoch 50 loss:-0.0027468
Contrastive_train, epoch 60 loss:-0.0025433
Contrastive_train, epoch 70 loss:-0.0028987
Contrastive_train, epoch 80 loss:-0.0030081
Contrastive_train, epoch 90 loss:-0.0023766
Contrastive_train, epoch 100 loss:-0.0029977
Contrastive_train, epoch 110 loss:-0.0033326
Contrastive_train, epoch 120 loss:-0.0029680
Contrastive_train, epoch 130 loss:-0.0032946
Contrastive_train, epoch 140 loss:-0.0031214
Contrastive_train, epoch 150 loss:-0.0032419
Contrastive_train, epoch 160 loss:-0.0030943
Contrastive_train, epoch 170 loss:-0.0035190
Contrastive_train, epoch 180 loss:-0.0034356
Contrastive_train, epoch 190 loss:-0.0031313
Contrastive_train, epoch 200 loss:-0.0037349
Contrastive_train, epoch 210 loss:-0.0034502
Contrastive_train, epoch 220 loss:-0.0032552
Contrastive_train, epoch 230 loss:-0.0034028
Contrastive_train, epoch 240 loss:-0.0032841
Contrastive_train, epoch 250 loss:-0.0036068
Contrastive_train, epoch 260 loss:-0.0036093
Contrastive_train, epoch 270 loss:-0.0030291
Contrastive_train, epoch 280 loss:-0.0034129
Contrastive_train, epoch 290 loss:-0.0030966
Contrastive_train, epoch 300 loss:-0.0031290
Contrastive_train, epoch 310 loss:-0.0035639
Contrastive_train, epoch 320 loss:-0.0032974
Contrastive_train, epoch 330 loss:-0.0034157
Contrastive_train, epoch 340 loss:-0.0036925
Contrastive_train, epoch 350 loss:-0.0036365
Contrastive_train, epoch 360 loss:-0.0039371
Contrastive_train, epoch 370 loss:-0.0035955
Contrastive_train, epoch 380 loss:-0.0037947
Contrastive_train, epoch 390 loss:-0.0037463
contrastive_train finished.
Total time elapsed: 106.70s
Clustering results on cluster assignments of each view:
ACC1 = 0.9095 NMI1 = 0.8241 PUR1 = 0.9095 ARI1=0.8066
ACC2 = 0.9286 NMI2 = 0.8553 PUR2 = 0.9286 ARI2=0.8422
ACC3 = 0.9238 NMI3 = 0.8448 PUR3 = 0.9238 ARI3=0.8323
ACC4 = 0.9190 NMI4 = 0.8344 PUR4 = 0.9190 ARI4=0.8224
ACC5 = 0.9143 NMI5 = 0.8271 PUR5 = 0.9143 ARI5=0.8121
Clustering results on semantic labels: 210
ACC = 0.9286 NMI = 0.8521 PUR = 0.9286 ARI=0.8426
root@autodl-container-7c5d4696fb-c54fea2a:~/CVCL/CVCL# 

```


```linux
root@autodl-container-534b4e910e-a60bb39b:~# sh a.sh
sh: 0: cannot open a.sh: No such file
root@autodl-container-534b4e910e-a60bb39b:~# cd CVCL
root@autodl-container-534b4e910e-a60bb39b:~/CVCL# cd CVCL/
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# ls
README.md    dataprocessing.py  layers.py  main.py     models     requirements.txt  result_MNIST-USPS.txt  utils.py
__pycache__  datasets           loss.py    metrics.py  models.py  result_BDGP.txt   result_MSRCv1.txt
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# cd models
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL/models# ls
CVCL_pytorch_model_BDGP.part1.rar  CVCL_pytorch_model_COIL20.rar         CVCL_pytorch_model_Fashion.pth           CVCL_pytorch_model_MNIST-USPS.pth    CVCL_pytorch_model_MSRCv1.part3.rar  readme
CVCL_pytorch_model_BDGP.part2.rar  CVCL_pytorch_model_Fashion.part1.rar  CVCL_pytorch_model_MNIST-USPS.part1.rar  CVCL_pytorch_model_MSRCv1.part1.rar  CVCL_pytorch_model_MSRCv1.pth
CVCL_pytorch_model_BDGP.pth        CVCL_pytorch_model_Fashion.part2.rar  CVCL_pytorch_model_MNIST-USPS.part2.rar  CVCL_pytorch_model_MSRCv1.part2.rar  a.sh
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL/models# sh a.sh 
--2024-11-15 16:22:45--  https://www.jiechen.site/downloads/CVCL/models/CVCL_pytorch_model_COIL20.rar
Resolving www.jiechen.site (www.jiechen.site)... 124.223.28.122
Connecting to www.jiechen.site (www.jiechen.site)|124.223.28.122|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 118477669 (113M) [application/octet-stream]
Saving to: ‘CVCL_pytorch_model_COIL20.rar.1’

CVCL_pytorch_model_COIL20.rar.1                  100%[==========================================================================================================>] 112.99M   586KB/s    in 3m 8s   

2024-11-15 16:25:54 (614 KB/s) - ‘CVCL_pytorch_model_COIL20.rar.1’ saved [118477669/118477669]

--2024-11-15 16:25:54--  https://www.jiechen.site/downloads/CVCL/models/CVCL_pytorch_model_hand.rar
Resolving www.jiechen.site (www.jiechen.site)... 124.223.28.122
Connecting to www.jiechen.site (www.jiechen.site)|124.223.28.122|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 81225083 (77M) [application/octet-stream]
Saving to: ‘CVCL_pytorch_model_hand.rar’

CVCL_pytorch_model_hand.rar                      100%[===================================================================================================
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# history 
    1  sh a.sh
    2  cd CVCL
    3  cd CVCL/
    4  ls
    5  cd models
    6  ls
    7  sh a.sh 
    8  cd ..
    9  history 
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# python main.py --help 
usage: main.py [-h] [--load_model LOAD_MODEL] [--save_model SAVE_MODEL] [--db {MSRCv1,MNIST-USPS,COIL20,scene,hand,Fashion,BDGP}] [--seed SEED]
               [--mse_epochs MSE_EPOCHS] [--con_epochs CON_EPOCHS] [-lr LEARNING_RATE] [--weight_decay WEIGHT_DECAY] [--temperature_l TEMPERATURE_L]
               [--batch_size BATCH_SIZE] [--normalized NORMALIZED] [--gpu GPU]

CVCLNet

options:
  -h, --help            show this help message and exit
  --load_model LOAD_MODEL
                        Testing if True or training.
  --save_model SAVE_MODEL
                        Saving the model after training.
  --db {MSRCv1,MNIST-USPS,COIL20,scene,hand,Fashion,BDGP}
                        dataset name
  --seed SEED           Initializing random seed.
  --mse_epochs MSE_EPOCHS
                        Number of epochs to pre-training.
  --con_epochs CON_EPOCHS
                        Number of epochs to fine-tuning.
  -lr LEARNING_RATE, --learning_rate LEARNING_RATE
                        Initializing learning rate.
  --weight_decay WEIGHT_DECAY
                        Initializing weight decay.
  --temperature_l TEMPERATURE_L
  --batch_size BATCH_SIZE
                        The total number of samples must be evenly divisible by batch_size.
  --normalized NORMALIZED
  --gpu GPU             GPU device idx.
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# python main.py --db scene
==========
Args:Namespace(load_model=True, save_model=False, db='scene', seed=10, mse_epochs=200, con_epochs=100, learning_rate=0.0005, weight_decay=0.0, temperature_l=1.0, batch_size=100, normalized=False, gpu='0')
==========
Clustering results on cluster assignments of each view:
ACC1 = 0.4256 NMI1 = 0.3998 PUR1 = 0.4513 ARI1=0.2431
ACC2 = 0.4513 NMI2 = 0.4314 PUR2 = 0.4765 ARI2=0.2673
ACC3 = 0.4285 NMI3 = 0.3894 PUR3 = 0.4551 ARI3=0.2424
Clustering results on semantic labels: 4485
ACC = 0.4459 NMI = 0.4217 PUR = 0.4736 ARI=0.2643
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# python main.py --db MSRCv1
==========
Args:Namespace(load_model=True, save_model=False, db='MSRCv1', seed=10, mse_epochs=200, con_epochs=100, learning_rate=0.0005, weight_decay=0.0, temperature_l=1.0, batch_size=100, normalized=False, gpu='0')
==========
Clustering results on cluster assignments of each view:
ACC1 = 0.9333 NMI1 = 0.8697 PUR1 = 0.9333 ARI1=0.8502
ACC2 = 0.9667 NMI2 = 0.9283 PUR2 = 0.9667 ARI2=0.9232
ACC3 = 0.9619 NMI3 = 0.9175 PUR3 = 0.9619 ARI3=0.9116
ACC4 = 0.9571 NMI4 = 0.9119 PUR4 = 0.9571 ARI4=0.9034
ACC5 = 0.9619 NMI5 = 0.9209 PUR5 = 0.9619 ARI5=0.9122
Clustering results on semantic labels: 210
ACC = 0.9762 NMI = 0.9498 PUR = 0.9762 ARI=0.9453
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# python main.py --db MNIST-USPS
==========
Args:Namespace(load_model=True, save_model=False, db='MNIST-USPS', seed=10, mse_epochs=200, con_epochs=100, learning_rate=0.0005, weight_decay=0.0, temperature_l=1.0, batch_size=100, normalized=False, gpu='0')
==========
Clustering results on cluster assignments of each view:
ACC1 = 0.9918 NMI1 = 0.9762 PUR1 = 0.9918 ARI1=0.9819
ACC2 = 0.9966 NMI2 = 0.9899 PUR2 = 0.9966 ARI2=0.9925
Clustering results on semantic labels: 5000
ACC = 0.9970 NMI = 0.9912 PUR = 0.9970 ARI=0.9933
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# python main.py --db COIL20
==========
Args:Namespace(load_model=True, save_model=False, db='COIL20', seed=10, mse_epochs=200, con_epochs=100, learning_rate=0.0005, weight_decay=0.0, temperature_l=1.0, batch_size=100, normalized=False, gpu='0')
==========
Traceback (most recent call last):
  File "/root/CVCL/CVCL/main.py", line 173, in <module>
    state_dict = torch.load('./models/CVCL_pytorch_model_%s.pth' % args.db)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/serialization.py", line 1319, in load
    with _open_file_like(f, "rb") as opened_file:
         ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/serialization.py", line 659, in _open_file_like
    return _open_file(name_or_buffer, mode)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/serialization.py", line 640, in __init__
    super().__init__(open(name, mode))
                     ^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: './models/CVCL_pytorch_model_COIL20.pth'
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# python main.py --db hand
==========
Args:Namespace(load_model=True, save_model=False, db='hand', seed=10, mse_epochs=200, con_epochs=100, learning_rate=0.0005, weight_decay=0.0, temperature_l=1.0, batch_size=100, normalized=False, gpu='0')
==========
Clustering results on cluster assignments of each view:
ACC1 = 0.9720 NMI1 = 0.9355 PUR1 = 0.9720 ARI1=0.9391
ACC2 = 0.9500 NMI2 = 0.8944 PUR2 = 0.9500 ARI2=0.8932
ACC3 = 0.9710 NMI3 = 0.9370 PUR3 = 0.9710 ARI3=0.9373
ACC4 = 0.8945 NMI4 = 0.8806 PUR4 = 0.8945 ARI4=0.8339
ACC5 = 0.9705 NMI5 = 0.9333 PUR5 = 0.9705 ARI5=0.9360
ACC6 = 0.7755 NMI6 = 0.7465 PUR6 = 0.7755 ARI6=0.6626
Clustering results on semantic labels: 2000
ACC = 0.9735 NMI = 0.9405 PUR = 0.9735 ARI=0.9424
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# python main.py --db Fashion
==========
Args:Namespace(load_model=True, save_model=False, db='Fashion', seed=10, mse_epochs=200, con_epochs=100, learning_rate=0.0005, weight_decay=0.0, temperature_l=1.0, batch_size=100, normalized=False, gpu='0')
==========
Clustering results on cluster assignments of each view:
ACC1 = 0.9907 NMI1 = 0.9748 PUR1 = 0.9907 ARI1=0.9796
ACC2 = 0.9901 NMI2 = 0.9733 PUR2 = 0.9901 ARI2=0.9782
ACC3 = 0.9895 NMI3 = 0.9714 PUR3 = 0.9895 ARI3=0.9770
Clustering results on semantic labels: 10000
ACC = 0.9931 NMI = 0.9821 PUR = 0.9931 ARI=0.9848
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# python main.py --db BDGP
==========
Args:Namespace(load_model=True, save_model=False, db='BDGP', seed=10, mse_epochs=200, con_epochs=100, learning_rate=0.0005, weight_decay=0.0, temperature_l=1.0, batch_size=100, normalized=False, gpu='0')
==========
Clustering results on cluster assignments of each view:
ACC1 = 0.9864 NMI1 = 0.9529 PUR1 = 0.9864 ARI1=0.9664
ACC2 = 0.9804 NMI2 = 0.9487 PUR2 = 0.9804 ARI2=0.9521
Clustering results on semantic labels: 2500
ACC = 0.9920 NMI = 0.9729 PUR = 0.9920 ARI=0.9801
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL# cd models
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL/models# unrar x CVCL_pytorch_model_COIL20.rar .

UNRAR 6.11 beta 1 freeware      Copyright (c) 1993-2022 Alexander Roshal


Extracting from CVCL_pytorch_model_COIL20.rar

Extracting  ./CVCL_pytorch_model_COIL20.pth                          100%
CVCL_pytorch_model_COIL20.pth - checksum error
Unexpected end of archive
Total errors: 2
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL/models# unrar x CVCL_pytorch_model_COIL20.rar .

UNRAR 6.11 beta 1 freeware      Copyright (c) 1993-2022 Alexander Roshal


Extracting from CVCL_pytorch_model_COIL20.rar

Extracting  ./CVCL_pytorch_model_COIL20.pth                          100%
CVCL_pytorch_model_COIL20.pth - checksum error
Unexpected end of archive
Total errors: 2
root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL/models# wget https://www.jiechen.site/downloads/CVCL/models/CVCL_pytorch_model_COIL20.rar
--2024-11-15 16:40:40--  https://www.jiechen.site/downloads/CVCL/models/CVCL_pytorch_model_COIL20.rar
Resolving www.jiechen.site (www.jiechen.site)... 124.223.28.122
Connecting to www.jiechen.site (www.jiechen.site)|124.223.28.122|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 118477669 (113M) [application/octet-stream]
Saving to: ‘CVCL_pytorch_model_COIL20.rar’

CVCL_pytorch_model_COIL20.rar       100%[=================================================================>] 112.99M   669KB/s    in 3m 8s   

2024-11-15 16:43:48 (616 KB/s) - ‘CVCL_pytorch_model_COIL20.rar’ saved [118477669/118477669]

root@autodl-container-534b4e910e-a60bb39b:~/CVCL/CVCL/models# 

```
