from loguru import logger
import warnings

warnings.filterwarnings('ignore')


from offlinerl.config.algo import cql_config, plas_config, mopo_config, moose_config, bcqd_config, bcq_config, bc_config, crr_config, combo_config, bremen_config, mycode_config, mycode_u_config, mycode_uw_config, mycode_uw_exp3_config
from offlinerl.utils.config import parse_config
from offlinerl.algo.modelfree import cql, plas, bcqd, bcq, bc, crr
from offlinerl.algo.modelbase import mopo, moose, combo, bremen, mycode, mycode_u, mycode_uw, mycode_uw_exp3

algo_dict = {
    'bc' : {"algo" : bc, "config" : bc_config},
    'bcq' : {"algo" : bcq, "config" : bcq_config},
    'bcqd' : {"algo" : bcqd, "config" : bcqd_config},
    'combo' : {"algo" : combo, "config" : combo_config},
    "cql" : {"algo" : cql, "config" : cql_config},
    "crr" : {"algo" : crr, "config" : crr_config},
    "plas" : {"algo" : plas, "config" : plas_config},
    'moose' : {"algo" : moose, "config" : moose_config},
    'mopo': {"algo" : mopo, "config": mopo_config},
    'bremen' : {"algo" : bremen, "config" : bremen_config},
    'mycode' : {"algo" : mycode, "config" : mycode_config},
    'mycode_u' : {"algo" : mycode_u, "config" : mycode_u_config},
    'mycode_uw': {"algo" : mycode_uw, "config" : mycode_uw_config},
    'mycode_uw_exp3': {"algo" : mycode_uw_exp3, "config" : mycode_uw_exp3_config},
}

def algo_select(command_args, algo_config_module=None):
    algo_name = command_args["algo_name"]
    logger.info('Use {} algorithm!', algo_name)
    assert algo_name in algo_dict.keys()
    algo = algo_dict[algo_name]["algo"]
    
    if algo_config_module is None:
        algo_config_module = algo_dict[algo_name]["config"]
    algo_config = parse_config(algo_config_module)
    algo_config.update(command_args)
    print("*********horizon: {}***************".format(algo_config['horizon']))
    
    algo_init = algo.algo_init
    algo_trainer = algo.AlgoTrainer
    
    return algo_init, algo_trainer, algo_config
    
    