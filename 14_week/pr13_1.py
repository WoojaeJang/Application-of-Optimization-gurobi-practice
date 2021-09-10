#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:50:52 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
   
    m = Model("pr13_1")
    
    Z = LinExpr()
    
    NTIME = 24
    
    X = m.addVars(24, vtype = GRB.CONTINUOUS, name = 'X')
    
    QCPV = m.addVars(NTIME, vtype = GRB.CONTINUOUS, name = 'QCPV')
    QDPV = m.addVars(NTIME, vtype = GRB.CONTINUOUS, name = 'QDPV')
    ESS = m.addVars(NTIME + 1, vtype = GRB.CONTINUOUS, name = 'ESS')
    
    Y1 = m.addVars(NTIME, vtype = GRB.BINARY, name = 'Y1')
    Y2 = m.addVars(NTIME, vtype = GRB.BINARY, name = 'Y2')
    
    W = m.addVars(NTIME, vtype = GRB.CONTINUOUS, name = 'W')
    
    Z1 = m.addVars(NTIME, vtype = GRB.BINARY, name = 'Z1')
    Z2 = m.addVars(NTIME, vtype = GRB.BINARY, name = 'Z2')
    
    BIGM = 1000000
    
    SMP = [5,5,5,5,5,5,10,10,10,10,15,15,15,15,15,15,10,10,10,10,5,5,5,5]
    SMP = [5,5,5,5,5,5,10,10,10,10,15,15,15,15,15,15,10,10,10,10,5,5,5,5] #판매가격
    RPV = [0,0,0,0,0,0,0,0,0,0,5000,5000,5000,5000,5000,5000,0,0,0,0,0,0,0,0]
    RPV = [0,0,0,0,0,0,0,0,0,0,5000,5000,5000,5000,5000,5000,0,0,0,0,0,0,0,0] #REC for 태양광발전 저장용
    FPV = [0,0,0,0,0,0,0.4,0.8,1.4,2.2,2.8,3.0,2.8,2.6,2.2,1.6,1.0,0.4,0.2,0,0,0,0,0]
    FPV = [0,0,0,0,0,0,0.4,0.8,1.4,2.2,2.8,3.0,2.8,2.6,2.2,1.6,1.0,0.4,0.2,0,0,0,0,0] # 태양광 전력 생산량 
    
    
    # 목적함수
    for i in range(NTIME) :
        Z += SMP[i]*X[i] + RPV[i]*QCPV[i]
    
    
    # 제약식 1
    for i in range(NTIME) :
        c0 = 0
        c0 = X[i] <= FPV[i] + ESS[i]
        m.addConstr(c0, 'c0_' + str(i))
    
    # 제약식 2
    for i in range(NTIME) :
        c1 = 0
        c1 = ESS[i+1] == ESS[i] + QCPV[i] - QDPV[i]
        m.addConstr(c1, 'c1_' + str(i))
        
    # 제약식 3
    for i in range(NTIME) :
        c2 = 0
        c2 = QCPV[i] <= BIGM*Y1[i]
        m.addConstr(c2, 'c2_' + str(i))
        
    for i in range(NTIME) :
        c3 = 0
        c3 = QDPV[i] <= BIGM*Y2[i]
        m.addConstr(c3, 'c3_' + str(i))
        
    for i in range(NTIME) :
        c4 = 0
        c4 = Y1[i] + Y2[i] <= 1
        m.addConstr(c4, 'c4_' + str(i))
        
    # 제약식 4
    for i in range(NTIME) :
        c5 = QCPV[i] <= W[i]
        m.addConstr(c5, 'c5_' + str(i))
        
    for i in range(NTIME) :
        c6 = 0
        c6 = FPV[i] - X[i] <= W[i]
        m.addConstr(c6, 'c6_' + str(i))
        
    for i in range(NTIME) :
        c7 = 0
        c7 = W[i] <= FPV[i] - X[i] + BIGM*Z1[i]
        m.addConstr(c7, 'c7_' + str(i))
            
    for i in range(NTIME) :
        c8 = 0
        c8 = W[i] <= BIGM*Z2[i]
        m.addConstr(c8, 'c8_' + str(i))
        
    for i in range(NTIME) :
        c9 = 0
        c9 = Z1[i] + Z2[i] <= 1
        m.addConstr(c9, 'c9_' + str(i))
    
    # 제약식 5
    for i in range(NTIME) :
        c10 = 0
        c10 = QDPV[i] >= X[i] - FPV[i]
        m.addConstr(c10, 'c10_' + str(i))
    
    # 제약식 6
    c11 = ESS[0] == 0
    m.addConstr(c11, 'c11')
    
    
    
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
    
    for v in m.getVars():
        if v.x != 0:
            print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
            
        
    
except GurobiError : 
    print('Error reported')
                
    
    