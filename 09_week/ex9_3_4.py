#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:26:22 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model('ex9_3_4')
    
    Z = LinExpr() 
    
    NODE = 5 
    
    AA = m.addVar(vtype = GRB.INTEGER, name = 'AA')
    AB = m.addVar(vtype = GRB.INTEGER, name = 'AB')
    AC = m.addVar(vtype = GRB.INTEGER, name = 'AC')
    AD = m.addVar(vtype = GRB.INTEGER, name = 'AD')
    AE = m.addVar(vtype = GRB.INTEGER, name = 'AE')
    BA = m.addVar(vtype = GRB.INTEGER, name = 'BA')
    BB = m.addVar(vtype = GRB.INTEGER, name = 'BB')
    BC = m.addVar(vtype = GRB.INTEGER, name = 'BC')
    BD = m.addVar(vtype = GRB.INTEGER, name = 'BD')
    BE = m.addVar(vtype = GRB.INTEGER, name = 'BE')
    CA = m.addVar(vtype = GRB.INTEGER, name = 'CA')
    CB = m.addVar(vtype = GRB.INTEGER, name = 'CB')
    CC = m.addVar(vtype = GRB.INTEGER, name = 'CC')
    CD = m.addVar(vtype = GRB.INTEGER, name = 'CD')
    CE = m.addVar(vtype = GRB.INTEGER, name = 'CE')
    DA = m.addVar(vtype = GRB.INTEGER, name = 'DA')
    DB = m.addVar(vtype = GRB.INTEGER, name = 'DB')
    DC = m.addVar(vtype = GRB.INTEGER, name = 'DC')
    DD = m.addVar(vtype = GRB.INTEGER, name = 'DD')
    DE = m.addVar(vtype = GRB.INTEGER, name = 'DE')
    EA = m.addVar(vtype = GRB.INTEGER, name = 'EA')
    EB = m.addVar(vtype = GRB.INTEGER, name = 'EB')
    EC = m.addVar(vtype = GRB.INTEGER, name = 'EC')
    ED = m.addVar(vtype = GRB.INTEGER, name = 'ED')
    EE = m.addVar(vtype = GRB.INTEGER, name = 'EE')
    
    X = [[AA, AB, AC, AD, AE],
         [BA, BB, BC, BD, BE],
         [CA, CB, CC, CD, CE],
         [DA, DB, DC, DD, DE],
         [EA, EB, EC, ED, EE]]
    
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