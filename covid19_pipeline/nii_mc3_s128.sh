srun -N 1 -n 1 --gres=gpu:4 --nodelist=hkbugpusrv02 python3.6 main.py --config_file ./config/nii_config.yml trainer.gpus [0,1,2,3] model.name mc3_18 dataset.slice_num 128 dataset.batch_size 32 trainer.logger.test_tube.name nii_mc3_18_datas_bs64_s128
