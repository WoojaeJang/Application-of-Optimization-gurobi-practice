#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:21:52 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model('ex9_2_1')
    
    Z = LinExpr() 
    
    NODE = 7 
    
    X = m.addVars(NODE, NODE, vtype = GRB.INTEGER, name = 'X')
    
    CAPA = [[0, 5, 7, 4, 0, 0, 0], 
            [0, 0, 1, 0, 3, 0, 0], 
            [0, 0, 0, 2, 4, 5, 0], 
            [0, 0, 0, 0, 0, 4, 0], 
            [0, 0, 0, 0, 0, 0, 9], 
            [0, 0, 0, 0, 1, 0, 6], 
            [0, 0, 0, 0, 0, 0, 0]]
    
    # 목적 함수
    Z = 0
    for j in range(NODE) :
        if CAPA[0][j] != 0 :
            Z += X[0,j]
    for k in range(NODE) :
        if CAPA[k][0] != 0 :
            Z -= X[k,0]
    
    # 제약 조건
    for i in range(NODE) :
        for j in range(NODE) :
            if CAPA[i][j] != 0 :
                c0 = X[i,j] <= CAPA[i][j]
                m.addConstr(c0, 'c0-'+str(i)+'-'+str(j))
        
    for i in range(1, NODE-1) :
        tempC = 0
        for j in range(NODE) :
            if CAPA[i][j] != 0 :
                tempC += X[i,j]
        for k in range(NODE) :
            if CAPA[k][i] != 0 :
                tempC -= X[k,i]
        
        c1 = tempC == 0
        m.addConstr(c1, 'c1-'+str(i))
  
        
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
    
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
    
except GurobiError() : 
    print('Error reported')