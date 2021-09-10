#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:32:31 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model('ex9_1_2')
    
    Z = LinExpr() 
    
    NODE = 7 
    
    OO = m.addVar(vtype = GRB.BINARY, name = 'OO')
    OA = m.addVar(vtype = GRB.BINARY, name = 'OA')
    OB = m.addVar(vtype = GRB.BINARY, name = 'OB')
    OC = m.addVar(vtype = GRB.BINARY, name = 'OC')
    OD = m.addVar(vtype = GRB.BINARY, name = 'OD')
    OE = m.addVar(vtype = GRB.BINARY, name = 'OE')
    OT = m.addVar(vtype = GRB.BINARY, name = 'OT')
    AO = m.addVar(vtype = GRB.BINARY, name = 'AO')
    AA = m.addVar(vtype = GRB.BINARY, name = 'AA')
    AB = m.addVar(vtype = GRB.BINARY, name = 'AB')
    AC = m.addVar(vtype = GRB.BINARY, name = 'AC')
    AD = m.addVar(vtype = GRB.BINARY, name = 'AD')
    AE = m.addVar(vtype = GRB.BINARY, name = 'AE')
    AT = m.addVar(vtype = GRB.BINARY, name = 'AT')
    BO = m.addVar(vtype = GRB.BINARY, name = 'BO')
    BA = m.addVar(vtype = GRB.BINARY, name = 'BA')
    BB = m.addVar(vtype = GRB.BINARY, name = 'BB')
    BC = m.addVar(vtype = GRB.BINARY, name = 'BC')
    BD = m.addVar(vtype = GRB.BINARY, name = 'BD')
    BE = m.addVar(vtype = GRB.BINARY, name = 'BE')
    BT = m.addVar(vtype = GRB.BINARY, name = 'BT')
    CO = m.addVar(vtype = GRB.BINARY, name = 'CO')
    CA = m.addVar(vtype = GRB.BINARY, name = 'CA')
    CB = m.addVar(vtype = GRB.BINARY, name = 'CB')
    CC = m.addVar(vtype = GRB.BINARY, name = 'CC')
    CD = m.addVar(vtype = GRB.BINARY, name = 'CD')
    CE = m.addVar(vtype = GRB.BINARY, name = 'CE')
    CT = m.addVar(vtype = GRB.BINARY, name = 'CT')
    DO = m.addVar(vtype = GRB.BINARY, name = 'DO')
    DA = m.addVar(vtype = GRB.BINARY, name = 'DA')
    DB = m.addVar(vtype = GRB.BINARY, name = 'DB')
    DC = m.addVar(vtype = GRB.BINARY, name = 'DC')
    DD = m.addVar(vtype = GRB.BINARY, name = 'DD')
    DE = m.addVar(vtype = GRB.BINARY, name = 'DE')
    DT = m.addVar(vtype = GRB.BINARY, name = 'DT')
    EO = m.addVar(vtype = GRB.BINARY, name = 'EO')
    EA = m.addVar(vtype = GRB.BINARY, name = 'EA')
    EB = m.addVar(vtype = GRB.BINARY, name = 'EB')
    EC = m.addVar(vtype = GRB.BINARY, name = 'EC')
    ED = m.addVar(vtype = GRB.BINARY, name = 'ED')
    EE = m.addVar(vtype = GRB.BINARY, name = 'EE')
    ET = m.addVar(vtype = GRB.BINARY, name = 'ET')
    TO = m.addVar(vtype = GRB.BINARY, name = 'TO')
    TA = m.addVar(vtype = GRB.BINARY, name = 'TA')
    TB = m.addVar(vtype = GRB.BINARY, name = 'TB')
    TC = m.addVar(vtype = GRB.BINARY, name = 'TC')
    TD = m.addVar(vtype = GRB.BINARY, name = 'TD')
    TE = m.addVar(vtype = GRB.BINARY, name = 'TE')
    TT = m.addVar(vtype = GRB.BINARY, name = 'TT')
    
    X = [[OO, OA, OB, OC, OD, OE, OT],
         [AO, AA, AB, AC, AD, AE, AT],
         [BO, BA, BB, BC, BD, BE, BT],
         [CO, CA, CB, CC, CD, CE, CT],
         [DO, DA, DB, DC, DD, DE, DT],
         [EO, EA, EB, EC, ED, EE, ET],
         [TO, TA, TB, TC, TD, TE, TT]]
    
    DIST = [[0, 2, 5, 4, 0, 0, 0], 
            [0, 0, 2, 0, 7, 0, 0], 
            [0, 0, 0, 1, 4, 3, 0], 
            [0, 0, 0, 0, 0, 4, 0], 
            [0, 0, 0, 0, 0, 1, 5], 
            [0, 0, 0, 0, 0, 0, 7], 
            [0, 0, 0, 0, 0, 0, 0]]
    
    # 목적 함수
    Z = 0
    for i in range(NODE) :
        for j in range(NODE) :
            Z += X[i][j]*DIST[i][j]
    
    # 제약 조건
    for i in range(NODE) :
        tempC = 0
        for j in range(NODE) :
            if DIST[i][j] != 0 :
                tempC += X[i][j]
        for k in range(NODE) :
            if DIST[k][i] != 0 :
                tempC -= X[k][i]
        
        if i == 0 :
            c0 = tempC == 1
            m.addConstr(c0, 'c0'+str(i))
        elif i == NODE - 1 :
            c0 = tempC == -1
            m.addConstr(c0, 'c0'+str(i))
        else :
            c0 = tempC == 0
            m.addConstr(c0, 'c0'+str(i))
  
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
    
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
    
except GurobiError() : 
    print('Error reported')