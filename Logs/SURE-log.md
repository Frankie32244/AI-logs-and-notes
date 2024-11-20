如果报这种错误的话，改一下run.py 


错误代码:
```linux
if not os.path.exists('./log/'):
    os.mkdir("./log/")
    if not os.path.exists('./log/' + str(data_name[args.data]) + '/'):
        os.mkdir('./log/' + str(data_name[args.data]) + '/')
path = os.path.join("./log/" + str(data_name[args.data]) + "/" + 'time=' + time
                     .strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

```

正确代码:
```linux
import os
import time

# 创建日志文件路径
if not os.path.exists('./log/'):
    os.makedirs("./log/")  # 使用 os.makedirs 递归创建目录
log_dir = './log/' + str(data_name[args.data])
if not os.path.exists(log_dir):
    os.makedirs(log_dir)  # 确保日志子目录存在

# 替换时间戳中的非法字符
timestamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
path = os.path.join(log_dir, f'time={timestamp}')

# 设置日志文件
log_format = '%(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_format, datefmt='%m/%d %I:%M:%S %p')
fh = logging.FileHandler(path + '.txt')
fh.setFormatter(logging.Formatter(log_format))
logging.getLogger().addHandler(fh)

logging.info("******** Training begin ********")
```

### dataset : scene15    align = 0.5
```linux
******** Training begin ********
=======> Train epoch: 0/80
margin = 5
dist: P = 2.36, N = 2.46, TN = 2.46, FN = 2.47; ncl_loss: 3.99, ver_loss:4.4, time = 1.59 s
Clustering: acc=0.1866, nmi=0.1182, ari=0.0422
=======> Train epoch: 1/80
dist: P = 3.43, N = 3.51, TN = 3.51, FN = 3.48; ncl_loss: 1.65, ver_loss:0.53, time = 2.74 s
Clustering: acc=0.3556, nmi=0.3614, ari=0.2063
=======> Train epoch: 2/80
dist: P = 3.67, N = 3.93, TN = 3.93, FN = 3.8; ncl_loss: 1.13, ver_loss:0.2, time = 1.8 s
Clustering: acc=0.3204, nmi=0.348, ari=0.1957
=======> Train epoch: 3/80
dist: P = 3.79, N = 4.15, TN = 4.16, FN = 3.97; ncl_loss: 0.9, ver_loss:0.18, time = 2.2 s
Clustering: acc=0.3184, nmi=0.3402, ari=0.1841
=======> Train epoch: 4/80
dist: P = 3.82, N = 4.33, TN = 4.35, FN = 4.08; ncl_loss: 0.73, ver_loss:0.17, time = 2.31 s
Clustering: acc=0.3052, nmi=0.3427, ari=0.1812
=======> Train epoch: 5/80
dist: P = 3.91, N = 4.51, TN = 4.54, FN = 4.21; ncl_loss: 0.6, ver_loss:0.17, time = 2.11 s
Clustering: acc=0.295, nmi=0.3263, ari=0.1684
=======> Train epoch: 6/80
dist: P = 4.01, N = 4.65, TN = 4.68, FN = 4.32; ncl_loss: 0.51, ver_loss:0.16, time = 2.64 s
Clustering: acc=0.299, nmi=0.3264, ari=0.1587
=======> Train epoch: 7/80
dist: P = 4.08, N = 4.76, TN = 4.79, FN = 4.39; ncl_loss: 0.46, ver_loss:0.14, time = 2.37 s
Clustering: acc=0.3258, nmi=0.3426, ari=0.1808
=======> Train epoch: 8/80
dist: P = 4.11, N = 4.84, TN = 4.87, FN = 4.46; ncl_loss: 0.42, ver_loss:0.13, time = 2.2 s
Clustering: acc=0.3139, nmi=0.3285, ari=0.1734
=======> Train epoch: 9/80
dist: P = 4.12, N = 4.91, TN = 4.94, FN = 4.49; ncl_loss: 0.4, ver_loss:0.13, time = 2.08 s
Clustering: acc=0.3043, nmi=0.3372, ari=0.1622
=======> Train epoch: 10/80
dist: P = 4.13, N = 4.96, TN = 5.0, FN = 4.53; ncl_loss: 0.38, ver_loss:0.12, time = 2.41 s
Clustering: acc=0.3222, nmi=0.3314, ari=0.1752
=======> Train epoch: 11/80
******* neg_dist_mean >= 1.0 * margin, start using fine loss at epoch: 12 *******
dist: P = 4.12, N = 5.01, TN = 5.05, FN = 4.55; ncl_loss: 0.37, ver_loss:0.11, time = 2.19 s
Clustering: acc=0.311, nmi=0.3253, ari=0.1594
=======> Train epoch: 12/80
dist: P = 3.95, N = 5.01, TN = 5.05, FN = 4.46; ncl_loss: 0.34, ver_loss:0.1, time = 2.89 s
Clustering: acc=0.3151, nmi=0.3321, ari=0.1686
=======> Train epoch: 13/80
dist: P = 3.8, N = 5.02, TN = 5.07, FN = 4.4; ncl_loss: 0.34, ver_loss:0.1, time = 2.42 s
Clustering: acc=0.3206, nmi=0.3428, ari=0.1896
=======> Train epoch: 14/80
dist: P = 3.7, N = 5.06, TN = 5.11, FN = 4.37; ncl_loss: 0.33, ver_loss:0.1, time = 2.67 s
Clustering: acc=0.3222, nmi=0.3497, ari=0.1963
=======> Train epoch: 15/80
dist: P = 3.5, N = 5.1, TN = 5.15, FN = 4.3; ncl_loss: 0.32, ver_loss:0.1, time = 2.26 s
Clustering: acc=0.359, nmi=0.3625, ari=0.2044
=======> Train epoch: 16/80
dist: P = 3.27, N = 5.15, TN = 5.21, FN = 4.25; ncl_loss: 0.31, ver_loss:0.09, time = 2.43 s
Clustering: acc=0.3547, nmi=0.3658, ari=0.2143
=======> Train epoch: 17/80
dist: P = 3.09, N = 5.2, TN = 5.28, FN = 4.22; ncl_loss: 0.3, ver_loss:0.09, time = 2.83 s
Clustering: acc=0.3581, nmi=0.3695, ari=0.2163
=======> Train epoch: 18/80
dist: P = 2.82, N = 5.24, TN = 5.33, FN = 4.11; ncl_loss: 0.29, ver_loss:0.09, time = 2.34 s
Clustering: acc=0.3521, nmi=0.3651, ari=0.2127
=======> Train epoch: 19/80
dist: P = 2.55, N = 5.29, TN = 5.38, FN = 4.06; ncl_loss: 0.27, ver_loss:0.09, time = 2.86 s
Clustering: acc=0.3703, nmi=0.3818, ari=0.2302
=======> Train epoch: 20/80
dist: P = 2.31, N = 5.34, TN = 5.44, FN = 4.01; ncl_loss: 0.26, ver_loss:0.09, time = 2.36 s
Clustering: acc=0.3815, nmi=0.3951, ari=0.2378
=======> Train epoch: 21/80
dist: P = 2.12, N = 5.4, TN = 5.5, FN = 4.01; ncl_loss: 0.24, ver_loss:0.09, time = 2.33 s
Clustering: acc=0.3764, nmi=0.3976, ari=0.2366
=======> Train epoch: 22/80
dist: P = 2.04, N = 5.44, TN = 5.55, FN = 4.04; ncl_loss: 0.23, ver_loss:0.09, time = 2.47 s
Clustering: acc=0.3862, nmi=0.3997, ari=0.2441
=======> Train epoch: 23/80
dist: P = 1.99, N = 5.49, TN = 5.59, FN = 4.06; ncl_loss: 0.22, ver_loss:0.09, time = 2.66 s
Clustering: acc=0.3871, nmi=0.393, ari=0.2445
=======> Train epoch: 24/80
dist: P = 1.95, N = 5.53, TN = 5.63, FN = 4.1; ncl_loss: 0.21, ver_loss:0.09, time = 2.67 s
Clustering: acc=0.3877, nmi=0.4043, ari=0.2485
=======> Train epoch: 25/80
dist: P = 1.92, N = 5.56, TN = 5.67, FN = 4.08; ncl_loss: 0.21, ver_loss:0.09, time = 2.39 s
Clustering: acc=0.3953, nmi=0.4124, ari=0.2546
=======> Train epoch: 26/80
dist: P = 1.86, N = 5.61, TN = 5.72, FN = 4.11; ncl_loss: 0.2, ver_loss:0.09, time = 2.39 s
Clustering: acc=0.3931, nmi=0.4095, ari=0.2522
=======> Train epoch: 27/80
dist: P = 1.88, N = 5.65, TN = 5.76, FN = 4.17; ncl_loss: 0.19, ver_loss:0.09, time = 2.25 s
Clustering: acc=0.394, nmi=0.404, ari=0.2488
=======> Train epoch: 28/80
dist: P = 1.85, N = 5.69, TN = 5.8, FN = 4.18; ncl_loss: 0.19, ver_loss:0.09, time = 2.39 s
Clustering: acc=0.3895, nmi=0.4082, ari=0.2519
=======> Train epoch: 29/80
dist: P = 1.82, N = 5.72, TN = 5.83, FN = 4.21; ncl_loss: 0.18, ver_loss:0.09, time = 2.25 s
Clustering: acc=0.3958, nmi=0.3965, ari=0.2437
=======> Train epoch: 30/80
dist: P = 1.82, N = 5.75, TN = 5.86, FN = 4.26; ncl_loss: 0.18, ver_loss:0.08, time = 2.21 s
Clustering: acc=0.3873, nmi=0.4011, ari=0.24
=======> Train epoch: 31/80
dist: P = 1.82, N = 5.8, TN = 5.91, FN = 4.28; ncl_loss: 0.18, ver_loss:0.08, time = 2.38 s
Clustering: acc=0.3951, nmi=0.4111, ari=0.2475
=======> Train epoch: 32/80
dist: P = 1.81, N = 5.82, TN = 5.93, FN = 4.3; ncl_loss: 0.17, ver_loss:0.08, time = 2.21 s
Clustering: acc=0.4045, nmi=0.4071, ari=0.2511
=======> Train epoch: 33/80
dist: P = 1.78, N = 5.85, TN = 5.97, FN = 4.32; ncl_loss: 0.17, ver_loss:0.08, time = 2.24 s
Clustering: acc=0.3971, nmi=0.411, ari=0.2477
=======> Train epoch: 34/80
dist: P = 1.78, N = 5.88, TN = 6.0, FN = 4.35; ncl_loss: 0.16, ver_loss:0.08, time = 2.31 s
Clustering: acc=0.3871, nmi=0.3943, ari=0.2378
=======> Train epoch: 35/80
dist: P = 1.75, N = 5.92, TN = 6.04, FN = 4.39; ncl_loss: 0.16, ver_loss:0.08, time = 2.25 s
Clustering: acc=0.3926, nmi=0.4036, ari=0.2446
=======> Train epoch: 36/80
dist: P = 1.74, N = 5.95, TN = 6.06, FN = 4.43; ncl_loss: 0.15, ver_loss:0.08, time = 2.18 s
Clustering: acc=0.3996, nmi=0.4032, ari=0.2462
=======> Train epoch: 37/80
dist: P = 1.73, N = 5.99, TN = 6.1, FN = 4.45; ncl_loss: 0.15, ver_loss:0.08, time = 2.38 s
Clustering: acc=0.398, nmi=0.4035, ari=0.2448
=======> Train epoch: 38/80
dist: P = 1.72, N = 6.04, TN = 6.15, FN = 4.47; ncl_loss: 0.15, ver_loss:0.08, time = 2.26 s
Clustering: acc=0.3933, nmi=0.4012, ari=0.2433
=======> Train epoch: 39/80
dist: P = 1.7, N = 6.05, TN = 6.17, FN = 4.48; ncl_loss: 0.14, ver_loss:0.08, time = 2.37 s
Clustering: acc=0.4027, nmi=0.4081, ari=0.25
=======> Train epoch: 40/80
dist: P = 1.69, N = 6.08, TN = 6.19, FN = 4.51; ncl_loss: 0.14, ver_loss:0.08, time = 3.09 s
Clustering: acc=0.4045, nmi=0.4097, ari=0.2494
=======> Train epoch: 41/80
dist: P = 1.71, N = 6.13, TN = 6.24, FN = 4.56; ncl_loss: 0.14, ver_loss:0.08, time = 2.64 s
Clustering: acc=0.3873, nmi=0.3952, ari=0.2375
=======> Train epoch: 42/80
dist: P = 1.68, N = 6.15, TN = 6.26, FN = 4.58; ncl_loss: 0.14, ver_loss:0.08, time = 2.24 s
Clustering: acc=0.396, nmi=0.4065, ari=0.2458
=======> Train epoch: 43/80
dist: P = 1.68, N = 6.17, TN = 6.29, FN = 4.58; ncl_loss: 0.13, ver_loss:0.07, time = 2.26 s
Clustering: acc=0.3958, nmi=0.3984, ari=0.244
=======> Train epoch: 44/80
dist: P = 1.66, N = 6.2, TN = 6.32, FN = 4.62; ncl_loss: 0.13, ver_loss:0.07, time = 2.32 s
Clustering: acc=0.3911, nmi=0.4023, ari=0.2421
=======> Train epoch: 45/80
dist: P = 1.69, N = 6.23, TN = 6.35, FN = 4.66; ncl_loss: 0.13, ver_loss:0.07, time = 2.49 s
Clustering: acc=0.3793, nmi=0.4028, ari=0.2391
=======> Train epoch: 46/80
dist: P = 1.65, N = 6.25, TN = 6.37, FN = 4.64; ncl_loss: 0.13, ver_loss:0.07, time = 2.49 s
Clustering: acc=0.3991, nmi=0.4031, ari=0.2461
=======> Train epoch: 47/80
dist: P = 1.66, N = 6.28, TN = 6.4, FN = 4.7; ncl_loss: 0.13, ver_loss:0.07, time = 2.27 s
Clustering: acc=0.3824, nmi=0.4033, ari=0.2414
=======> Train epoch: 48/80
dist: P = 1.64, N = 6.31, TN = 6.43, FN = 4.7; ncl_loss: 0.12, ver_loss:0.07, time = 2.29 s
Clustering: acc=0.396, nmi=0.4128, ari=0.2487
=======> Train epoch: 49/80
dist: P = 1.65, N = 6.33, TN = 6.46, FN = 4.7; ncl_loss: 0.12, ver_loss:0.07, time = 2.37 s
Clustering: acc=0.39, nmi=0.4035, ari=0.2448
=======> Train epoch: 50/80
dist: P = 1.63, N = 6.37, TN = 6.49, FN = 4.73; ncl_loss: 0.12, ver_loss:0.07, time = 2.13 s
Clustering: acc=0.3835, nmi=0.3999, ari=0.2375
=======> Train epoch: 51/80
dist: P = 1.62, N = 6.39, TN = 6.51, FN = 4.78; ncl_loss: 0.12, ver_loss:0.07, time = 2.33 s
Clustering: acc=0.3964, nmi=0.3936, ari=0.2406
=======> Train epoch: 52/80
dist: P = 1.62, N = 6.42, TN = 6.54, FN = 4.79; ncl_loss: 0.12, ver_loss:0.07, time = 2.95 s
Clustering: acc=0.3828, nmi=0.4041, ari=0.2409
=======> Train epoch: 53/80
dist: P = 1.61, N = 6.43, TN = 6.56, FN = 4.81; ncl_loss: 0.12, ver_loss:0.07, time = 2.13 s
Clustering: acc=0.3906, nmi=0.4011, ari=0.2431
=======> Train epoch: 54/80
dist: P = 1.6, N = 6.47, TN = 6.59, FN = 4.83; ncl_loss: 0.11, ver_loss:0.07, time = 2.57 s
Clustering: acc=0.3831, nmi=0.4001, ari=0.2395
=======> Train epoch: 55/80
dist: P = 1.6, N = 6.49, TN = 6.62, FN = 4.84; ncl_loss: 0.11, ver_loss:0.07, time = 2.42 s
Clustering: acc=0.3877, nmi=0.3961, ari=0.2366
=======> Train epoch: 56/80
dist: P = 1.62, N = 6.49, TN = 6.61, FN = 4.84; ncl_loss: 0.11, ver_loss:0.06, time = 2.28 s
Clustering: acc=0.3909, nmi=0.4016, ari=0.2406
=======> Train epoch: 57/80
dist: P = 1.58, N = 6.53, TN = 6.65, FN = 4.89; ncl_loss: 0.11, ver_loss:0.07, time = 2.24 s
Clustering: acc=0.3942, nmi=0.4095, ari=0.2498
=======> Train epoch: 58/80
dist: P = 1.58, N = 6.55, TN = 6.67, FN = 4.88; ncl_loss: 0.11, ver_loss:0.06, time = 2.33 s
Clustering: acc=0.3933, nmi=0.4052, ari=0.2452
=======> Train epoch: 59/80
dist: P = 1.56, N = 6.57, TN = 6.69, FN = 4.91; ncl_loss: 0.11, ver_loss:0.06, time = 2.33 s
Clustering: acc=0.3909, nmi=0.406, ari=0.246
=======> Train epoch: 60/80
dist: P = 1.56, N = 6.6, TN = 6.72, FN = 4.94; ncl_loss: 0.11, ver_loss:0.06, time = 2.47 s
Clustering: acc=0.3884, nmi=0.3986, ari=0.2413
=======> Train epoch: 61/80
dist: P = 1.59, N = 6.62, TN = 6.74, FN = 4.95; ncl_loss: 0.11, ver_loss:0.06, time = 2.5 s
Clustering: acc=0.3931, nmi=0.3946, ari=0.2376
=======> Train epoch: 62/80
dist: P = 1.55, N = 6.62, TN = 6.75, FN = 4.95; ncl_loss: 0.1, ver_loss:0.06, time = 2.32 s
Clustering: acc=0.3949, nmi=0.3956, ari=0.2375
=======> Train epoch: 63/80
dist: P = 1.55, N = 6.65, TN = 6.78, FN = 4.98; ncl_loss: 0.1, ver_loss:0.06, time = 2.42 s
Clustering: acc=0.3915, nmi=0.4047, ari=0.2436
=======> Train epoch: 64/80
dist: P = 1.55, N = 6.68, TN = 6.8, FN = 5.01; ncl_loss: 0.1, ver_loss:0.06, time = 2.41 s
Clustering: acc=0.3949, nmi=0.4101, ari=0.2476
=======> Train epoch: 65/80
dist: P = 1.52, N = 6.7, TN = 6.82, FN = 5.02; ncl_loss: 0.1, ver_loss:0.06, time = 2.3 s
Clustering: acc=0.3922, nmi=0.4064, ari=0.2428
=======> Train epoch: 66/80
dist: P = 1.55, N = 6.71, TN = 6.83, FN = 5.01; ncl_loss: 0.1, ver_loss:0.06, time = 2.35 s
Clustering: acc=0.3864, nmi=0.3923, ari=0.2411
=======> Train epoch: 67/80
dist: P = 1.51, N = 6.73, TN = 6.85, FN = 5.04; ncl_loss: 0.1, ver_loss:0.06, time = 2.06 s
Clustering: acc=0.402, nmi=0.4034, ari=0.2457
=======> Train epoch: 68/80
dist: P = 1.53, N = 6.75, TN = 6.88, FN = 5.05; ncl_loss: 0.1, ver_loss:0.06, time = 2.74 s
Clustering: acc=0.3922, nmi=0.3966, ari=0.2375
=======> Train epoch: 69/80
dist: P = 1.51, N = 6.76, TN = 6.89, FN = 5.06; ncl_loss: 0.09, ver_loss:0.06, time = 2.5 s
Clustering: acc=0.3955, nmi=0.4055, ari=0.2444
=======> Train epoch: 70/80
dist: P = 1.48, N = 6.79, TN = 6.92, FN = 5.09; ncl_loss: 0.09, ver_loss:0.06, time = 3.1 s
Clustering: acc=0.3987, nmi=0.3999, ari=0.244
=======> Train epoch: 71/80
dist: P = 1.5, N = 6.8, TN = 6.92, FN = 5.09; ncl_loss: 0.09, ver_loss:0.06, time = 1.84 s
Clustering: acc=0.3973, nmi=0.4042, ari=0.244
=======> Train epoch: 72/80
dist: P = 1.49, N = 6.82, TN = 6.95, FN = 5.11; ncl_loss: 0.09, ver_loss:0.06, time = 1.84 s
Clustering: acc=0.396, nmi=0.4082, ari=0.2448
=======> Train epoch: 73/80
dist: P = 1.46, N = 6.85, TN = 6.97, FN = 5.13; ncl_loss: 0.09, ver_loss:0.06, time = 2.37 s
Clustering: acc=0.3906, nmi=0.4035, ari=0.2408
=======> Train epoch: 74/80
dist: P = 1.47, N = 6.85, TN = 6.98, FN = 5.15; ncl_loss: 0.09, ver_loss:0.06, time = 2.36 s
Clustering: acc=0.3902, nmi=0.3959, ari=0.2403
=======> Train epoch: 75/80
dist: P = 1.45, N = 6.88, TN = 7.0, FN = 5.15; ncl_loss: 0.09, ver_loss:0.06, time = 2.28 s
Clustering: acc=0.3822, nmi=0.3983, ari=0.2374
=======> Train epoch: 76/80
dist: P = 1.44, N = 6.88, TN = 7.01, FN = 5.15; ncl_loss: 0.09, ver_loss:0.06, time = 2.55 s
Clustering: acc=0.3862, nmi=0.396, ari=0.2385
=======> Train epoch: 77/80
dist: P = 1.46, N = 6.89, TN = 7.02, FN = 5.17; ncl_loss: 0.09, ver_loss:0.06, time = 2.34 s
Clustering: acc=0.3851, nmi=0.4023, ari=0.241
=======> Train epoch: 78/80
dist: P = 1.44, N = 6.91, TN = 7.04, FN = 5.17; ncl_loss: 0.08, ver_loss:0.06, time = 2.25 s
Clustering: acc=0.3891, nmi=0.3976, ari=0.2394
=======> Train epoch: 79/80
dist: P = 1.44, N = 6.93, TN = 7.06, FN = 5.21; ncl_loss: 0.09, ver_loss:0.06, time = 3.0 s
Clustering: acc=0.3819, nmi=0.3975, ari=0.2348
=======> Train epoch: 80/80
dist: P = 1.44, N = 6.94, TN = 7.07, FN = 5.2; ncl_loss: 0.08, ver_loss:0.06, time = 1.87 s
Clustering: acc=0.3906, nmi=0.4062, ari=0.2439
******** End, training time = 192.31 s ********
```

