```linux
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# git clone https://github.com/XLearning-SCU/2023-CVPR-FCMI
Cloning into '2023-CVPR-FCMI'...
remote: Enumerating objects: 83, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 83 (delta 7), reused 3 (delta 3), pack-reused 69 (from 1)
Receiving objects: 100% (83/83), 2.28 MiB | 3.04 MiB/s, done.
Resolving deltas: 100% (8/8), done.
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# ls
 2023-CVPR-FCMI   Clustering.py   data_loader.py   psp_data_loader.py   readme.md      sure_inference.py   train_NC.sh
'=1.18.2'         __pycache__     models.py        pvp_data_loader.py   run_RMCNC.py   train.sh            utils.py
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# rm 2023-CVPR-FCMI/
rm: cannot remove '2023-CVPR-FCMI/': Is a directory
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# rm -r 2023-CVPR-FCMI/
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# ls
'=1.18.2'   Clustering.py   __pycache__   data_loader.py   models.py   psp_data_loader.py   pvp_data_loader.py   readme.md   run_RMCNC.py   sure_inference.py   train.sh   train_NC.sh   utils.py
root@autodl-container-7c5d4696fb-c54fea2a:~/RMCNC/2024-TKDE-RMCNC-main/RMCNC_main# cd ~
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
CVCL  DIVIDE  Pro-Imp  RMCNC  SMILE  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# git clone https://github.com/XLearning-SCU/2023-CVPR-FCMI
Cloning into '2023-CVPR-FCMI'...
remote: Enumerating objects: 83, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 83 (delta 7), reused 3 (delta 3), pack-reused 69 (from 1)
Receiving objects: 100% (83/83), 2.28 MiB | 2.56 MiB/s, done.
Resolving deltas: 100% (8/8), done.
root@autodl-container-7c5d4696fb-c54fea2a:~# ls
CVCL  DIVIDE  FCMI  Pro-Imp  RMCNC  SMILE  Sure  autodl-pub  autodl-tmp  miniconda3  tf-logs
root@autodl-container-7c5d4696fb-c54fea2a:~# cd FCMI/
root@autodl-container-7c5d4696fb-c54fea2a:~/FCMI# ks
bash: ks: command not found
root@autodl-container-7c5d4696fb-c54fea2a:~/FCMI# ls
AutoLauncher.py  Experiment  Fig2.png       MainLauncher.py  README.md  Tab1.png  TrainHAR.txt   TrainOffice.txt    Utils        loss.py  networkExplicitDecoupleShuffle.py
DataSetMaster    Fig         FigVisual.png  QuickConfig      Results    Temp.txt  TrainMTFL.txt  TrainRevMnist.txt  evaluate.py  main.py  requirements.txt
root@autodl-container-7c5d4696fb-c54fea2a:~/FCMI# python main.py --dataset ReverseMNIST --seed 0  
/root/FCMI/Utils/DirectoryOperator.py:89: SyntaxWarning: invalid escape sequence '\]'
  """
Traceback (most recent call last):
  File "/root/FCMI/main.py", line 4, in <module>
    from DataSetMaster import dataset
  File "/root/FCMI/DataSetMaster/dataset.py", line 9, in <module>
    from MainLauncher import path_operator
  File "/root/FCMI/MainLauncher.py", line 14, in <module>
    path_operator = PathPresettingOperator.PathOperator(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/FCMI/Utils/PathPresettingOperator.py", line 66, in __init__
    raise NotImplementedError("Unknown Gpu '{}'".format(current_gpu))
NotImplementedError: Unknown Gpu 'NVIDIA GeForce RTX 3080 Ti'
root@autodl-container-7c5d4696fb-c54fea2a:~/FCMI# 

```
