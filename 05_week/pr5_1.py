#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:28:04 2021

@author: woojae-macbook13
"""

from gurobipy import*
import numpy as np
import matplotlib.pyplot as plt

try : 
    
    m = Model("pr5_1")
    
    Z = LinExpr()
    
    I = m.addVars(8, 25, vtype=GRB.INTEGER, name='I')
    P = m.addVars(8, 25, vtype=GRB.INTEGER, name='P')
    Y = m.addVars(8, 25, vtype=GRB.BINARY, name='Y')
    S = m.addVars(8, 25, vtype=GRB.BINARY, name='S')
    
    UC = [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 25, 25, 25, 25, 25, 25, 25, 5, 5, 5, 5, 5, 5, 5, 5]
    PC = [15, 14, 16, 10, 17, 16, 15, 18]
    SC = 100
    
    Z = 0
    for i in range(0, 8) :
        for j in range(1, 25) :
            Z += UC[j]*P[i, j] + SC*S[i, j]
    
    # 재고 제약 (기계 0-6)
    for i in range(0, 7) :
        for j in range(1, 25) :
            c0 = 0
            c0 = I[i, j] == I[i,j-1] + P[i, j] - P[i+1, j]
            m.addConstr(c0, 'c0'+str(i)+str(j))
         
    # 재고 제약 (마지막 기계 7)
    for j in range(1, 25) :
        c1 = 0
        c1 = I[7, j] == I[7, j-1] + P[7, j]
        m.addConstr(c1, 'tem'+str(j))
    
    
    # 초기 재고 (기계 0~6)
    for i in range(0, 7) :
        c2 = 0
        c2 = I[i,0] == 2*PC[i+1]
        m.addConstr(c2, 'c2'+str(i))
        
    # 초기 재고 (마지막 기계 7)
    c3 = 0
    c3 = I[7,0] == 0
    m.addConstr(c3, 'c3')    
    
    # 기말 재고 (기계 0~6)
    for i in range(0, 7) : 
        c4 = 0
        c4 = I[i,24] == 2*PC[i+1]
        m.addConstr(c4, 'c4'+str(i))
    
    # 기말 재고 (마지막 기계 7) - Throughput
    c5 = 0
    c5 = I[7, 24] == 240
    m.addConstr(c5, 'c5')    
    
    # 재고에 의한 생산량 제약
    for i in range(1, 8) :
        for j in range (1, 25) :
            c6 = 0
            c6 = P[i, j] <= I[i-1, j-1]
            m.addConstr(c6, 'c6'+str(i)+str(j))    
    
    # 생산용량에 의한 생산량 제약
    for i in range(0, 8) :
        for j in range(1, 25) : 
            c7 = 0
            c7 = P[i, j] <= PC[i]*Y[i,j]
            m.addConstr(c7, 'c7'+str(i)+str(j))
    
    # 가동 여부
    M = 1000000000
    for i in range(0, 8) : 
        for j in range(1, 25) :
            c8 = 0
            c8 = P[i, j] <= M*Y[i, j]
            c9 = 0
            c9 = P[i, j] >= Y[i, j]
            m.addConstr(c8, 'c8'+str(i)+str(j))
            m.addConstr(c9, 'c9'+str(i)+str(j))   
    
    # 준비 비용 발생 여부
    for i in range(0, 8) : 
        for j in range(1, 25) : 
            c10 = 0
            c10 = S[i, j] >= Y[i, j] - Y[i, j-1]
            m.addConstr(c10, 'c10'+str(i)+str(j))
            
    for i in range(0, 8) :
        c11 = 0
        c11 = S[i, 1] == Y[i, 1]
        m.addConstr(c11, 'c11'+str(i))
    
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
    
    
#    for v in m.getVars():
#        if v.x != 0 :
#            print(v.varName, ':', v.x)
#        
#    print('Z : ', m.objVal)

     
    PD = np.zeros((9,25))
    
    count = 0
    quotient = 0
    remainder = 0
    
    for v in m.getVars() :
        if (v.varName[0] == "P") :
            PD[count // 25, count % 25] = v.x
            print(v.varName, count // 35, count % 25, PD[count // 25, count%25])
            count = count + 1
    
    # 그래프 그리기  
    for i in range(8) :
        plt.plot(PD[i][:], label=i)
        plt.legend()
        
    plt.plot(PD[0][:])
    
            
    print('Z : ', m.objVal)
    
    m.write("pr5_1.lp")
    # m.write("out.mps)
    m.write("out.sol")
       
            
except GurobiError : 
    print('Error reported')
            
    