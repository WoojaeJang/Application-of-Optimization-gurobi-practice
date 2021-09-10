#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:24:30 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model("ex3_1")
    
    # 정보
    Rating = [['-', 9, 3, 4, 2, 1, 5, 6],
              ['-', '-', 1, 7, 3, 5, 2, 1],
              ['-', '-', '-', 4, 4, 2, 9, 2],
              ['-', '-', '-', '-', 1, 5, 5, 2],
              ['-', '-', '-', '-', '-', 8, 7, 6],
              ['-', '-', '-', '-', '-', '-', 2, 3],
              ['-', '-', '-', '-', '-', '-', '-', 4]]
    
    # 의사결정변수
    x = m.addVars(8, 8, vtype=GRB.BINARY, name = 'x')
    
    # 목적함수
    Z = LinExpr()
    
    for i in range(7):
        for j in range(8):
            if j>i:
                Z += Rating[i][j]*x[i,j]
                
    # 제약식1
    for i in range(8):
        tempC = 0
        for j in range(8):
            if j != i:
                tempC += x[i,j]
                
        m.addConstr(tempC==1, 'c1_'+str(i)+str(j))
    
    # 제약식2            
    for i in range(8):
        for j in range(8):
            tempC = 0
            if i<j:
                tempC = (x[i,j] - x[j,i] == 0)
                
                m. addConstr(tempC, 'c2_'+str(i)+str(j))
                    
    
    m.setObjective(Z, GRB.MINIMIZE)
    m.optimize()
    
    for v in m.getVars():
        print(v.varName,':',v.x)
        
    print('Z:', m.objVal)
                
      
        
except GurobiError :
    print('Error reproted')