#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:38:21 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model('ex9_1_1')
    
    Z = LinExpr() 
    
    NODE = 7 
    
    X = m.addVars(NODE, NODE, vtype = GRB.BINARY, name = 'X')
    
    DIST = [[0, 2, 5, 4, 0, 0, 0], 
            [0, 0, 2, 0, 7, 0, 0], 
            [0, 0, 0, 1, 4, 3, 0], 
            [0, 0, 0, 0, 0, 4, 0], 
            [0, 0, 0, 0, 0, 1, 5], 
            [0, 0, 0, 0, 0, 0, 7], 
            [0, 0, 0, 0, 0, 0, 0]]
    
    # 목적 함수
    Z = 0
    for i in range(NODE) :
        for j in range(NODE) :
            Z += X[i,j]*DIST[i][j]
    
    # 제약 조건
    for i in range(NODE) :
        tempC = 0
        for j in range(NODE) :
            if DIST[i][j] != 0 :
                tempC += X[i,j]
        for k in range(NODE) :
            if DIST[k][i] != 0 :
                tempC -= X[k,i]
        
        if i == 0 :
            c0 = tempC == 1
            m.addConstr(c0, 'c0'+str(i))
        elif i == NODE - 1 :
            c0 = tempC == -1
            m.addConstr(c0, 'c0'+str(i))
        else :
            c0 = tempC == 0
            m.addConstr(c0, 'c0'+str(i))
  
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
    
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
    
except GurobiError() : 
    print('Error reported')
    
    
    
    
    
    