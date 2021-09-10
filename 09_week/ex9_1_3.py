#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 02:39:45 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model('ex9_1_3')
    
    Z = LinExpr() 
    
    NODE = 7 
    
    OA = m.addVar(vtype = GRB.BINARY, name = 'OA')
    OB = m.addVar(vtype = GRB.BINARY, name = 'OB')
    OC = m.addVar(vtype = GRB.BINARY, name = 'OC')
    
    AB = m.addVar(vtype = GRB.BINARY, name = 'AB')
    AD = m.addVar(vtype = GRB.BINARY, name = 'AD')
    
    BC = m.addVar(vtype = GRB.BINARY, name = 'BC')
    BD = m.addVar(vtype = GRB.BINARY, name = 'BD')
    BE = m.addVar(vtype = GRB.BINARY, name = 'BE')
    
    CB = m.addVar(vtype = GRB.BINARY, name = 'CB')
    CE = m.addVar(vtype = GRB.BINARY, name = 'CE')
    
    DE = m.addVar(vtype = GRB.BINARY, name = 'DE')
    DT = m.addVar(vtype = GRB.BINARY, name = 'DT')
    
    ED = m.addVar(vtype = GRB.BINARY, name = 'ED')
    ET = m.addVar(vtype = GRB.BINARY, name = 'ET')
    
    
    X = [[0, OA, OB, OC, 0, 0, 0],
         [0, 0, AB, 0, AD, 0, 0],
         [0, 0, 0, BC, BD, BE, 0],
         [0, 0, CB, 0, 0, CE, 0],
         [0, 0, 0, 0, 0, DE, DT],
         [0, 0, 0, 0, ED, 0, ET],
         [0, 0, 0, 0, 0, 0, 0]]
    
    DIST = [[0, 2, 5, 4, 0, 0, 0], 
            [0, 0, 2, 0, 7, 0, 0], 
            [0, 0, 0, 1, 4, 3, 0], 
            [0, 0, 1, 0, 0, 4, 0], 
            [0, 0, 0, 0, 0, 1, 5], 
            [0, 0, 0, 0, 1, 0, 7], 
            [0, 0, 0, 0, 0, 0, 0]]
    
    # 목적 함수
    Z = 0
    for i in range(NODE) :
        for j in range(NODE) :
            Z += X[i][j]*DIST[i][j]
    
    # 제약 조건
    for i in range(NODE) :
        tempC = 0
        # From i 더하기
        for j in range(NODE) :
            if DIST[i][j] != 0 :
                tempC += X[i][j]
        # To i 빼기
        for k in range(NODE) :
            if DIST[k][i] != 0 :
                tempC -= X[k][i]
        # 시작점 합 = 1
        if i == 0 :
            c0 = tempC == 1
            m.addConstr(c0, 'c0'+str(i))
        # 끝점 합 = -1
        elif i == NODE - 1 :
            c0 = tempC == -1
            m.addConstr(c0, 'c0'+str(i))
        # 나머지 합 = 0
        else :
            c0 = tempC == 0
            m.addConstr(c0, 'c0'+str(i))
  
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
    
    print()
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
    print()
    
    print("경로 : ", end = '')
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName[0], "-> ", end = '')
    print('T')
    print()
    
            
    print('총 거리 : ', m.objVal)
    
    
    
    
    
except GurobiError() : 
    print('Error reported')