#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 08:53:00 2020

@author: ashim
"""

from multiprocessing import cpu_count
from collections import deque
import copy
from icarus.util import Tree

LOG_LEVEL = 'INFO'

PARALLEL_EXECUTION =True
N_PROCESSES = cpu_count()

N_REPLICATIONS = 1
CACHING_GRANULARITY = 'OBJECT'
RESULTS_FORMAT = 'PICKLE'
DATA_COLLECTORS = ['CACHE_HIT_RATIO', 'LATENCY']

EXPERIMENT_QUEUE = deque()

experiment = Tree()
experiment['topology']['name'] = 'PATH'
experiment['topology']['n'] = 10
experiment['topology']['delay'] = 10

experiment['workload'] = {
        'name' : 'STATIONARY',
        'n_contents' : 10 ** 5,
        'n_warmup' : 10 ** 2,
        'n_measured' : 4*10**2,
        'alpha' : 1.0,
        'rate' : 1
    }

experiment['cache_placement']['name'] = 'UNIFORM'
experiment['cache_placement']['network_cache'] = 0.01 #10% of total content

experiment['content_placement']['name'] = 'UNIFORM'

experiment['cache_policy']['name'] = 'LRU'
experiment['strategy']['name'] = 'LCE'

experiment['desc'] = "Line topology with 10 nodes"

EXPERIMENT_QUEUE.append(experiment)




























