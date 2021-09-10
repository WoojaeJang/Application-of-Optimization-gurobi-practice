#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:39:01 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model("ex4_3")
    
    Z = LinExpr()
    X = m.addVars(4, vtype = GRB.INTEGER, name='X')
    Y = m.addVars(5, vtype = GRB.BINARY, name='Y')
    Cos = [50000, 40000, 70000, 60000]
    Rev = [70, 60, 90, 80]
        
    Z = (sum(X[i]*Rev[i] - Y[i]*Cos[i] for i in range(0, 4)))
    
    # 제약식 1
    M = 100000
    for i in range(0, 4):
        c0 = X[i] <= M*Y[i]
        m.addConstr(c0, 'c0'+str(i))
    
    # 제약식 2
    c1 = (sum(Y[i] for i in range(0, 4))) <= 2
    c2 = Y[2] <= Y[0] + Y[1]
    c3 = Y[3] <= Y[0] + Y[1]
    
    # 제약식 3
    Ei1 = [5, 3, 6, 4]
    Ei2 = [4, 6, 3, 5]
    c4 = (sum(X[i]*Ei1[i] for i in range(0, 4))) <= 6000 + M*Y[4]
    c5 = (sum(X[i]*Ei2[i] for i in range(0, 4))) <= 6000 + M*(1-Y[4])
    
    m.addConstr(c1, "c1")
    m.addConstr(c2, "c2")
    m.addConstr(c3, "c3")
    m.addConstr(c4, "c4")
    m.addConstr(c5, "c5")
    
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
        
    for v in m.getVars():
        print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
    
    
except GurobiError:
    print('Error reported') 