#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:17:12 2020

@author: ashim
"""

from multiprocessing import cpu_count
from collections import deque
import copy
from icarus.util import Tree

PARALLEL_EXECUTION = True
N_PROCESSES = cpu_count()
LOG_LEVEL = 'INFO'
RESULTS_FORMAT = 'PICKLE'
CACHING_GRANULARITY = 'OBJECT'

N_REPLICATIONS = 1
DATA_COLLECTORS = ['CACHE_HIT_RATIO','LATENCY','LINK_LOAD', 'PATH_STRETCH']

EXPERIMENT_QUEUE = deque()
default = Tree()

default['workload'] = {
        'name' : 'STATIONARY',
        'alpha' : 0.8,
        'n_contents' : 10 ** 5,
        'n_warmup' : 10 ** 5,
        'n_measured' : 4 * 10 **5,
        'rate' : 1.0
    }
default['topology']['name'] = 'ROCKET_FUEL'
default['topology']['asn'] = 1221

default['cache_placement']['network_cache'] = 0.01
default['cache_placement']['name'] = 'UNIFORM'

default['content_placement']['name'] = 'UNIFORM'

default['cache_policy']['name'] = 'LRU'

STRATEGIES = [ 'NO_CACHE','RAND_CHOICE', 'LCE', 'LCD', 'CL4M', 'ASHIM_CLOSENESS', 'ASHIM_HBLB', 'ASHIM_HBHC' ]


for strategy in STRATEGIES:
    experiment = copy.deepcopy(default)
    experiment['strategy']['name'] = strategy;
    experiment['desc'] = "Strategy: %s " % strategy
    EXPERIMENT_QUEUE.append(experiment)



























