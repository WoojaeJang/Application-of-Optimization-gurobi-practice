#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:42:40 2021

@author: woojae-macbook13
"""

from gurobipy import*

try : 
    
    m = Model('ex9_2_2')
    
    Z = LinExpr() 
    
    NODE = 7 
    
    OO = m.addVar(vtype = GRB.INTEGER, name = 'OO')
    OA = m.addVar(vtype = GRB.INTEGER, name = 'OA')
    OB = m.addVar(vtype = GRB.INTEGER, name = 'OB')
    OC = m.addVar(vtype = GRB.INTEGER, name = 'OC')
    OD = m.addVar(vtype = GRB.INTEGER, name = 'OD')
    OE = m.addVar(vtype = GRB.INTEGER, name = 'OE')
    OT = m.addVar(vtype = GRB.INTEGER, name = 'OT')
    AO = m.addVar(vtype = GRB.INTEGER, name = 'AO')
    AA = m.addVar(vtype = GRB.INTEGER, name = 'AA')
    AB = m.addVar(vtype = GRB.INTEGER, name = 'AB')
    AC = m.addVar(vtype = GRB.INTEGER, name = 'AC')
    AD = m.addVar(vtype = GRB.INTEGER, name = 'AD')
    AE = m.addVar(vtype = GRB.INTEGER, name = 'AE')
    AT = m.addVar(vtype = GRB.INTEGER, name = 'AT')
    BO = m.addVar(vtype = GRB.INTEGER, name = 'BO')
    BA = m.addVar(vtype = GRB.INTEGER, name = 'BA')
    BB = m.addVar(vtype = GRB.INTEGER, name = 'BB')
    BC = m.addVar(vtype = GRB.INTEGER, name = 'BC')
    BD = m.addVar(vtype = GRB.INTEGER, name = 'BD')
    BE = m.addVar(vtype = GRB.INTEGER, name = 'BE')
    BT = m.addVar(vtype = GRB.INTEGER, name = 'BT')
    CO = m.addVar(vtype = GRB.INTEGER, name = 'CO')
    CA = m.addVar(vtype = GRB.INTEGER, name = 'CA')
    CB = m.addVar(vtype = GRB.INTEGER, name = 'CB')
    CC = m.addVar(vtype = GRB.INTEGER, name = 'CC')
    CD = m.addVar(vtype = GRB.INTEGER, name = 'CD')
    CE = m.addVar(vtype = GRB.INTEGER, name = 'CE')
    CT = m.addVar(vtype = GRB.INTEGER, name = 'CT')
    DO = m.addVar(vtype = GRB.INTEGER, name = 'DO')
    DA = m.addVar(vtype = GRB.INTEGER, name = 'DA')
    DB = m.addVar(vtype = GRB.INTEGER, name = 'DB')
    DC = m.addVar(vtype = GRB.INTEGER, name = 'DC')
    DD = m.addVar(vtype = GRB.INTEGER, name = 'DD')
    DE = m.addVar(vtype = GRB.INTEGER, name = 'DE')
    DT = m.addVar(vtype = GRB.INTEGER, name = 'DT')
    EO = m.addVar(vtype = GRB.INTEGER, name = 'EO')
    EA = m.addVar(vtype = GRB.INTEGER, name = 'EA')
    EB = m.addVar(vtype = GRB.INTEGER, name = 'EB')
    EC = m.addVar(vtype = GRB.INTEGER, name = 'EC')
    ED = m.addVar(vtype = GRB.INTEGER, name = 'ED')
    EE = m.addVar(vtype = GRB.INTEGER, name = 'EE')
    ET = m.addVar(vtype = GRB.INTEGER, name = 'ET')
    TO = m.addVar(vtype = GRB.INTEGER, name = 'TO')
    TA = m.addVar(vtype = GRB.INTEGER, name = 'TA')
    TB = m.addVar(vtype = GRB.INTEGER, name = 'TB')
    TC = m.addVar(vtype = GRB.INTEGER, name = 'TC')
    TD = m.addVar(vtype = GRB.INTEGER, name = 'TD')
    TE = m.addVar(vtype = GRB.INTEGER, name = 'TE')
    TT = m.addVar(vtype = GRB.INTEGER, name = 'TT')
    
    X = [[OO, OA, OB, OC, OD, OE, OT],
         [AO, AA, AB, AC, AD, AE, AT],
         [BO, BA, BB, BC, BD, BE, BT],
         [CO, CA, CB, CC, CD, CE, CT],
         [DO, DA, DB, DC, DD, DE, DT],
         [EO, EA, EB, EC, ED, EE, ET],
         [TO, TA, TB, TC, TD, TE, TT]]
    
    CAPA = [[0, 5, 7, 4, 0, 0, 0], 
            [0, 0, 1, 0, 3, 0, 0], 
            [0, 0, 0, 2, 4, 5, 0], 
            [0, 0, 0, 0, 0, 4, 0], 
            [0, 0, 0, 0, 0, 0, 9], 
            [0, 0, 0, 0, 1, 0, 6], 
            [0, 0, 0, 0, 0, 0, 0]]
    
    # 목적 함수
    Z = 0
    for j in range(NODE) :
        if CAPA[0][j] != 0 :
            Z += X[0][j]
    for k in range(NODE) :
        if CAPA[k][0] != 0 :
            Z -= X[k][0]
    
    # 제약 조건
    for i in range(NODE) :
        for j in range(NODE) :
            if CAPA[i][j] != 0 :
                c0 = X[i][j] <= CAPA[i][j]
                m.addConstr(c0, 'c0-'+str(i)+'-'+str(j))
        
    for i in range(1, NODE-1) :
        tempC = 0
        for j in range(NODE) :
            if CAPA[i][j] != 0 :
                tempC += X[i][j]
        for k in range(NODE) :
            if CAPA[k][i] != 0 :
                tempC -= X[k][i]
        
        c1 = tempC == 0
        m.addConstr(c1, 'c1-'+str(i))
  
        
    m.setObjective(Z, GRB.MAXIMIZE)
    
    m.optimize()
    
    
    for v in m.getVars() :
        if v.x != 0 :
            print(v.varName, ':', v.x)
            
    print('Z : ', m.objVal)
    
    
except GurobiError() : 
    print('Error reported')