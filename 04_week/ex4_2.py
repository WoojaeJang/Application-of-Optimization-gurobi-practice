#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:27:18 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model("ex4_2")
    
    Z = LinExpr()
    X = m.addVars(7, vtype = GRB.BINARY, name = 'X')
    Prf = [17, 10, 15, 19, 7, 13, 9]
    Req = [43, 28, 34, 48, 17, 32, 23]
    
    Z = (sum(X[i]*Prf[i] for i in range(0, 7)))
    
    # 제약식 1
    tempC = (sum(X[i]*Req[i] for i in range(0, 7)))
    c0 = tempC <= 100
    
    # 제약식 2
    c1 = X[1] + X[2] <= 1
    c2 = X[3] + X[4] <= 1
    c3 = X[3] <= X[1] + X[2]
    c4 = X[4] <= X[1] + X[2]
    
    m.addConstr(c0, 'c0')
    m.addConstr(c1, 'c1')
    m.addConstr(c2, 'c2')
    m.addConstr(c3, 'c3')
    m.addConstr(c4, 'c4')
    
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
    
    for v in m.getVars():
        if v.x != 0.0:
            print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
    
    
except GurobiError:
    print('Error reported')