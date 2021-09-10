#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:49:58 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model('ex7_3')
    
    Z = LinExpr()
    
    X = m.addVars(5, 5, vtype = GRB.BINARY, name = 'X')
    Y = m.addVars(5, vtype = GRB.BINARY, name = 'Y')
    U = m.addVars(5, vtype = GRB.INTEGER, name = 'U')
    
    NCITY = 5
    V = [10, 9, 8, 7, 100]
    C = [[0, 14, 15, 4, 9],
         [14, 0, 18, 5, 4],
         [15, 18, 0, 13, 10],
         [4, 5, 13, 0, 12],
         [9, 4, 10, 12, 0]]
    
    # 목적함수
    Z = 0
    for j in range(NCITY) : 
        for i in range(NCITY) : 
            Z += C[i][j]*X[i,j]
        Z -= V[j]*Y[j]
        
    # 제약조건 1 : 각 도시 j 는 많아야 한번 방문한다.
    for j in range(NCITY) : 
        tempC = 0
        for i in range(NCITY) :
            if (i != j) : 
                tempC += X[i,j]
        c0 = tempC == Y[j]
        m.addConstr(c0, 'c0'+str(j))
        
    # 제약조건 2 : 도시 j 는 반드시 나와야 한다.
    for i in range(NCITY) : 
        tempC2 = 0
        for j in range(NCITY) :
            if (i != j) :
                tempC2 += X[i,j]
        c1 = tempC2 == Y[i]
        m.addConstr(c1, 'c1'+str(i))
        
    # 제약조건 3 : 부분순환은 허용되지 않는다.
    for i in range(1, NCITY) :
        for j in range(NCITY) : 
            if (i != j) :
                c2 = U[i] >= U[j] + X[j,i] - (NCITY-2)*(1-X[j,i]) + (NCITY-3)*X[i,j]
                m.addConstr(c2, 'c2'+str(i)+str(j))
    
    for k in range(1, NCITY) : 
        c3 = U[k] <= (NCITY-1) - (NCITY-2)*X[0,k]
        c4 = U[k] >= 1 + (NCITY-2)*X[k,0]
        m.addConstr(c3, 'c3'+str(k))
        m.addConstr(c4, 'c4'+str(k))
    
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
    
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
    
except GurobiError() : 
    print('Error reported')
            
    
    
    