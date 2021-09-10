#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:16:37 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model('ex9_3_3')
    
    Z = LinExpr() 
    
    NODE = 5 
    
    AB = m.addVar(vtype = GRB.INTEGER, name = 'AB')
    AC = m.addVar(vtype = GRB.INTEGER, name = 'AC')
    AD = m.addVar(vtype = GRB.INTEGER, name = 'AD')
    BC = m.addVar(vtype = GRB.INTEGER, name = 'BC')
    CE = m.addVar(vtype = GRB.INTEGER, name = 'CE')
    DE = m.addVar(vtype = GRB.INTEGER, name = 'DE')
    ED = m.addVar(vtype = GRB.INTEGER, name = 'ED')
    
    X = [[0, AB, AC, AD, 0],
         [0, 0, BC, 0, 0], 
         [0, 0, 0, 0, CE],
         [0, 0, 0, 0, DE],
         [0, 0, 0, ED, 0]]
    
    COST = [[0, 2, 4, 9, 0],
            [0, 0, 3, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 3],
            [0, 0, 0, 2, 0]]
    
    CAPA = [[0, 10, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 80],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    
    B = [50, 40, 0, -30, -60]
    
    # 목적 함수
    Z = 0
    for i in range(NODE) :
        for j in range(NODE) :
            Z += X[i][j]*COST[i][j]
            
    # 제약 조건
    for i in range(NODE) :
        tempC = 0
        for j in range(NODE) :
            if COST[i][j] != 0 :
                tempC += X[i][j]
        for k in range(NODE) :
            if COST[k][i] != 0 :
                tempC -= X[k][i]
                
        c0 = tempC == B[i]
        m.addConstr(c0, 'c0-'+str(i))
        
    for i in range(NODE) :
        for j in range(NODE) :
            if CAPA[i][j] != 0 :
                c1 = X[i][j] <= CAPA[i][j]
                m.addConstr(c1, 'c1-'+str(i)+'-'+str(j))
                
    for i in range(NODE) :
        for j in range(NODE) :
            c2 = X[i][j] >= 0
            m.addConstr(c2, 'c2-'+str(i)+'-'+str(j))
            
            
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
    
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
    
except GurobiError() : 
    print('Error reported')