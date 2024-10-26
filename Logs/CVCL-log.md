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
