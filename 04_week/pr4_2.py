#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:55:49 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model("pr4_2")
    
    Z = LinExpr()
    X = m.addVars(3, vtype = GRB.INTEGER, name = 'X')
    Y = m.addVars(3, vtype = GRB.BINARY, name = 'Y')
    Cos = [3, 2, 0]
    Prf = [2, 3, 0.8]
    Cap = [0.2, 0.4, 0.2]
    Ord = [3, 2, 5]
    
    Z = (sum(X[i]*Prf[i] - Y[i]*Cos[i] for i in range(0, 3)))
    
    # 제약식 1
    c0 = (sum(X[i]*Cap[i] for i in range(0, 3))) <= 1
    m.addConstr(c0, 'c0')
    
    # 제약식 2
    for i in range(0, 3):
        c1 = X[i] <= Ord[i]
        m.addConstr(c1, 'c1'+str(i))
    
    # 제약식 3
    M = 10000000
    for i in range(0, 3):
        c2 = X[i] <= M*Y[i]
        m.addConstr(c2, 'c2'+str(i))
        
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
    
    for v in m.getVars():
        print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
    

except GurobiError : 
    print('Error reported')
    