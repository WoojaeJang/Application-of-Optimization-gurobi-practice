#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:01:35 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model('ex9_4_2')
    
    Z = LinExpr()
    
    NODE = 14
    
    X = m.addVars(NODE, vtype = GRB.INTEGER, name = 'X')
    Y = m.addVars(NODE + 1, vtype = GRB.INTEGER, name = 'Y')
    
    N_TIME = [2, 4, 10, 6, 4, 5, 7, 9, 7, 8, 4, 5, 2, 6]
    N_COST = [180000, 320000, 620000, 260000, 410000, 180000, 900000, 200000, 210000, 430000, 160000, 250000, 100000, 330000]
    C_COST = [100000, 50000, 80000, 40000, 160000, 40000, 40000, 60000, 30000, 30000, 40000, 50000, 100000, 60000]
    C_MAXTIME = [1, 2, 3, 2, 1, 2, 3, 3, 2, 2, 1, 2, 1, 3]
    
    # 목적 함수
    Z = 0
    for i in range(NODE) :
        Z += X[i]*C_COST[i] + N_COST[i]
        
    # 제약 조건 1 (최대 공기 단축 제약)
    for i in range(NODE) : 
        m.addConstr(X[i] <= C_MAXTIME[i], 'c0'+str(i))
    
    # 제약 조건 2 (시작 시간 제약)
    m.addConstr(Y[0] == 0, 'c1') # START -> A(0)(A의 시작시간 Y[0] == 0)
     
    m.addConstr(Y[1] >= Y[0] + N_TIME[0] - X[0], 'c2') # B(1) <- A(0) 
    m.addConstr(Y[2] >= Y[1] + N_TIME[1] - X[1], 'c3') # C(2) <- B(1)
    m.addConstr(Y[3] >= Y[2] + N_TIME[2] - X[2], 'c4') # D(3) <- C(2)
    m.addConstr(Y[4] >= Y[2] + N_TIME[2] - X[2], 'c5') # E(4) <- C(2)
    m.addConstr(Y[5] >= Y[4] + N_TIME[4] - X[4], 'c6') # F(5) <- E(4)
    m.addConstr(Y[6] >= Y[3] + N_TIME[3] - X[3], 'c7') # G(6) <- D(3)
    m.addConstr(Y[7] >= Y[4] + N_TIME[4] - X[4], 'c8') # H(7) <- E(4)
    m.addConstr(Y[7] >= Y[6] + N_TIME[6] - X[6], 'c9') # H(7) <- G(6)
    m.addConstr(Y[8] >= Y[2] + N_TIME[2] - X[2], 'c10') # I(8) <- C(2)
    m.addConstr(Y[9] >= Y[5] + N_TIME[5] - X[5], 'c11') # J(9) <- F(5)
    m.addConstr(Y[9] >= Y[8] + N_TIME[8] - X[8], 'c12') # J(9) <- I(8)
    m.addConstr(Y[10] >= Y[9] + N_TIME[9] - X[9], 'c13') # K(10) <- J(9)
    m.addConstr(Y[11] >= Y[9] + N_TIME[9] - X[9], 'c14') # L(11) <- J(9)
    m.addConstr(Y[12] >= Y[7] + N_TIME[7] - X[7], 'c15') # M(12) <- H(7)
    m.addConstr(Y[13] >= Y[10] + N_TIME[10] - X[10], 'c16') # N(13) <- K(10)
    m.addConstr(Y[13] >= Y[11] + N_TIME[11] - X[11], 'c17') # N(13) <- L(11)
    m.addConstr(Y[14] >= Y[12] + N_TIME[12] - X[12], 'c18') # FINISH(14) <- M(12)
    m.addConstr(Y[14] >= Y[13] + N_TIME[13] - X[13], 'c19') # FINISH(14) <- N(13)
       
    # 제약 조건 3 (전체 프로젝트 기간 제약)
    m.addConstr(Y[14] <= 40, 'c20')
      
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
    
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
    
except GurobiError() : 
    print('Error reported')
    
    