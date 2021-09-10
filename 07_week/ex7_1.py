#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:06:42 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model('ex7_1')
    
    Z = LinExpr()
    
    X = m.addVars(5, 6, vtype = GRB.BINARY, name = 'X')
    Y = m.addVars(5, vtype = GRB.BINARY, name = 'Y')
    
    C = [[1675, 400, 685, 1630, 1160, 2800],
         [1460, 1940, 970, 100, 495, 1200],
         [1925, 2400, 1425, 500, 950, 800],
         [380, 1355, 543, 1045, 665, 2321],
         [922, 1646, 700, 508, 311, 1797]]
    D = [10, 8, 12, 6, 7, 11]
    K = [18, 24, 27, 22, 31]
    F = [7650, 3500, 3500, 4100, 2200]
    
    # 목적함수
    Z = 0
    for i in range(5) :
        Z += F[i]*Y[i]
        for j in range(6) : 
            Z += C[i][j]*X[i,j]
    
    # 제약조건 1
    for j in range(6) :
        tempC = 0
        for i in range(5) :
            tempC += X[i,j]
        c0 = tempC == 1
        m.addConstr(c0, 'c0'+str(j))
    
    # 제약조건 2
    for i in range(5) : 
        tempC2 = 0
        for j in range(6) :
            tempC2 += D[j]*X[i,j]
        c1 = tempC2 <= K[i]*Y[i]
        m.addConstr(c1, 'c1'+str(i))
        
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
except GurobiError() :
    print('Error reported')
         
    
    
    