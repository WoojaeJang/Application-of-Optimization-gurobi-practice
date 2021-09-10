#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:25:13 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    m = Model("ex3_2")
    
    x = m.addVars(10, vtype = GRB.BINARY, name = 'x')
    x2 = m.addVars(14, vtype = GRB.BINARY, name = 'x2')
    x3 = m.addVars(17, vtype = GRB.BINARY, name = 'x3')
    
    m.update()
    
    COST = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    COST2 = [3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 2]
    COST3 = [2, 3, 3, 2, 3, 3, 2, 3, 3, 3, 2, 3, 2, 2, 3, 3, 3]
        
    YN1 = [[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
           [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

    YN2 = [[1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
           [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
           [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
    
    
    Z = LinExpr()
    
    Z = (sum(x[i]*COST[i] for i in range(0, 10))) +\
        (sum(x2[j]*COST2[j] for j in range(0, 14))) +\
        (sum(x3[i]*COST3[i] for i in range(0, 17)))
        
    for i in range(0, 10):
        tempC = x[i]
        for j in range(0,14):
            if YN1[i][j] != 0:
                tempC += YN1[i][j]*x2[j]
                
        for k in range(0, 17):
            if YN2[i][k] != 0:
                tempC += YN2[i][k]*x3[k]
        
        tempCC = tempC == 1
        
        m.addConstr(tempCC, "c"+str(i))
        
    
    m.setObjective(Z, GRB.MINIMIZE)
    m.optimize()
    
    for v in m.getVars():
        print(v.varName,':',v.x)
        
    print('Z:', m.objVal)
    
    
except GurobiError:
    print('Error reported')
        
        
        
    
    
    
    
    








