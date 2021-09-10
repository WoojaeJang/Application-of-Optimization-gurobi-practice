#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:38:22 2021

@author: woojae-macbook13
"""

import numpy as np

A = np.array([[-0.2, 0.25, 0.15],\
              [0.15, -0.3, 0.05],\
              [1, 1, 1]])

b = np.array([0, 0, 1])

x = np.linalg.inv(A).dot(b)

print(x)