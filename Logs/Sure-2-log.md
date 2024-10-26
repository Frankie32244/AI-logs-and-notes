```linux

root@autodl-container-7c5d4696fb-c54fea2a:~/Sure/2022-TPAMI-SURE-main# ls
Clustering.py  README.md  __pycache__  data_loader.py  datasets  models.py  psp_data_loader.py  pvp_data_loader.py  run.py  sure_inference.py  utils.py
root@autodl-container-7c5d4696fb-c54fea2a:~/Sure/2022-TPAMI-SURE-main# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=2, aligned_prop=0.5, complete_prop=0.5)
==========
Traceback (most recent call last):
  File "/root/Sure/2022-TPAMI-SURE-main/run.py", line 255, in <module>
    main()
  File "/root/Sure/2022-TPAMI-SURE-main/run.py", line 184, in main
    train_pair_loader, all_loader, divide_seed = loader(args.batch_size, args.neg_prop, args.aligned_prop,
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/Sure/2022-TPAMI-SURE-main/data_loader.py", line 232, in loader
    divide_seed, mask = load_data(dataset, neg_prop, aligned_prop, complete_prop, is_noise)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/Sure/2022-TPAMI-SURE-main/data_loader.py", line 58, in load_data
    train_idx, test_idx = TT_split(len(label), 1 - aligned_prop, divide_seed)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/Sure/2022-TPAMI-SURE-main/utils.py", line 28, in TT_split
    train_num = np.ceil((1-test_prop) * n_all).astype(np.int)
                                                      ^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/numpy/__init__.py", line 324, in __getattr__
    raise AttributeError(__former_attrs__[attr])
AttributeError: module 'numpy' has no attribute 'int'.
`np.int` was a deprecated alias for the builtin `int`. To avoid this error in existing code, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations. Did you mean: 'inf'?
root@autodl-container-7c5d4696fb-c54fea2a:~/Sure/2022-TPAMI-SURE-main# python run.py --data 0 --gpu 0 --settings 2 --aligned-prop 0.5 --complete-prop 0.5
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=2, aligned_prop=0.5, complete_prop=0.5)
==========
noise rate of the constructed neg. pairs is  0.07
----------------------Training with noisy_negatives----------------------
******** Training begin ********
=======> Train epoch: 0/80
margin = 5
dist: P = 2.37, N = 2.45, TN = 2.45, FN = 2.49; ncl_loss: 4.04, ver_loss:4.45, time = 2.43 s
/root/Sure/2022-TPAMI-SURE-main/sure_inference.py:171: UserWarning: This overload of addmm_ is deprecated:
        addmm_(Number beta, Number alpha, Tensor mat1, Tensor mat2)
Consider using one of the following signatures instead:
        addmm_(Tensor mat1, Tensor mat2, *, Number beta, Number alpha) (Triggered internally at ../torch/csrc/utils/python_arg_parser.cpp:1578.)
  dist.addmm_(1, -2, x, y.t())
Traceback (most recent call last):
  File "/root/Sure/2022-TPAMI-SURE-main/run.py", line 255, in <module>
    main()
  File "/root/Sure/2022-TPAMI-SURE-main/run.py", line 237, in main
    v0, v1, gt_label = both_infer(model, device, all_loader, args.settings)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/Sure/2022-TPAMI-SURE-main/sure_inference.py", line 118, in both_infer
    idx0 = col_idx[i, :][M[col_idx[i, :], i]]  # idx for view 0 to sort and find the non-missing neighbors
                         ~^^^^^^^^^^^^^^^^^^
RuntimeError: indices should be either on cpu or on the same device as the indexed tensor (cpu)
root@autodl-container-7c5d4696fb-c54fea2a:~/Sure/2022-TPAMI-SURE-main# python run.py --data 0 --gpu 0 --settings 0 --aligned-prop 0.5 --complete-prop 1.0
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=0, aligned_prop=0.5, complete_prop=1.0)
==========
noise rate of the constructed neg. pairs is  0.07
----------------------Training with noisy_negatives----------------------
******** Training begin ********
=======> Train epoch: 0/80
margin = 5
dist: P = 2.36, N = 2.45, TN = 2.45, FN = 2.44; ncl_loss: 4.06, ver_loss:4.41, time = 1.64 s
/root/Sure/2022-TPAMI-SURE-main/sure_inference.py:171: UserWarning: This overload of addmm_ is deprecated:
        addmm_(Number beta, Number alpha, Tensor mat1, Tensor mat2)
Consider using one of the following signatures instead:
        addmm_(Tensor mat1, Tensor mat2, *, Number beta, Number alpha) (Triggered internally at ../torch/csrc/utils/python_arg_parser.cpp:1578.)
  dist.addmm_(1, -2, x, y.t())
Clustering: acc=0.1857, nmi=0.1213, ari=0.0423
=======> Train epoch: 1/80
dist: P = 3.38, N = 3.49, TN = 3.5, FN = 3.39; ncl_loss: 1.68, ver_loss:0.53, time = 2.67 s
Clustering: acc=0.2836, nmi=0.3082, ari=0.1519
=======> Train epoch: 2/80
dist: P = 3.58, N = 3.93, TN = 3.95, FN = 3.72; ncl_loss: 1.1, ver_loss:0.2, time = 2.24 s
Clustering: acc=0.2814, nmi=0.3137, ari=0.1543
=======> Train epoch: 3/80
dist: P = 3.67, N = 4.17, TN = 4.19, FN = 3.85; ncl_loss: 0.87, ver_loss:0.18, time = 2.53 s
Clustering: acc=0.2892, nmi=0.3112, ari=0.1569
=======> Train epoch: 4/80
dist: P = 3.78, N = 4.36, TN = 4.39, FN = 4.02; ncl_loss: 0.71, ver_loss:0.16, time = 2.39 s
Clustering: acc=0.2941, nmi=0.3101, ari=0.1598
=======> Train epoch: 5/80
dist: P = 3.88, N = 4.52, TN = 4.55, FN = 4.15; ncl_loss: 0.59, ver_loss:0.15, time = 2.18 s
Clustering: acc=0.3003, nmi=0.3082, ari=0.1683
=======> Train epoch: 6/80
dist: P = 3.96, N = 4.66, TN = 4.68, FN = 4.26; ncl_loss: 0.51, ver_loss:0.14, time = 1.74 s
Clustering: acc=0.2718, nmi=0.2991, ari=0.1543
=======> Train epoch: 7/80
dist: P = 4.02, N = 4.77, TN = 4.8, FN = 4.35; ncl_loss: 0.45, ver_loss:0.14, time = 2.03 s
Clustering: acc=0.2742, nmi=0.3113, ari=0.1456
=======> Train epoch: 8/80
dist: P = 4.09, N = 4.86, TN = 4.9, FN = 4.43; ncl_loss: 0.42, ver_loss:0.13, time = 1.81 s
Clustering: acc=0.2798, nmi=0.3087, ari=0.1451
=======> Train epoch: 9/80
dist: P = 4.13, N = 4.94, TN = 4.98, FN = 4.49; ncl_loss: 0.4, ver_loss:0.12, time = 1.95 s
Clustering: acc=0.2912, nmi=0.311, ari=0.1485
=======> Train epoch: 10/80
******* neg_dist_mean >= 1.0 * margin, start using fine loss at epoch: 11 *******
dist: P = 4.14, N = 5.0, TN = 5.04, FN = 4.53; ncl_loss: 0.39, ver_loss:0.11, time = 1.91 s
Clustering: acc=0.3019, nmi=0.3194, ari=0.1565
=======> Train epoch: 11/80
dist: P = 3.97, N = 5.01, TN = 5.05, FN = 4.45; ncl_loss: 0.36, ver_loss:0.11, time = 1.73 s
Clustering: acc=0.3001, nmi=0.334, ari=0.1659
=======> Train epoch: 12/80
dist: P = 3.78, N = 5.03, TN = 5.08, FN = 4.37; ncl_loss: 0.35, ver_loss:0.1, time = 1.98 s
Clustering: acc=0.2979, nmi=0.318, ari=0.1611
=======> Train epoch: 13/80
dist: P = 3.62, N = 5.05, TN = 5.1, FN = 4.33; ncl_loss: 0.34, ver_loss:0.09, time = 1.73 s
Clustering: acc=0.3229, nmi=0.3472, ari=0.1783
=======> Train epoch: 14/80
dist: P = 3.43, N = 5.08, TN = 5.14, FN = 4.27; ncl_loss: 0.33, ver_loss:0.09, time = 1.76 s
Clustering: acc=0.3378, nmi=0.3636, ari=0.1959
=======> Train epoch: 15/80
dist: P = 3.21, N = 5.13, TN = 5.19, FN = 4.21; ncl_loss: 0.31, ver_loss:0.09, time = 1.95 s
Clustering: acc=0.3398, nmi=0.3744, ari=0.2087
=======> Train epoch: 16/80
dist: P = 3.01, N = 5.18, TN = 5.26, FN = 4.18; ncl_loss: 0.3, ver_loss:0.09, time = 1.67 s
Clustering: acc=0.3608, nmi=0.3796, ari=0.2114
=======> Train epoch: 17/80
dist: P = 2.85, N = 5.23, TN = 5.31, FN = 4.15; ncl_loss: 0.29, ver_loss:0.09, time = 2.38 s
Clustering: acc=0.3712, nmi=0.3852, ari=0.2269
=======> Train epoch: 18/80
dist: P = 2.76, N = 5.27, TN = 5.35, FN = 4.15; ncl_loss: 0.28, ver_loss:0.09, time = 2.09 s
Clustering: acc=0.381, nmi=0.3845, ari=0.2221
=======> Train epoch: 19/80
dist: P = 2.71, N = 5.32, TN = 5.4, FN = 4.18; ncl_loss: 0.27, ver_loss:0.09, time = 1.89 s
Clustering: acc=0.3775, nmi=0.3923, ari=0.2226
=======> Train epoch: 20/80
dist: P = 2.66, N = 5.35, TN = 5.44, FN = 4.21; ncl_loss: 0.26, ver_loss:0.09, time = 2.04 s
Clustering: acc=0.3688, nmi=0.382, ari=0.2242
=======> Train epoch: 21/80
dist: P = 2.64, N = 5.38, TN = 5.47, FN = 4.23; ncl_loss: 0.25, ver_loss:0.09, time = 1.95 s
Clustering: acc=0.3703, nmi=0.3901, ari=0.2302
=======> Train epoch: 22/80
dist: P = 2.6, N = 5.42, TN = 5.5, FN = 4.23; ncl_loss: 0.25, ver_loss:0.08, time = 2.03 s
Clustering: acc=0.3708, nmi=0.3939, ari=0.2265
=======> Train epoch: 23/80
dist: P = 2.57, N = 5.44, TN = 5.53, FN = 4.25; ncl_loss: 0.24, ver_loss:0.08, time = 1.98 s
Clustering: acc=0.3875, nmi=0.3972, ari=0.232
=======> Train epoch: 24/80
dist: P = 2.48, N = 5.47, TN = 5.56, FN = 4.24; ncl_loss: 0.23, ver_loss:0.08, time = 1.91 s
Clustering: acc=0.3721, nmi=0.3904, ari=0.2274
=======> Train epoch: 25/80
dist: P = 2.39, N = 5.49, TN = 5.58, FN = 4.25; ncl_loss: 0.23, ver_loss:0.08, time = 1.87 s
Clustering: acc=0.3788, nmi=0.3935, ari=0.2267
=======> Train epoch: 26/80
dist: P = 2.3, N = 5.53, TN = 5.63, FN = 4.23; ncl_loss: 0.22, ver_loss:0.08, time = 2.07 s
Clustering: acc=0.3775, nmi=0.3993, ari=0.2317
=======> Train epoch: 27/80
dist: P = 2.21, N = 5.56, TN = 5.66, FN = 4.23; ncl_loss: 0.21, ver_loss:0.08, time = 1.7 s
Clustering: acc=0.3779, nmi=0.4011, ari=0.2329
=======> Train epoch: 28/80
dist: P = 2.08, N = 5.61, TN = 5.71, FN = 4.21; ncl_loss: 0.21, ver_loss:0.08, time = 1.89 s
Clustering: acc=0.3793, nmi=0.3971, ari=0.2279
=======> Train epoch: 29/80
dist: P = 1.97, N = 5.66, TN = 5.77, FN = 4.22; ncl_loss: 0.2, ver_loss:0.08, time = 2.02 s
Clustering: acc=0.3868, nmi=0.4111, ari=0.2424
=======> Train epoch: 30/80
dist: P = 1.92, N = 5.71, TN = 5.82, FN = 4.24; ncl_loss: 0.19, ver_loss:0.08, time = 1.85 s
Clustering: acc=0.3699, nmi=0.4031, ari=0.2361
=======> Train epoch: 31/80
dist: P = 1.88, N = 5.77, TN = 5.88, FN = 4.29; ncl_loss: 0.19, ver_loss:0.08, time = 2.01 s
Clustering: acc=0.3795, nmi=0.4033, ari=0.2351
=======> Train epoch: 32/80
dist: P = 1.88, N = 5.81, TN = 5.92, FN = 4.35; ncl_loss: 0.18, ver_loss:0.08, time = 1.99 s
Clustering: acc=0.3978, nmi=0.4063, ari=0.2428
=======> Train epoch: 33/80
dist: P = 1.85, N = 5.85, TN = 5.96, FN = 4.37; ncl_loss: 0.17, ver_loss:0.08, time = 1.77 s
Clustering: acc=0.386, nmi=0.4077, ari=0.2383
=======> Train epoch: 34/80
dist: P = 1.84, N = 5.89, TN = 6.0, FN = 4.42; ncl_loss: 0.17, ver_loss:0.08, time = 2.08 s
Clustering: acc=0.3882, nmi=0.4031, ari=0.2355
=======> Train epoch: 35/80
dist: P = 1.84, N = 5.94, TN = 6.05, FN = 4.45; ncl_loss: 0.17, ver_loss:0.08, time = 1.81 s
Clustering: acc=0.3886, nmi=0.4112, ari=0.2419
=======> Train epoch: 36/80
dist: P = 1.85, N = 5.97, TN = 6.08, FN = 4.49; ncl_loss: 0.17, ver_loss:0.08, time = 1.93 s
Clustering: acc=0.3955, nmi=0.4083, ari=0.2388
=======> Train epoch: 37/80
dist: P = 1.82, N = 6.01, TN = 6.12, FN = 4.54; ncl_loss: 0.16, ver_loss:0.07, time = 1.99 s
Clustering: acc=0.3855, nmi=0.4028, ari=0.2358
=======> Train epoch: 38/80
dist: P = 1.8, N = 6.04, TN = 6.15, FN = 4.56; ncl_loss: 0.15, ver_loss:0.07, time = 1.88 s
Clustering: acc=0.3505, nmi=0.3885, ari=0.2237
=======> Train epoch: 39/80
dist: P = 1.82, N = 6.09, TN = 6.2, FN = 4.61; ncl_loss: 0.15, ver_loss:0.07, time = 1.88 s
Clustering: acc=0.3942, nmi=0.4028, ari=0.2383
=======> Train epoch: 40/80
dist: P = 1.81, N = 6.12, TN = 6.23, FN = 4.61; ncl_loss: 0.15, ver_loss:0.07, time = 2.04 s
Clustering: acc=0.3918, nmi=0.4098, ari=0.2383
=======> Train epoch: 41/80
dist: P = 1.82, N = 6.15, TN = 6.26, FN = 4.65; ncl_loss: 0.15, ver_loss:0.07, time = 2.18 s
Clustering: acc=0.3804, nmi=0.3969, ari=0.2288
=======> Train epoch: 42/80
dist: P = 1.77, N = 6.18, TN = 6.29, FN = 4.67; ncl_loss: 0.14, ver_loss:0.07, time = 1.88 s
Clustering: acc=0.3857, nmi=0.4035, ari=0.2333
=======> Train epoch: 43/80
dist: P = 1.81, N = 6.21, TN = 6.32, FN = 4.7; ncl_loss: 0.14, ver_loss:0.07, time = 1.58 s
Clustering: acc=0.3935, nmi=0.4092, ari=0.2383
=======> Train epoch: 44/80
dist: P = 1.76, N = 6.24, TN = 6.35, FN = 4.71; ncl_loss: 0.14, ver_loss:0.07, time = 1.7 s
Clustering: acc=0.3824, nmi=0.4098, ari=0.2373
=======> Train epoch: 45/80
dist: P = 1.77, N = 6.29, TN = 6.4, FN = 4.75; ncl_loss: 0.14, ver_loss:0.07, time = 1.98 s
Clustering: acc=0.3933, nmi=0.4138, ari=0.2401
=======> Train epoch: 46/80
dist: P = 1.73, N = 6.32, TN = 6.43, FN = 4.79; ncl_loss: 0.13, ver_loss:0.07, time = 1.86 s
Clustering: acc=0.3706, nmi=0.4015, ari=0.2288
=======> Train epoch: 47/80
dist: P = 1.71, N = 6.35, TN = 6.46, FN = 4.8; ncl_loss: 0.13, ver_loss:0.07, time = 1.84 s
Clustering: acc=0.3868, nmi=0.4018, ari=0.233
=======> Train epoch: 48/80
dist: P = 1.74, N = 6.36, TN = 6.47, FN = 4.82; ncl_loss: 0.13, ver_loss:0.07, time = 2.04 s
Clustering: acc=0.3931, nmi=0.4113, ari=0.2389
=======> Train epoch: 49/80
dist: P = 1.73, N = 6.39, TN = 6.51, FN = 4.86; ncl_loss: 0.13, ver_loss:0.07, time = 1.77 s
Clustering: acc=0.3938, nmi=0.4078, ari=0.2378
=======> Train epoch: 50/80
dist: P = 1.71, N = 6.43, TN = 6.55, FN = 4.87; ncl_loss: 0.13, ver_loss:0.06, time = 1.85 s
Clustering: acc=0.3884, nmi=0.4, ari=0.2304
=======> Train epoch: 51/80
dist: P = 1.72, N = 6.45, TN = 6.56, FN = 4.91; ncl_loss: 0.12, ver_loss:0.06, time = 2.05 s
Clustering: acc=0.3944, nmi=0.4088, ari=0.2381
=======> Train epoch: 52/80
dist: P = 1.72, N = 6.48, TN = 6.59, FN = 4.91; ncl_loss: 0.12, ver_loss:0.06, time = 1.49 s
Clustering: acc=0.3804, nmi=0.403, ari=0.2294
=======> Train epoch: 53/80
dist: P = 1.7, N = 6.51, TN = 6.62, FN = 4.95; ncl_loss: 0.12, ver_loss:0.06, time = 1.92 s
Clustering: acc=0.3993, nmi=0.4163, ari=0.2432
=======> Train epoch: 54/80
dist: P = 1.7, N = 6.55, TN = 6.66, FN = 4.98; ncl_loss: 0.12, ver_loss:0.06, time = 2.18 s
Clustering: acc=0.377, nmi=0.3994, ari=0.2259
=======> Train epoch: 55/80
dist: P = 1.69, N = 6.56, TN = 6.68, FN = 4.99; ncl_loss: 0.12, ver_loss:0.06, time = 1.73 s
Clustering: acc=0.3826, nmi=0.408, ari=0.2327
=======> Train epoch: 56/80
dist: P = 1.69, N = 6.58, TN = 6.69, FN = 5.01; ncl_loss: 0.12, ver_loss:0.06, time = 2.62 s
Clustering: acc=0.379, nmi=0.4076, ari=0.2304
=======> Train epoch: 57/80
dist: P = 1.68, N = 6.6, TN = 6.72, FN = 5.02; ncl_loss: 0.11, ver_loss:0.06, time = 1.76 s
Clustering: acc=0.377, nmi=0.4001, ari=0.2272
=======> Train epoch: 58/80
dist: P = 1.67, N = 6.64, TN = 6.76, FN = 5.04; ncl_loss: 0.11, ver_loss:0.06, time = 1.85 s
Clustering: acc=0.3913, nmi=0.4055, ari=0.2329
=======> Train epoch: 59/80
dist: P = 1.64, N = 6.66, TN = 6.78, FN = 5.07; ncl_loss: 0.11, ver_loss:0.06, time = 1.99 s
Clustering: acc=0.3855, nmi=0.4047, ari=0.2323
=======> Train epoch: 60/80
dist: P = 1.64, N = 6.69, TN = 6.8, FN = 5.1; ncl_loss: 0.11, ver_loss:0.06, time = 1.94 s
Clustering: acc=0.3828, nmi=0.397, ari=0.2285
=======> Train epoch: 61/80
dist: P = 1.64, N = 6.71, TN = 6.83, FN = 5.13; ncl_loss: 0.11, ver_loss:0.06, time = 1.94 s
Clustering: acc=0.3871, nmi=0.4111, ari=0.2356
=======> Train epoch: 62/80
dist: P = 1.61, N = 6.73, TN = 6.85, FN = 5.13; ncl_loss: 0.11, ver_loss:0.06, time = 2.09 s
Clustering: acc=0.3808, nmi=0.404, ari=0.2284
=======> Train epoch: 63/80
dist: P = 1.63, N = 6.75, TN = 6.87, FN = 5.16; ncl_loss: 0.11, ver_loss:0.06, time = 1.77 s
Clustering: acc=0.3833, nmi=0.4012, ari=0.2284
=======> Train epoch: 64/80
dist: P = 1.64, N = 6.77, TN = 6.89, FN = 5.17; ncl_loss: 0.11, ver_loss:0.06, time = 1.88 s
Clustering: acc=0.3848, nmi=0.4039, ari=0.2291
=======> Train epoch: 65/80
dist: P = 1.61, N = 6.8, TN = 6.92, FN = 5.19; ncl_loss: 0.1, ver_loss:0.05, time = 2.06 s
Clustering: acc=0.3929, nmi=0.4127, ari=0.2391
=======> Train epoch: 66/80
dist: P = 1.62, N = 6.82, TN = 6.94, FN = 5.18; ncl_loss: 0.1, ver_loss:0.05, time = 1.79 s
Clustering: acc=0.3748, nmi=0.4047, ari=0.2282
=======> Train epoch: 67/80
dist: P = 1.58, N = 6.85, TN = 6.97, FN = 5.22; ncl_loss: 0.1, ver_loss:0.05, time = 2.02 s
Clustering: acc=0.3813, nmi=0.4016, ari=0.2282
=======> Train epoch: 68/80
dist: P = 1.59, N = 6.87, TN = 6.99, FN = 5.25; ncl_loss: 0.1, ver_loss:0.05, time = 1.85 s
Clustering: acc=0.3844, nmi=0.4055, ari=0.2336
=======> Train epoch: 69/80
dist: P = 1.59, N = 6.89, TN = 7.01, FN = 5.27; ncl_loss: 0.1, ver_loss:0.05, time = 1.83 s
Clustering: acc=0.3828, nmi=0.4089, ari=0.234
=======> Train epoch: 70/80
dist: P = 1.58, N = 6.91, TN = 7.03, FN = 5.29; ncl_loss: 0.1, ver_loss:0.05, time = 2.04 s
Clustering: acc=0.388, nmi=0.4078, ari=0.234
=======> Train epoch: 71/80
dist: P = 1.57, N = 6.93, TN = 7.05, FN = 5.3; ncl_loss: 0.09, ver_loss:0.05, time = 1.73 s
Clustering: acc=0.3819, nmi=0.4076, ari=0.2322
=======> Train epoch: 72/80
dist: P = 1.57, N = 6.97, TN = 7.09, FN = 5.31; ncl_loss: 0.09, ver_loss:0.05, time = 1.91 s
Clustering: acc=0.3806, nmi=0.3991, ari=0.2274
=======> Train epoch: 73/80
dist: P = 1.55, N = 6.97, TN = 7.09, FN = 5.31; ncl_loss: 0.09, ver_loss:0.05, time = 2.07 s
Clustering: acc=0.4, nmi=0.4089, ari=0.2387
=======> Train epoch: 74/80
dist: P = 1.56, N = 6.99, TN = 7.11, FN = 5.37; ncl_loss: 0.09, ver_loss:0.05, time = 1.82 s
Clustering: acc=0.3741, nmi=0.3992, ari=0.223
=======> Train epoch: 75/80
dist: P = 1.52, N = 7.0, TN = 7.13, FN = 5.35; ncl_loss: 0.09, ver_loss:0.05, time = 1.96 s
Clustering: acc=0.3909, nmi=0.4076, ari=0.2323
=======> Train epoch: 76/80
dist: P = 1.54, N = 7.04, TN = 7.16, FN = 5.38; ncl_loss: 0.09, ver_loss:0.05, time = 1.96 s
Clustering: acc=0.3732, nmi=0.4115, ari=0.2295
=======> Train epoch: 77/80
dist: P = 1.54, N = 7.04, TN = 7.17, FN = 5.38; ncl_loss: 0.09, ver_loss:0.05, time = 1.71 s
Clustering: acc=0.3795, nmi=0.3999, ari=0.2253
=======> Train epoch: 78/80
dist: P = 1.54, N = 7.07, TN = 7.19, FN = 5.41; ncl_loss: 0.09, ver_loss:0.05, time = 2.01 s
Clustering: acc=0.3831, nmi=0.4009, ari=0.2301
=======> Train epoch: 79/80
dist: P = 1.52, N = 7.09, TN = 7.21, FN = 5.42; ncl_loss: 0.09, ver_loss:0.05, time = 1.75 s
Clustering: acc=0.3873, nmi=0.4067, ari=0.2333
=======> Train epoch: 80/80
dist: P = 1.52, N = 7.1, TN = 7.22, FN = 5.43; ncl_loss: 0.09, ver_loss:0.05, time = 1.79 s
Clustering: acc=0.3779, nmi=0.4029, ari=0.2279
******** End, training time = 157.17 s ********
root@autodl-container-7c5d4696fb-c54fea2a:~/Sure/2022-TPAMI-SURE-main# python run.py --data 0 --gpu 0 --settings 0 --aligned-prop 1.0 --complete-prop 1.0
==========
Args:Namespace(data=0, log_interval=1, batch_size=1024, epochs=80, learn_rate=0.001, lam=0.5, noisy_training=True, neg_prop=30, margin=5, gpu='0', robust=True, switching_time=1.0, start_fine=False, settings=0, aligned_prop=1.0, complete_prop=1.0)
==========
noise rate of the constructed neg. pairs is  0.07
----------------------Training with noisy_negatives----------------------
******** Training begin ********
=======> Train epoch: 0/80
margin = 5
dist: P = 2.37, N = 2.45, TN = 2.45, FN = 2.43; ncl_loss: 4.02, ver_loss:4.41, time = 3.0 s
/root/Sure/2022-TPAMI-SURE-main/sure_inference.py:171: UserWarning: This overload of addmm_ is deprecated:
        addmm_(Number beta, Number alpha, Tensor mat1, Tensor mat2)
Consider using one of the following signatures instead:
        addmm_(Tensor mat1, Tensor mat2, *, Number beta, Number alpha) (Triggered internally at ../torch/csrc/utils/python_arg_parser.cpp:1578.)
  dist.addmm_(1, -2, x, y.t())
Clustering: acc=0.1989, nmi=0.1289, ari=0.0484
=======> Train epoch: 1/80
dist: P = 3.45, N = 3.7, TN = 3.71, FN = 3.53; ncl_loss: 1.42, ver_loss:0.36, time = 4.39 s
Clustering: acc=0.3162, nmi=0.3458, ari=0.1844
=======> Train epoch: 2/80
dist: P = 3.67, N = 4.24, TN = 4.27, FN = 3.88; ncl_loss: 0.81, ver_loss:0.17, time = 3.57 s
Clustering: acc=0.3077, nmi=0.3382, ari=0.1912
=======> Train epoch: 3/80
dist: P = 3.88, N = 4.6, TN = 4.63, FN = 4.15; ncl_loss: 0.54, ver_loss:0.15, time = 3.81 s
Clustering: acc=0.3108, nmi=0.3421, ari=0.2009
=======> Train epoch: 4/80
dist: P = 4.06, N = 4.85, TN = 4.88, FN = 4.35; ncl_loss: 0.43, ver_loss:0.13, time = 4.02 s
Clustering: acc=0.32, nmi=0.35, ari=0.1974
=======> Train epoch: 5/80
dist: P = 4.12, N = 4.99, TN = 5.03, FN = 4.46; ncl_loss: 0.39, ver_loss:0.11, time = 3.77 s
Clustering: acc=0.3311, nmi=0.3607, ari=0.2096
=======> Train epoch: 6/80
******* neg_dist_mean >= 1.0 * margin, start using fine loss at epoch: 7 *******
dist: P = 4.11, N = 5.08, TN = 5.13, FN = 4.52; ncl_loss: 0.37, ver_loss:0.1, time = 3.97 s
Clustering: acc=0.3525, nmi=0.3602, ari=0.2153
=======> Train epoch: 7/80
dist: P = 3.73, N = 5.11, TN = 5.17, FN = 4.38; ncl_loss: 0.33, ver_loss:0.09, time = 4.13 s
Clustering: acc=0.3554, nmi=0.3725, ari=0.2194
=======> Train epoch: 8/80
dist: P = 3.4, N = 5.18, TN = 5.25, FN = 4.31; ncl_loss: 0.31, ver_loss:0.09, time = 3.66 s
Clustering: acc=0.3786, nmi=0.3858, ari=0.2164
=======> Train epoch: 9/80
dist: P = 3.2, N = 5.28, TN = 5.35, FN = 4.31; ncl_loss: 0.29, ver_loss:0.09, time = 4.04 s
Clustering: acc=0.3779, nmi=0.3906, ari=0.2207
=======> Train epoch: 10/80
dist: P = 3.08, N = 5.35, TN = 5.43, FN = 4.33; ncl_loss: 0.28, ver_loss:0.08, time = 4.21 s
Clustering: acc=0.3938, nmi=0.3912, ari=0.2202
=======> Train epoch: 11/80
dist: P = 2.93, N = 5.43, TN = 5.51, FN = 4.33; ncl_loss: 0.27, ver_loss:0.08, time = 3.82 s
Clustering: acc=0.4025, nmi=0.3946, ari=0.2231
=======> Train epoch: 12/80
dist: P = 2.78, N = 5.51, TN = 5.6, FN = 4.34; ncl_loss: 0.26, ver_loss:0.08, time = 4.16 s
Clustering: acc=0.412, nmi=0.3964, ari=0.2233
=======> Train epoch: 13/80
dist: P = 2.74, N = 5.61, TN = 5.7, FN = 4.4; ncl_loss: 0.25, ver_loss:0.08, time = 4.18 s
Clustering: acc=0.4123, nmi=0.4087, ari=0.2336
=======> Train epoch: 14/80
dist: P = 2.69, N = 5.7, TN = 5.8, FN = 4.48; ncl_loss: 0.24, ver_loss:0.08, time = 3.75 s
Clustering: acc=0.4065, nmi=0.3978, ari=0.2227
=======> Train epoch: 15/80
dist: P = 2.64, N = 5.79, TN = 5.88, FN = 4.52; ncl_loss: 0.23, ver_loss:0.08, time = 4.02 s
Clustering: acc=0.4029, nmi=0.4076, ari=0.2297
=======> Train epoch: 16/80
dist: P = 2.45, N = 5.86, TN = 5.96, FN = 4.5; ncl_loss: 0.22, ver_loss:0.07, time = 4.22 s
Clustering: acc=0.4239, nmi=0.4047, ari=0.241
=======> Train epoch: 17/80
dist: P = 2.22, N = 5.96, TN = 6.07, FN = 4.51; ncl_loss: 0.21, ver_loss:0.07, time = 3.9 s
Clustering: acc=0.4243, nmi=0.4064, ari=0.2444
=======> Train epoch: 18/80
dist: P = 2.18, N = 6.08, TN = 6.19, FN = 4.58; ncl_loss: 0.2, ver_loss:0.07, time = 3.93 s
Clustering: acc=0.4054, nmi=0.4085, ari=0.233
=======> Train epoch: 19/80
dist: P = 2.12, N = 6.18, TN = 6.29, FN = 4.65; ncl_loss: 0.19, ver_loss:0.07, time = 4.1 s
Clustering: acc=0.4094, nmi=0.4033, ari=0.2342
=======> Train epoch: 20/80
dist: P = 2.11, N = 6.27, TN = 6.39, FN = 4.7; ncl_loss: 0.18, ver_loss:0.07, time = 3.73 s
Clustering: acc=0.419, nmi=0.412, ari=0.2375
=======> Train epoch: 21/80
dist: P = 2.07, N = 6.36, TN = 6.48, FN = 4.76; ncl_loss: 0.18, ver_loss:0.07, time = 3.9 s
Clustering: acc=0.3993, nmi=0.4043, ari=0.2366
=======> Train epoch: 22/80
dist: P = 2.05, N = 6.44, TN = 6.56, FN = 4.83; ncl_loss: 0.17, ver_loss:0.07, time = 4.23 s
Clustering: acc=0.3969, nmi=0.4001, ari=0.2349
=======> Train epoch: 23/80
dist: P = 2.05, N = 6.52, TN = 6.64, FN = 4.89; ncl_loss: 0.16, ver_loss:0.06, time = 3.74 s
Clustering: acc=0.3955, nmi=0.3959, ari=0.2318
=======> Train epoch: 24/80
dist: P = 2.04, N = 6.6, TN = 6.72, FN = 4.95; ncl_loss: 0.16, ver_loss:0.06, time = 3.94 s
Clustering: acc=0.425, nmi=0.4003, ari=0.2339
=======> Train epoch: 25/80
dist: P = 2.05, N = 6.66, TN = 6.79, FN = 5.02; ncl_loss: 0.16, ver_loss:0.06, time = 4.16 s
Clustering: acc=0.4243, nmi=0.3998, ari=0.2325
=======> Train epoch: 26/80
dist: P = 2.03, N = 6.74, TN = 6.86, FN = 5.05; ncl_loss: 0.15, ver_loss:0.06, time = 3.76 s
Clustering: acc=0.39, nmi=0.4077, ari=0.242
=======> Train epoch: 27/80
dist: P = 2.03, N = 6.81, TN = 6.94, FN = 5.1; ncl_loss: 0.15, ver_loss:0.06, time = 3.96 s
Clustering: acc=0.423, nmi=0.4003, ari=0.2297
=======> Train epoch: 28/80
dist: P = 2.02, N = 6.87, TN = 7.0, FN = 5.16; ncl_loss: 0.15, ver_loss:0.06, time = 4.04 s
Clustering: acc=0.4386, nmi=0.4117, ari=0.2449
=======> Train epoch: 29/80
dist: P = 2.03, N = 6.93, TN = 7.05, FN = 5.21; ncl_loss: 0.14, ver_loss:0.06, time = 3.77 s
Clustering: acc=0.4042, nmi=0.4083, ari=0.2359
=======> Train epoch: 30/80
dist: P = 2.01, N = 6.98, TN = 7.11, FN = 5.25; ncl_loss: 0.14, ver_loss:0.06, time = 4.09 s
Clustering: acc=0.4178, nmi=0.4037, ari=0.2268
=======> Train epoch: 31/80
dist: P = 2.03, N = 7.04, TN = 7.17, FN = 5.28; ncl_loss: 0.14, ver_loss:0.06, time = 3.87 s
Clustering: acc=0.4138, nmi=0.4143, ari=0.2423
=======> Train epoch: 32/80
dist: P = 2.01, N = 7.09, TN = 7.23, FN = 5.33; ncl_loss: 0.14, ver_loss:0.06, time = 4.06 s
Clustering: acc=0.3964, nmi=0.4024, ari=0.2293
=======> Train epoch: 33/80
dist: P = 1.99, N = 7.14, TN = 7.28, FN = 5.35; ncl_loss: 0.13, ver_loss:0.05, time = 3.6 s
Clustering: acc=0.3998, nmi=0.4, ari=0.2232
=======> Train epoch: 34/80
dist: P = 1.98, N = 7.19, TN = 7.32, FN = 5.37; ncl_loss: 0.13, ver_loss:0.05, time = 3.45 s
Clustering: acc=0.3935, nmi=0.4106, ari=0.2343
=======> Train epoch: 35/80
dist: P = 2.0, N = 7.24, TN = 7.38, FN = 5.43; ncl_loss: 0.13, ver_loss:0.05, time = 3.91 s
Clustering: acc=0.4314, nmi=0.4136, ari=0.2399
=======> Train epoch: 36/80
dist: P = 1.99, N = 7.29, TN = 7.43, FN = 5.47; ncl_loss: 0.13, ver_loss:0.05, time = 3.64 s
Clustering: acc=0.4312, nmi=0.4138, ari=0.2418
=======> Train epoch: 37/80
dist: P = 1.98, N = 7.33, TN = 7.47, FN = 5.5; ncl_loss: 0.12, ver_loss:0.05, time = 3.56 s
Clustering: acc=0.4343, nmi=0.4058, ari=0.2356
=======> Train epoch: 38/80
dist: P = 1.96, N = 7.38, TN = 7.52, FN = 5.53; ncl_loss: 0.12, ver_loss:0.05, time = 3.85 s
Clustering: acc=0.4103, nmi=0.4163, ari=0.2387
=======> Train epoch: 39/80
dist: P = 1.96, N = 7.42, TN = 7.56, FN = 5.56; ncl_loss: 0.12, ver_loss:0.05, time = 5.07 s
Clustering: acc=0.3969, nmi=0.41, ari=0.2325
=======> Train epoch: 40/80
dist: P = 1.96, N = 7.45, TN = 7.59, FN = 5.59; ncl_loss: 0.12, ver_loss:0.05, time = 2.81 s
Clustering: acc=0.408, nmi=0.4146, ari=0.2403
=======> Train epoch: 41/80
dist: P = 1.96, N = 7.49, TN = 7.63, FN = 5.61; ncl_loss: 0.12, ver_loss:0.05, time = 3.81 s
Clustering: acc=0.4067, nmi=0.4111, ari=0.2407
=======> Train epoch: 42/80
dist: P = 1.95, N = 7.51, TN = 7.65, FN = 5.64; ncl_loss: 0.12, ver_loss:0.05, time = 4.0 s
Clustering: acc=0.3933, nmi=0.4103, ari=0.2332
=======> Train epoch: 43/80
dist: P = 1.94, N = 7.56, TN = 7.7, FN = 5.66; ncl_loss: 0.11, ver_loss:0.05, time = 3.69 s
Clustering: acc=0.4339, nmi=0.417, ari=0.2437
=======> Train epoch: 44/80
dist: P = 1.94, N = 7.58, TN = 7.73, FN = 5.66; ncl_loss: 0.11, ver_loss:0.05, time = 3.93 s
Clustering: acc=0.4047, nmi=0.4171, ari=0.2391
=======> Train epoch: 45/80
dist: P = 1.93, N = 7.61, TN = 7.75, FN = 5.7; ncl_loss: 0.11, ver_loss:0.05, time = 4.05 s
Clustering: acc=0.4165, nmi=0.4209, ari=0.2481
=======> Train epoch: 46/80
dist: P = 1.92, N = 7.64, TN = 7.78, FN = 5.71; ncl_loss: 0.11, ver_loss:0.05, time = 3.59 s
Clustering: acc=0.4399, nmi=0.4201, ari=0.247
=======> Train epoch: 47/80
dist: P = 1.92, N = 7.67, TN = 7.81, FN = 5.74; ncl_loss: 0.11, ver_loss:0.04, time = 3.86 s
Clustering: acc=0.4071, nmi=0.4133, ari=0.2355
=======> Train epoch: 48/80
dist: P = 1.9, N = 7.7, TN = 7.85, FN = 5.77; ncl_loss: 0.11, ver_loss:0.04, time = 3.99 s
Clustering: acc=0.4105, nmi=0.4183, ari=0.2431
=======> Train epoch: 49/80
dist: P = 1.9, N = 7.73, TN = 7.87, FN = 5.79; ncl_loss: 0.1, ver_loss:0.04, time = 3.7 s
Clustering: acc=0.39, nmi=0.4204, ari=0.2473
=======> Train epoch: 50/80
dist: P = 1.89, N = 7.76, TN = 7.9, FN = 5.79; ncl_loss: 0.1, ver_loss:0.04, time = 3.8 s
Clustering: acc=0.3683, nmi=0.4004, ari=0.228
=======> Train epoch: 51/80
dist: P = 1.9, N = 7.78, TN = 7.93, FN = 5.81; ncl_loss: 0.1, ver_loss:0.04, time = 3.93 s
Clustering: acc=0.3953, nmi=0.4106, ari=0.2346
=======> Train epoch: 52/80
dist: P = 1.86, N = 7.8, TN = 7.95, FN = 5.83; ncl_loss: 0.1, ver_loss:0.04, time = 3.83 s
Clustering: acc=0.4245, nmi=0.4169, ari=0.2455
=======> Train epoch: 53/80
dist: P = 1.87, N = 7.83, TN = 7.98, FN = 5.87; ncl_loss: 0.1, ver_loss:0.04, time = 2.86 s
Clustering: acc=0.3982, nmi=0.4125, ari=0.2312
=======> Train epoch: 54/80
dist: P = 1.83, N = 7.86, TN = 8.01, FN = 5.87; ncl_loss: 0.1, ver_loss:0.04, time = 3.56 s
Clustering: acc=0.4219, nmi=0.4249, ari=0.2483
=======> Train epoch: 55/80
dist: P = 1.85, N = 7.88, TN = 8.03, FN = 5.9; ncl_loss: 0.1, ver_loss:0.04, time = 3.86 s
Clustering: acc=0.3875, nmi=0.4052, ari=0.2281
=======> Train epoch: 56/80
dist: P = 1.83, N = 7.9, TN = 8.05, FN = 5.91; ncl_loss: 0.1, ver_loss:0.04, time = 4.1 s
Clustering: acc=0.3989, nmi=0.4159, ari=0.2426
=======> Train epoch: 57/80
dist: P = 1.83, N = 7.92, TN = 8.07, FN = 5.92; ncl_loss: 0.1, ver_loss:0.04, time = 3.92 s
Clustering: acc=0.3989, nmi=0.4088, ari=0.2365
=======> Train epoch: 58/80
dist: P = 1.82, N = 7.95, TN = 8.1, FN = 5.93; ncl_loss: 0.09, ver_loss:0.04, time = 4.11 s
Clustering: acc=0.3777, nmi=0.4113, ari=0.2314
=======> Train epoch: 59/80
dist: P = 1.81, N = 7.97, TN = 8.12, FN = 5.96; ncl_loss: 0.09, ver_loss:0.04, time = 4.62 s
Clustering: acc=0.4002, nmi=0.4141, ari=0.2351
=======> Train epoch: 60/80












dist: P = 1.79, N = 7.99, TN = 8.14, FN = 5.99; ncl_loss: 0.09, ver_loss:0.04, time = 4.01 s
Clustering: acc=0.4178, nmi=0.4161, ari=0.238
=======> Train epoch: 61/80
dist: P = 1.8, N = 8.0, TN = 8.15, FN = 5.98; ncl_loss: 0.09, ver_loss:0.04, time = 4.85 s
Clustering: acc=0.4132, nmi=0.4179, ari=0.241
=======> Train epoch: 62/80
dist: P = 1.78, N = 8.03, TN = 8.18, FN = 6.0; ncl_loss: 0.09, ver_loss:0.04, time = 4.16 s
Clustering: acc=0.3967, nmi=0.4116, ari=0.231
=======> Train epoch: 63/80
dist: P = 1.79, N = 8.03, TN = 8.18, FN = 6.01; ncl_loss: 0.09, ver_loss:0.04, time = 3.82 s
Clustering: acc=0.3949, nmi=0.4056, ari=0.2276
=======> Train epoch: 64/80
dist: P = 1.78, N = 8.05, TN = 8.2, FN = 5.99; ncl_loss: 0.09, ver_loss:0.04, time = 4.08 s
Clustering: acc=0.3987, nmi=0.3988, ari=0.2214
=======> Train epoch: 65/80
dist: P = 1.75, N = 8.07, TN = 8.22, FN = 6.03; ncl_loss: 0.09, ver_loss:0.04, time = 4.36 s
Clustering: acc=0.4147, nmi=0.416, ari=0.2403
=======> Train epoch: 66/80
dist: P = 1.77, N = 8.09, TN = 8.25, FN = 6.05; ncl_loss: 0.09, ver_loss:0.04, time = 4.02 s
Clustering: acc=0.3973, nmi=0.4144, ari=0.2339
=======> Train epoch: 67/80
dist: P = 1.74, N = 8.11, TN = 8.26, FN = 6.06; ncl_loss: 0.08, ver_loss:0.04, time = 4.14 s
Clustering: acc=0.4357, nmi=0.4109, ari=0.2431
=======> Train epoch: 68/80
dist: P = 1.75, N = 8.13, TN = 8.28, FN = 6.1; ncl_loss: 0.08, ver_loss:0.04, time = 4.2 s
Clustering: acc=0.3844, nmi=0.4091, ari=0.231
=======> Train epoch: 69/80
dist: P = 1.73, N = 8.13, TN = 8.29, FN = 6.1; ncl_loss: 0.08, ver_loss:0.04, time = 4.12 s
Clustering: acc=0.4232, nmi=0.4113, ari=0.2326
=======> Train epoch: 70/80
dist: P = 1.71, N = 8.15, TN = 8.3, FN = 6.11; ncl_loss: 0.08, ver_loss:0.04, time = 3.82 s
Clustering: acc=0.4018, nmi=0.406, ari=0.2236
=======> Train epoch: 71/80
dist: P = 1.71, N = 8.17, TN = 8.32, FN = 6.12; ncl_loss: 0.08, ver_loss:0.04, time = 3.96 s
Clustering: acc=0.4085, nmi=0.4162, ari=0.2382
=======> Train epoch: 72/80
dist: P = 1.7, N = 8.19, TN = 8.34, FN = 6.13; ncl_loss: 0.08, ver_loss:0.04, time = 4.12 s
Clustering: acc=0.4225, nmi=0.4119, ari=0.2317
=======> Train epoch: 73/80
dist: P = 1.7, N = 8.21, TN = 8.37, FN = 6.16; ncl_loss: 0.08, ver_loss:0.04, time = 4.41 s
Clustering: acc=0.3612, nmi=0.4057, ari=0.2259
=======> Train epoch: 74/80
dist: P = 1.71, N = 8.22, TN = 8.37, FN = 6.16; ncl_loss: 0.08, ver_loss:0.04, time = 3.82 s
Clustering: acc=0.388, nmi=0.4131, ari=0.2369
=======> Train epoch: 75/80
dist: P = 1.69, N = 8.23, TN = 8.38, FN = 6.16; ncl_loss: 0.08, ver_loss:0.04, time = 3.99 s
Clustering: acc=0.4214, nmi=0.4068, ari=0.2316
=======> Train epoch: 76/80
dist: P = 1.68, N = 8.24, TN = 8.4, FN = 6.16; ncl_loss: 0.08, ver_loss:0.04, time = 3.37 s
Clustering: acc=0.3668, nmi=0.4077, ari=0.2287
=======> Train epoch: 77/80
dist: P = 1.68, N = 8.27, TN = 8.42, FN = 6.2; ncl_loss: 0.08, ver_loss:0.04, time = 3.05 s
Clustering: acc=0.4087, nmi=0.4123, ari=0.2368
=======> Train epoch: 78/80
dist: P = 1.67, N = 8.27, TN = 8.42, FN = 6.22; ncl_loss: 0.08, ver_loss:0.04, time = 3.3 s
Clustering: acc=0.4045, nmi=0.4111, ari=0.2319
=======> Train epoch: 79/80
dist: P = 1.69, N = 8.28, TN = 8.43, FN = 6.22; ncl_loss: 0.08, ver_loss:0.04, time = 4.13 s
Clustering: acc=0.3922, nmi=0.4128, ari=0.2353
=======> Train epoch: 80/80
dist: P = 1.65, N = 8.29, TN = 8.44, FN = 6.22; ncl_loss: 0.07, ver_loss:0.04, time = 3.74 s
Clustering: acc=0.4103, nmi=0.3955, ari=0.2185
******** End, training time = 316.48 s ********
root@autodl-container-7c5d4696fb-c54fea2a:~/Sure/2022-TPAMI-SURE-main# 
```
