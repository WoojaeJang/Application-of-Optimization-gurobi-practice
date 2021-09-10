#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:26:49 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model("ex4_0")
    
    Z = LinExpr()
    X = m.addVars(4, vtype = GRB.BINARY, name='X')
    VAL = [9, 5, 6, 4]
    REQ = [6, 3, 5, 2]
    
    Z = (sum(X[i]*VAL[i] for i in range(0, 4)))
    tempC = (sum(X[i]*REQ[i] for i in range(0, 4)))
    
    c0 = tempC <= 11
    c1 = X[2] + X[3] <= 1
    c2 = X[2] - X[0] <= 0
    c3 = X[3] - X[1] <= 0
       
    m.addConstr(c0, "c0")
    m.addConstr(c1, "c1")
    m.addConstr(c2, "c2")
    m.addConstr(c3, "c3")
    
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
        
    for v in m.getVars():
        print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
  
        
    
except GurobiError:
    print('Error reported')


