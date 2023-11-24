# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:01:09 2023

@author: s_thren20
"""
import numpy as np
D = np.tile(np.arange(1, 11), (10, 1))
D_summe = D.sum(axis = 0)
D_mittelwert = D.mean(axis = 1)

print(D_summe)
print(D_mittelwert)

E = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[9,8,7], [6,5,4], [3,2,1]], [[9,8,7], [3,2,1], [6,5,4]]])
print(E.sum(axis=0))