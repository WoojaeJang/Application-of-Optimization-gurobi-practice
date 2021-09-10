#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:03:44 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model("ex4_1_2")
    
    Z = LinExpr()
    E = m.addVars(4, vtype = GRB.BINARY, name = 'E')
    S = m.addVars(4, vtype = GRB.BINARY, name = 'S')
    VAL_E = [4.5, 7.8, 3.6, 2.9]
    VAL_S = [4.9, 7.2, 4.3, 3.1]
    
    for i in range(0, 4):
        Z += VAL_E[i]*E[i] + VAL_S[i]*S[i]
    
    # 제약식 1
    tempC = 0
    for i in range(0, 4):
        tempC = E[i] + S[i]
        c0 = tempC == 1
        m.addConstr(c0, 'c0'+str(i))
    
    # 제약식 2
    tempE = 0
    for i in range(0, 4):
        tempE += E[i]
    c1 = tempE == 2
    
    # 제약식 3
    tempS = 0
    for i in range(0, 4):
        tempS += S[i]
    c2 = tempS == 2
    
    m.addConstr(c1, 'c1')
    m.addConstr(c2, 'c2')
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
        
    for v in m.getVars():
        print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
    
    
except GurobiError:
    print('Error reported')
        