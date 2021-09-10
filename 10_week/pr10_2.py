#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:55:06 2021

@author: woojae-macbook13
"""

import numpy as np

A = np.array([[-0.05, 0.5],\
              [1, 1]])

b = np.array([0, 1])

x = np.linalg.inv(A).dot(b)

print(x)