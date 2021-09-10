#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:32:23 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model('ex7_2')
    
    Z = LinExpr()
    
    X = m.addVars(6, 6, vtype = GRB.BINARY, name = 'X')
    
    C = [[20, 15, 16, 5, 4, 7],
         [17, 15, 33, 12, 8, 6],
         [9, 12, 18, 16, 30, 13],
         [12, 8, 11, 27, 19, 14],
         [0, 7, 10, 21, 10, 32],
         [0, 0, 0, 6, 11, 13]]
    
    # 목적함수
    Z = 0
    for i in range(6) : 
        for j in range(6) :
            Z += C[i][j] * X[i,j]
            
    # 제약조건 1 도착
    for i in range(6) : 
        tempC = 0
        for j in range(6) : 
            tempC += X[i,j]
        c0 = tempC == 1
        m.addConstr(c0, 'c0'+str(j))
    
    # 제약조건 2 출발
    for j in range(6) :
        tempC2 = 0
        for i in range(6) : 
            tempC2 += X[i,j]
        c1 = tempC2 == 1
        m.addConstr(c1, 'c1'+str(j))
        
    
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
    
except GurobiError() :
    print('Error reported')
    
    
    