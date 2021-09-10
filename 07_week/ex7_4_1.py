#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:11:06 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model('ex7_4_1')
    
    Z = LinExpr()
    
    X = m.addVars(10, 10, vtype = GRB.BINARY, name= 'X')
    S = m.addVars(10, 10, 10, vtype = GRB.BINARY, name = 'S')
    RANK = m.addVars(10, vtype = GRB.INTEGER, name = 'RANK')
    
    C = [[0, 2, 2, 3, 3, 5, 5, 5, 4, 4],
         [4, 0, 3, 3, 4, 3, 2, 3, 2, 2],
         [4, 3 ,0, 3, 5, 4, 3, 2, 4, 4],
         [3, 3, 3, 0, 5, 6, 3, 4, 4, 3],
         [3, 2, 1, 1, 0, 1, 4, 4, 5, 3],
         [1, 3, 2, 0, 5, 0, 5, 4, 1, 4],
         [1, 4, 3, 3, 2, 1, 0, 2, 1, 3],
         [1, 3, 4, 2, 2, 2, 4, 0, 4, 2],
         [2, 4, 2, 2, 1, 5, 5, 2, 0, 4],
         [2, 4, 2, 3, 3, 2, 3, 4, 2, 0]]
    NITEM = 10
    
    # 목적함수
    Z = 0
    for i in range(NITEM) : 
        for j in range(NITEM) : 
            if (i < j) : 
                Z += C[i][j]*X[i,j]
            elif (i > j) :
                Z += C[i][j]*(1-X[j,i])
            
    # 제약조건
    for i in range(NITEM) : 
        for j in range(NITEM) :
            if(i < j) : 
                c0 = X[i,j] + X[j,i] == 1
                m.addConstr(c0, 'c0'+str(i*10)+str(j))
                
    for i in range(NITEM) : 
        for j in range(NITEM) :
            for k in range(NITEM) : 
                if (i < j and j < k) : 
                    c1 = X[i,j] + X[j,k] - X[i,k] + S[i,j,k] == 1
                    m.addConstr(c1, 'c1'+str(i*10)+str(j*10)+str(k))
    
    # 랭크
    for i in range(NITEM) : 
        tempC = RANK[i]
        for j in range(NITEM) : 
            if (i < j) :
                tempC += (-1)*(1-X[i,j])
            elif (j < i) :
                tempC += (-1)*X[j,i]
        m.addConstr(tempC == 1, 'R_'+str(i))
     
    
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
    
    
    for v in m.getVars() :
        if v.x != 0:
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
except GurobiError() : 
    print('Error reported')
    