# This file is eval'd inside the plot-correlation.py file

# This maps the named GPGPU-Sim config to the card name reported in the nvprof file.
#   Every time you want to correlate a new configuration, you need to map it here.
config_maps = \
{
    "TITANRTX": set("NVIDIA RTX TITAN"),
    "TITANX": set("TITAN X (Pascal)"),
    "P100_HBM" : set("Tesla P100"),
    "GTX480" : set("GeForce GTX 480"),
    "GTX1080Ti" : set("GeForce GTX 1080 Ti"),
    "TITANK" : set("GeForce GTX TITAN"),
    "QV100" : set(["TITAN V", "Quadro GV100","Tesla V100-SXM2-32GB"]),
    "RTX2060" : set("GeForce RTX 2060"),
    "RTX3070" : set("GeForce RTX 3070"),
}

import os
import yaml
import collections

# Every stat you want to correlate gets an entry here.
#   For cycles, the math is different for every card so we have differnt stats baed on the hardware.
CorrelStat = collections.namedtuple('CorrelStat', 'chart_name hw_eval hw_error sim_eval hw_name plotfile drophwnumbelow plottype stattype')

with open(os.path.dirname(os.path.realpath(__file__)) + '/correl.yml', 'r') as f:
    correl_list = yaml.safe_load(f)