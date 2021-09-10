#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:10:20 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model("pr4_1")
    
    Z = LinExpr()
    X = m.addVars(2,2, vtype = GRB.INTEGER, name='X')
    Y = m.addVars(2,2, vtype= GRB.BINARY, name='Y')
    Y2 = m.addVar(vtype = GRB.BINARY, name='Y2')
    Prf = [[10, 15], [10, 15]]
    Cos = [[50000, 80000], [50000, 80000]]
    
    for i in range(0, 2) :
        for j in range(0, 2) :
            Z += X[i,j]*Prf[i][j] - Y[i,j]*Cos[i][j]
    
    # 제약식 1
    M = 10000000
    k=0
    for i in range(0, 2):
        for j in range(0, 2):
            c0 = X[i,j] <= M*Y[i,j]
            m.addConstr(c0, 'c0'+str(k))
            k += 1
    
    # 제약식 2
    c1 = X[0,0]/50 + X[0,1]/40 <= 500
    c2 = X[1,0]/40 + X[1,1]/25 <= 700
    
    # 제약식 3
    c3 = X[0,0]+X[0,1] <= M*Y2
    c4 = X[1,0]+X[1,1] <= M*(1-Y2)
    
    m.addConstr(c1, "c1")
    m.addConstr(c2, "c2")
    m.addConstr(c3, "c3")
    m.addConstr(c4, "c4")
    
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
        
    for v in m.getVars():
        print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
    
    
except GurobiError:
    print('Error reported') 
