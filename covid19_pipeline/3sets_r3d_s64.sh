#srun -N 1 -n 1 --gres=gpu:3 --nodelist=hkbugpusrv05 python3.6 main.py --config_file ./config/3sets_config.yml trainer.gpus [1,2,3] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64
#########################################################################################
#train
#~/py36/bin/python main.py --config_file ./config/3sets_config.yml trainer.gpus [1,2,3] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64
~/py36/bin/python main.py --config_file ./config/3sets_2cls_config.yml trainer.gpus [1,2,3] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64
#########################################################################################
#~/py36/bin/python main.py   --test_only   --config_file ./config/3sets_config.yml  trainer.gpus [1] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64 predict_only.weights_path ./output/3sets_r3d_18_bs9_s64/version_3/checkpoints/epoch=76-valid_acc_1=85.20.ckpt
#~/py36/bin/python main.py   --test_only   --config_file ./config/ccccii_config.yml trainer.gpus [1] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64 predict_only.weights_path ./output/3sets_r3d_18_bs9_s64/version_3/checkpoints/epoch=76-valid_acc_1=85.20.ckpt
#~/py36/bin/python main.py --test_only --config_file ./config/mosmeddata_config.yml trainer.gpus [1] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64 predict_only.weights_path ./output/3sets_r3d_18_bs9_s64/version_3/checkpoints/epoch=76-valid_acc_1=85.20.ckpt
#~/py36/bin/python main.py --test_only --config_file ./config/covidctset_config.yml trainer.gpus [1] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64 predict_only.weights_path ./output/3sets_r3d_18_bs9_s64/version_3/checkpoints/epoch=76-valid_acc_1=85.20.ckpt
#~/py36/bin/python main.py   --test_only   --config_file ./config/ccccii_config.yml trainer.gpus [1] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64 predict_only.weights_path ./output/3sets_r3d_18_bs9_s64/version_17/checkpoints/epoch=51-valid_acc_1=86.24.ckpt
#~/py36/bin/python main.py --test_only --config_file ./config/mosmeddata_config.yml trainer.gpus [1] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64 predict_only.weights_path ./output/3sets_r3d_18_bs9_s64/version_17/checkpoints/epoch=51-valid_acc_1=86.24.ckpt
#~/py36/bin/python main.py --test_only --config_file ./config/covidctset_config.yml trainer.gpus [1] model.name resnet3d model.model_depth 18 dataset.slice_num 64 dataset.batch_size 9 trainer.logger.test_tube.name 3sets_r3d_18_bs9_s64 predict_only.weights_path ./output/3sets_r3d_18_bs9_s64/version_17/checkpoints/epoch=51-valid_acc_1=86.24.ckpt