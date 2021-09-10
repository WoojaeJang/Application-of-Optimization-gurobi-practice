#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:49:14 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model("ex4_1")
    
    Z = LinExpr()
    X = m.addVars(2,4, vtype = GRB.BINARY, name = 'X')
    Val = [[4.5, 7.8, 3.6, 2.9], [4.9, 7.2, 4.3, 3.1]]
    
    for i in range(2):
        for j in range(4):
            Z += Val[i][j]*X[i,j]
    
    # 제약식 1
    c0 = (sum(X[i,j] for i in range(2)) == 1 for j in range(4))
    
    # 제약식 2
    c1 = (sum(X[i,j] for j in range(4)) == 2 for i in range(2))
    
    m.addConstrs(c0, 'c0')
    m.addConstrs(c1, 'c1')
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
        
    for v in m.getVars():
        if v.x != 0.0:
            print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
    
    
except GurobiError:
    print('Error reported')