### dataset : scene15    align = 1.0
```linux
******** Training begin ********
=======> Train epoch: 0/80
margin = 5
dist: P = 2.37, N = 2.45, TN = 2.45, FN = 2.46; ncl_loss: 4.02, ver_loss:4.41, time = 2.68 s
Clustering: acc=0.1955, nmi=0.1282, ari=0.0442
=======> Train epoch: 1/80
dist: P = 3.57, N = 3.7, TN = 3.71, FN = 3.62; ncl_loss: 1.42, ver_loss:0.35, time = 4.43 s
Clustering: acc=0.3021, nmi=0.3446, ari=0.1684
=======> Train epoch: 2/80
dist: P = 3.68, N = 4.24, TN = 4.27, FN = 3.9; ncl_loss: 0.81, ver_loss:0.15, time = 3.86 s
Clustering: acc=0.3351, nmi=0.3455, ari=0.1771
=======> Train epoch: 3/80
dist: P = 3.88, N = 4.59, TN = 4.62, FN = 4.17; ncl_loss: 0.56, ver_loss:0.13, time = 4.13 s
Clustering: acc=0.3001, nmi=0.3198, ari=0.1621
=======> Train epoch: 4/80
dist: P = 4.08, N = 4.81, TN = 4.84, FN = 4.38; ncl_loss: 0.45, ver_loss:0.12, time = 3.97 s
Clustering: acc=0.3128, nmi=0.3157, ari=0.1666
=======> Train epoch: 5/80
dist: P = 4.17, N = 4.95, TN = 4.98, FN = 4.5; ncl_loss: 0.4, ver_loss:0.11, time = 4.06 s
Clustering: acc=0.3041, nmi=0.3113, ari=0.1547
=======> Train epoch: 6/80
******* neg_dist_mean >= 1.0 * margin, start using fine loss at epoch: 7 *******
dist: P = 4.15, N = 5.04, TN = 5.08, FN = 4.54; ncl_loss: 0.37, ver_loss:0.1, time = 3.73 s
Clustering: acc=0.3231, nmi=0.3346, ari=0.1799
=======> Train epoch: 7/80
dist: P = 3.64, N = 5.07, TN = 5.13, FN = 4.3; ncl_loss: 0.33, ver_loss:0.09, time = 3.85 s
Clustering: acc=0.3449, nmi=0.3554, ari=0.1975
=======> Train epoch: 8/80
dist: P = 3.11, N = 5.16, TN = 5.23, FN = 4.13; ncl_loss: 0.31, ver_loss:0.09, time = 4.16 s
Clustering: acc=0.3628, nmi=0.3866, ari=0.2265
=======> Train epoch: 9/80
dist: P = 2.67, N = 5.24, TN = 5.34, FN = 4.03; ncl_loss: 0.28, ver_loss:0.09, time = 3.75 s
Clustering: acc=0.363, nmi=0.3794, ari=0.2204
=======> Train epoch: 10/80
dist: P = 2.36, N = 5.35, TN = 5.44, FN = 4.05; ncl_loss: 0.26, ver_loss:0.09, time = 3.86 s
Clustering: acc=0.3654, nmi=0.3949, ari=0.2275
=======> Train epoch: 11/80
dist: P = 2.21, N = 5.43, TN = 5.53, FN = 4.07; ncl_loss: 0.25, ver_loss:0.09, time = 4.14 s
Clustering: acc=0.3724, nmi=0.3916, ari=0.2309
=======> Train epoch: 12/80
dist: P = 2.11, N = 5.51, TN = 5.62, FN = 4.11; ncl_loss: 0.23, ver_loss:0.09, time = 4.04 s
Clustering: acc=0.3855, nmi=0.4072, ari=0.246
=======> Train epoch: 13/80
dist: P = 2.04, N = 5.6, TN = 5.71, FN = 4.18; ncl_loss: 0.22, ver_loss:0.09, time = 4.15 s
Clustering: acc=0.3828, nmi=0.4065, ari=0.2402
=======> Train epoch: 14/80
dist: P = 2.01, N = 5.68, TN = 5.79, FN = 4.25; ncl_loss: 0.21, ver_loss:0.08, time = 3.88 s
Clustering: acc=0.3935, nmi=0.4154, ari=0.245
=======> Train epoch: 15/80
dist: P = 2.0, N = 5.78, TN = 5.89, FN = 4.31; ncl_loss: 0.2, ver_loss:0.08, time = 3.55 s
Clustering: acc=0.3902, nmi=0.4171, ari=0.2335
=======> Train epoch: 16/80
dist: P = 1.98, N = 5.85, TN = 5.96, FN = 4.39; ncl_loss: 0.2, ver_loss:0.08, time = 4.23 s
Clustering: acc=0.4049, nmi=0.4146, ari=0.2398
=======> Train epoch: 17/80
dist: P = 1.96, N = 5.94, TN = 6.05, FN = 4.42; ncl_loss: 0.19, ver_loss:0.08, time = 3.84 s
Clustering: acc=0.419, nmi=0.4175, ari=0.244
=======> Train epoch: 18/80
dist: P = 1.95, N = 6.01, TN = 6.13, FN = 4.48; ncl_loss: 0.18, ver_loss:0.08, time = 4.03 s
Clustering: acc=0.4185, nmi=0.4249, ari=0.246
=======> Train epoch: 19/80
dist: P = 1.97, N = 6.09, TN = 6.2, FN = 4.56; ncl_loss: 0.18, ver_loss:0.07, time = 4.28 s
Clustering: acc=0.4165, nmi=0.4249, ari=0.2472
=======> Train epoch: 20/80
dist: P = 1.93, N = 6.16, TN = 6.28, FN = 4.62; ncl_loss: 0.17, ver_loss:0.07, time = 3.78 s
Clustering: acc=0.4192, nmi=0.411, ari=0.2393
=======> Train epoch: 21/80
dist: P = 1.92, N = 6.23, TN = 6.34, FN = 4.67; ncl_loss: 0.17, ver_loss:0.07, time = 4.06 s
Clustering: acc=0.4232, nmi=0.4172, ari=0.2448
=======> Train epoch: 22/80
dist: P = 1.94, N = 6.3, TN = 6.42, FN = 4.71; ncl_loss: 0.17, ver_loss:0.07, time = 4.18 s
Clustering: acc=0.425, nmi=0.4131, ari=0.2454
=======> Train epoch: 23/80
dist: P = 1.93, N = 6.37, TN = 6.49, FN = 4.79; ncl_loss: 0.16, ver_loss:0.07, time = 3.94 s
Clustering: acc=0.4239, nmi=0.4178, ari=0.2426
=======> Train epoch: 24/80
dist: P = 1.94, N = 6.43, TN = 6.55, FN = 4.83; ncl_loss: 0.16, ver_loss:0.07, time = 4.03 s
Clustering: acc=0.4268, nmi=0.4125, ari=0.2444
=======> Train epoch: 25/80
dist: P = 1.94, N = 6.49, TN = 6.61, FN = 4.87; ncl_loss: 0.15, ver_loss:0.07, time = 4.16 s
Clustering: acc=0.4252, nmi=0.431, ari=0.2535
=======> Train epoch: 26/80
dist: P = 1.93, N = 6.55, TN = 6.68, FN = 4.91; ncl_loss: 0.15, ver_loss:0.06, time = 3.77 s
Clustering: acc=0.4174, nmi=0.4172, ari=0.2445
=======> Train epoch: 27/80
dist: P = 1.92, N = 6.61, TN = 6.73, FN = 4.94; ncl_loss: 0.15, ver_loss:0.06, time = 4.01 s
Clustering: acc=0.4192, nmi=0.4218, ari=0.2501
=======> Train epoch: 28/80
dist: P = 1.92, N = 6.67, TN = 6.79, FN = 5.0; ncl_loss: 0.15, ver_loss:0.06, time = 4.08 s
Clustering: acc=0.4169, nmi=0.4181, ari=0.2456
=======> Train epoch: 29/80
dist: P = 1.91, N = 6.71, TN = 6.84, FN = 5.03; ncl_loss: 0.14, ver_loss:0.06, time = 4.0 s
Clustering: acc=0.4156, nmi=0.4202, ari=0.2474
=======> Train epoch: 30/80
dist: P = 1.9, N = 6.78, TN = 6.9, FN = 5.07; ncl_loss: 0.14, ver_loss:0.06, time = 4.13 s
Clustering: acc=0.4272, nmi=0.4282, ari=0.2518
=======> Train epoch: 31/80
dist: P = 1.91, N = 6.82, TN = 6.95, FN = 5.11; ncl_loss: 0.14, ver_loss:0.06, time = 4.3 s
Clustering: acc=0.4216, nmi=0.4179, ari=0.2476
=======> Train epoch: 32/80
dist: P = 1.92, N = 6.88, TN = 7.01, FN = 5.15; ncl_loss: 0.14, ver_loss:0.06, time = 3.88 s
Clustering: acc=0.4154, nmi=0.4244, ari=0.2477
=======> Train epoch: 33/80
dist: P = 1.92, N = 6.92, TN = 7.06, FN = 5.17; ncl_loss: 0.14, ver_loss:0.06, time = 4.12 s
Clustering: acc=0.4381, nmi=0.4232, ari=0.2525
=======> Train epoch: 34/80
dist: P = 1.92, N = 6.96, TN = 7.09, FN = 5.19; ncl_loss: 0.13, ver_loss:0.06, time = 4.31 s
Clustering: acc=0.4355, nmi=0.4255, ari=0.2563
=======> Train epoch: 35/80
dist: P = 1.89, N = 7.02, TN = 7.15, FN = 5.24; ncl_loss: 0.13, ver_loss:0.05, time = 4.02 s
Clustering: acc=0.4123, nmi=0.4248, ari=0.2484
=======> Train epoch: 36/80
dist: P = 1.88, N = 7.06, TN = 7.19, FN = 5.27; ncl_loss: 0.13, ver_loss:0.05, time = 4.13 s
Clustering: acc=0.4192, nmi=0.435, ari=0.2558
=======> Train epoch: 37/80
dist: P = 1.88, N = 7.1, TN = 7.24, FN = 5.29; ncl_loss: 0.13, ver_loss:0.05, time = 4.35 s
Clustering: acc=0.4256, nmi=0.4345, ari=0.2599
=======> Train epoch: 38/80
dist: P = 1.87, N = 7.14, TN = 7.27, FN = 5.32; ncl_loss: 0.13, ver_loss:0.05, time = 3.82 s
Clustering: acc=0.4225, nmi=0.4284, ari=0.2515
=======> Train epoch: 39/80
dist: P = 1.88, N = 7.17, TN = 7.31, FN = 5.34; ncl_loss: 0.13, ver_loss:0.05, time = 4.03 s
Clustering: acc=0.4201, nmi=0.4257, ari=0.2493
=======> Train epoch: 40/80
dist: P = 1.88, N = 7.21, TN = 7.35, FN = 5.36; ncl_loss: 0.12, ver_loss:0.05, time = 4.21 s
Clustering: acc=0.4334, nmi=0.424, ari=0.2549
=======> Train epoch: 41/80
dist: P = 1.85, N = 7.24, TN = 7.38, FN = 5.4; ncl_loss: 0.12, ver_loss:0.05, time = 3.9 s
Clustering: acc=0.4448, nmi=0.4287, ari=0.2594
=======> Train epoch: 42/80
dist: P = 1.86, N = 7.28, TN = 7.41, FN = 5.42; ncl_loss: 0.12, ver_loss:0.05, time = 4.01 s
Clustering: acc=0.4196, nmi=0.431, ari=0.2547
=======> Train epoch: 43/80
dist: P = 1.84, N = 7.32, TN = 7.46, FN = 5.43; ncl_loss: 0.12, ver_loss:0.05, time = 4.2 s
Clustering: acc=0.4201, nmi=0.4338, ari=0.2565
=======> Train epoch: 44/80
dist: P = 1.83, N = 7.35, TN = 7.49, FN = 5.46; ncl_loss: 0.12, ver_loss:0.05, time = 3.78 s
Clustering: acc=0.4225, nmi=0.4268, ari=0.2499
=======> Train epoch: 45/80
dist: P = 1.84, N = 7.39, TN = 7.53, FN = 5.49; ncl_loss: 0.12, ver_loss:0.05, time = 4.12 s
Clustering: acc=0.4169, nmi=0.4292, ari=0.2519
=======> Train epoch: 46/80
dist: P = 1.82, N = 7.4, TN = 7.55, FN = 5.5; ncl_loss: 0.11, ver_loss:0.05, time = 4.27 s
Clustering: acc=0.4163, nmi=0.4217, ari=0.2453
=======> Train epoch: 47/80
dist: P = 1.83, N = 7.44, TN = 7.58, FN = 5.53; ncl_loss: 0.11, ver_loss:0.05, time = 3.96 s
Clustering: acc=0.4268, nmi=0.4389, ari=0.2599
=======> Train epoch: 48/80
dist: P = 1.82, N = 7.47, TN = 7.61, FN = 5.53; ncl_loss: 0.11, ver_loss:0.05, time = 4.15 s
Clustering: acc=0.4152, nmi=0.4356, ari=0.2557
=======> Train epoch: 49/80
dist: P = 1.8, N = 7.5, TN = 7.64, FN = 5.57; ncl_loss: 0.11, ver_loss:0.05, time = 4.24 s
Clustering: acc=0.4223, nmi=0.4356, ari=0.2553
=======> Train epoch: 50/80
dist: P = 1.81, N = 7.52, TN = 7.67, FN = 5.58; ncl_loss: 0.11, ver_loss:0.05, time = 3.87 s
Clustering: acc=0.4444, nmi=0.4354, ari=0.2615
=======> Train epoch: 51/80
dist: P = 1.8, N = 7.56, TN = 7.71, FN = 5.61; ncl_loss: 0.11, ver_loss:0.05, time = 4.2 s
Clustering: acc=0.4433, nmi=0.4362, ari=0.2616
=======> Train epoch: 52/80
dist: P = 1.78, N = 7.59, TN = 7.74, FN = 5.63; ncl_loss: 0.11, ver_loss:0.05, time = 4.3 s
Clustering: acc=0.4482, nmi=0.4367, ari=0.2646
=======> Train epoch: 53/80
dist: P = 1.78, N = 7.6, TN = 7.74, FN = 5.62; ncl_loss: 0.11, ver_loss:0.04, time = 3.98 s
Clustering: acc=0.4245, nmi=0.4384, ari=0.2588
=======> Train epoch: 54/80
dist: P = 1.76, N = 7.62, TN = 7.77, FN = 5.66; ncl_loss: 0.1, ver_loss:0.04, time = 4.07 s
Clustering: acc=0.441, nmi=0.4436, ari=0.266
=======> Train epoch: 55/80
dist: P = 1.76, N = 7.65, TN = 7.8, FN = 5.66; ncl_loss: 0.1, ver_loss:0.04, time = 4.34 s
Clustering: acc=0.4256, nmi=0.4331, ari=0.2539
=======> Train epoch: 56/80
dist: P = 1.74, N = 7.68, TN = 7.82, FN = 5.68; ncl_loss: 0.1, ver_loss:0.04, time = 3.85 s
Clustering: acc=0.4464, nmi=0.4393, ari=0.266
=======> Train epoch: 57/80
dist: P = 1.76, N = 7.68, TN = 7.83, FN = 5.7; ncl_loss: 0.1, ver_loss:0.04, time = 4.12 s
Clustering: acc=0.4372, nmi=0.4293, ari=0.2546
=======> Train epoch: 58/80
dist: P = 1.73, N = 7.71, TN = 7.86, FN = 5.7; ncl_loss: 0.1, ver_loss:0.04, time = 4.33 s
Clustering: acc=0.4459, nmi=0.4354, ari=0.2617
=======> Train epoch: 59/80
dist: P = 1.75, N = 7.72, TN = 7.87, FN = 5.73; ncl_loss: 0.1, ver_loss:0.04, time = 4.33 s
Clustering: acc=0.4201, nmi=0.4272, ari=0.247
=======> Train epoch: 60/80
dist: P = 1.74, N = 7.73, TN = 7.88, FN = 5.73; ncl_loss: 0.1, ver_loss:0.04, time = 4.44 s
Clustering: acc=0.4395, nmi=0.4306, ari=0.2585
=======> Train epoch: 61/80
dist: P = 1.72, N = 7.75, TN = 7.9, FN = 5.75; ncl_loss: 0.1, ver_loss:0.04, time = 4.58 s
Clustering: acc=0.4263, nmi=0.4333, ari=0.2531
=======> Train epoch: 62/80
dist: P = 1.71, N = 7.77, TN = 7.92, FN = 5.76; ncl_loss: 0.1, ver_loss:0.04, time = 4.21 s
Clustering: acc=0.4491, nmi=0.4458, ari=0.2693
=======> Train epoch: 63/80
dist: P = 1.71, N = 7.78, TN = 7.93, FN = 5.77; ncl_loss: 0.1, ver_loss:0.04, time = 4.2 s
Clustering: acc=0.4464, nmi=0.4362, ari=0.2632
=======> Train epoch: 64/80
dist: P = 1.7, N = 7.8, TN = 7.95, FN = 5.79; ncl_loss: 0.09, ver_loss:0.04, time = 4.69 s
Clustering: acc=0.4508, nmi=0.4371, ari=0.2659
=======> Train epoch: 65/80
dist: P = 1.72, N = 7.81, TN = 7.96, FN = 5.79; ncl_loss: 0.1, ver_loss:0.04, time = 3.93 s
Clustering: acc=0.4256, nmi=0.4329, ari=0.2574
=======> Train epoch: 66/80
dist: P = 1.69, N = 7.83, TN = 7.98, FN = 5.8; ncl_loss: 0.09, ver_loss:0.04, time = 3.57 s
Clustering: acc=0.4426, nmi=0.44, ari=0.2638
=======> Train epoch: 67/80
dist: P = 1.68, N = 7.85, TN = 8.0, FN = 5.81; ncl_loss: 0.09, ver_loss:0.04, time = 3.72 s
Clustering: acc=0.414, nmi=0.4337, ari=0.2531
=======> Train epoch: 68/80
dist: P = 1.66, N = 7.87, TN = 8.02, FN = 5.84; ncl_loss: 0.09, ver_loss:0.04, time = 3.79 s
Clustering: acc=0.4433, nmi=0.4386, ari=0.2624
=======> Train epoch: 69/80
dist: P = 1.65, N = 7.88, TN = 8.03, FN = 5.83; ncl_loss: 0.09, ver_loss:0.04, time = 4.13 s
Clustering: acc=0.4357, nmi=0.4441, ari=0.2667
=======> Train epoch: 70/80
dist: P = 1.66, N = 7.9, TN = 8.05, FN = 5.85; ncl_loss: 0.09, ver_loss:0.04, time = 4.3 s
Clustering: acc=0.4412, nmi=0.4371, ari=0.2622
=======> Train epoch: 71/80
dist: P = 1.65, N = 7.91, TN = 8.06, FN = 5.87; ncl_loss: 0.09, ver_loss:0.04, time = 3.93 s
Clustering: acc=0.4455, nmi=0.4397, ari=0.2611
=======> Train epoch: 72/80
dist: P = 1.65, N = 7.92, TN = 8.07, FN = 5.86; ncl_loss: 0.09, ver_loss:0.04, time = 4.18 s
Clustering: acc=0.4241, nmi=0.4379, ari=0.2546
=======> Train epoch: 73/80
dist: P = 1.62, N = 7.93, TN = 8.09, FN = 5.89; ncl_loss: 0.08, ver_loss:0.04, time = 4.36 s
Clustering: acc=0.4419, nmi=0.433, ari=0.2601
=======> Train epoch: 74/80
dist: P = 1.62, N = 7.95, TN = 8.11, FN = 5.9; ncl_loss: 0.08, ver_loss:0.04, time = 3.94 s
Clustering: acc=0.4281, nmi=0.4306, ari=0.2502
=======> Train epoch: 75/80
dist: P = 1.63, N = 7.96, TN = 8.12, FN = 5.92; ncl_loss: 0.08, ver_loss:0.04, time = 4.18 s
Clustering: acc=0.4285, nmi=0.4324, ari=0.2575
=======> Train epoch: 76/80
dist: P = 1.61, N = 7.99, TN = 8.14, FN = 5.93; ncl_loss: 0.08, ver_loss:0.04, time = 4.32 s
Clustering: acc=0.4279, nmi=0.4371, ari=0.2594
=======> Train epoch: 77/80
dist: P = 1.6, N = 7.99, TN = 8.15, FN = 5.93; ncl_loss: 0.08, ver_loss:0.04, time = 3.99 s
Clustering: acc=0.4163, nmi=0.4302, ari=0.2508
=======> Train epoch: 78/80
dist: P = 1.61, N = 7.99, TN = 8.15, FN = 5.94; ncl_loss: 0.08, ver_loss:0.04, time = 4.15 s
Clustering: acc=0.4435, nmi=0.4391, ari=0.2613
=======> Train epoch: 79/80
dist: P = 1.59, N = 8.0, TN = 8.16, FN = 5.95; ncl_loss: 0.08, ver_loss:0.04, time = 4.28 s
Clustering: acc=0.4491, nmi=0.4363, ari=0.2637
=======> Train epoch: 80/80
dist: P = 1.59, N = 8.02, TN = 8.18, FN = 5.96; ncl_loss: 0.08, ver_loss:0.04, time = 3.91 s
Clustering: acc=0.4297, nmi=0.4374, ari=0.2549
******** End, training time = 328.73 s ********
```
