#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:43:35 2021

@author: woojae-macbook13
"""

import numpy as np

A = np.array([[-1, 0, 0, 1],
              [7/8, -1/4, 0, 0],
              [1/16, 1/8, -1/2, 0],
              [1, 1, 1, 1]])

b = np.array([0, 0, 0, 1])

x = np.linalg.inv(A).dot(b)

print(x)

COST = [0, 1000, 3000, 6000]

print(sum(x*COST))

print(1/x[0])