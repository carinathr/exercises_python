# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:46:20 2023

@author: s_thren20
"""
from math import log10
import numpy as np

x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

log_x = [log10(k) for k in x]
print(log_x)

x_log_numpy = np.log10(x)
print(x_log_numpy)