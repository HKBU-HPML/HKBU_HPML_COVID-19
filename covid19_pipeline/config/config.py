from torchline.config import CfgNode as CN

__all__ = [
    'add_config'
]

def add_config(cfg):
    '''
    cfg.new_item = CN()
    '''
    cfg.dataset.slice_num = 64
    cfg.dataset.is_color = False
    
    # model_depth
    cfg.model.model_depth = 101
    cfg.model.n_input_channels = 1
    cfg.model.dropout = 0

    ################################################################
    # ct transforms                                                #
    # https://torchio.readthedocs.io/                              #
    ################################################################
    cfg.transforms.ct = CN()
    cfg.transforms.ct.randomflip = CN()
    cfg.transforms.ct.randomflip.enable = 1
    cfg.transforms.ct.randomflip.p = 0.5 
    cfg.transforms.ct.randomflip.axes = (0, 1,2) 
    cfg.transforms.ct.randomflip.flip_probability = 0.5

    cfg.transforms.ct.randomaffine = CN()
    cfg.transforms.ct.randomaffine.enable = 0 
    cfg.transforms.ct.randomaffine.scales = (0.5,0.5)
    cfg.transforms.ct.randomaffine.degrees = (-10,10)
    cfg.transforms.ct.randomaffine.isotropic = True
    cfg.transforms.ct.randomaffine.p = 0.5

    cfg.transforms.ct.randomblur = CN()
    cfg.transforms.ct.randomblur.enable = 0
    cfg.transforms.ct.randomblur.p = 0.5
    cfg.transforms.ct.randomblur.std = (0, 4)

    cfg.transforms.ct.randomnoise = CN()
    cfg.transforms.ct.randomnoise.enable = 0
    cfg.transforms.ct.randomnoise.p = 0.5
    cfg.transforms.ct.randomnoise.mean = (0,0.25)
    cfg.transforms.ct.randomnoise.std = (0,0.25)

    cfg.transforms.ct.randomswap = CN()
    cfg.transforms.ct.randomswap.enable = 0
    cfg.transforms.ct.randomswap.p = 0.5
    cfg.transforms.ct.randomswap.patch_size = (16,16,16)
    cfg.transforms.ct.randomswap.num_iterations = 100

    cfg.transforms.ct.randomelasticdeformation = CN()
    cfg.transforms.ct.randomelasticdeformation.enable = 0
    cfg.transforms.ct.randomelasticdeformation.p = 0.5
    cfg.transforms.ct.randomelasticdeformation.num_control_points = (4,4,4)
    cfg.transforms.ct.randomelasticdeformation.max_displacement = (7,7,7)
    cfg.transforms.ct.randomelasticdeformation.locked_borders = 0

    return cfg
