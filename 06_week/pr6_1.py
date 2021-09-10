#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:30:02 2021

@author: woojae-macbook13
"""

from gurobipy import *

try: 
    
    m = Model("pr6_1")
    
    nCity = 6
    
    DIST = [    [0, 702, 454, 842, 2396, 1196],
                [702, 0, 324, 1093, 2136, 764],
                [454, 324, 0, 1137, 2180, 798],
                [842, 1093, 1137, 0, 1616, 1857],
                [2396, 2136, 2180, 1616, 0, 2900],
                [1196, 764, 798, 1857, 2900, 0]
            ]
        
    X = m.addVars(nCity, nCity, vtype=GRB.BINARY, name='X')
    U = m.addVars(nCity, vtype=GRB.INTEGER, name='U')
    
    # 목적함수
    Z = 0
    for i in range(nCity):
        for j in range(nCity):
            Z += DIST[i][j] * X[i,j]
            
    # 제약조건
    # 도시 i로 한 번은 들어와야 한다.
    for j in range(nCity):
        result = 0
        for i in range(nCity):
            if (i != j):
                result += X[i, j]
        c0 = result == 1
        m.addConstr(c0,'c0'+str(j))         

           
    # 도시 i에서 한 번은 나와야 한다.
    for j in range(nCity):
        result = 0
        for k in range(nCity):
            if (j != k): 
                result += X[j, k]
        c1 = result == 1
        m.addConstr(c1,'c1'+str(j))        

        
    #방문 순서 제약
    for i in range(1,nCity):
        for j in range(1,nCity):
            if (i != j):
                c2 = U[i] >= U[j] + X[j,i] - (nCity-2)*(1-X[j,i]) + (nCity-3)*X[i,j]
                m.addConstr(c2, 'c2'+str(i)+str(j))
        
  
    #출발도시와의 관계
    for k in range(1,nCity):
        c3 = U[k] <= nCity-1 - (nCity-2)*X[0,k]
        c4 = U[k] >= 1 + (nCity-2)*X[k,0]
        m.addConstr(c3, 'c3'+str(k))
        m.addConstr(c4, 'c4'+str(k))


    m.setObjective(Z, GRB.MINIMIZE)    
    m.optimize()
    
    for v in m.getVars():
         if v.x != 0:
            print(v.varName,': ', v.x)
            
    print('Z:', m.objVal)
    
    m.write("pr6_1.lp")
    m.write("pr6_1.sol")
        
except GurobiError:
    print('Error reported')