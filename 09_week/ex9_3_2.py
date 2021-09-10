#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:57:35 2021

@author: woojae-macbook13
"""

from gurobipy import *

try:
    m = Model('ex9_3_2')
    
    Z= LinExpr()
    
    AB = m.addVar(vtype = GRB.INTEGER, name = 'AB')
    AC = m.addVar(vtype = GRB.INTEGER, name = 'AC')
    AD = m.addVar(vtype = GRB.INTEGER, name = 'AD')
    BC = m.addVar(vtype = GRB.INTEGER, name = 'BC')
    CE = m.addVar(vtype = GRB.INTEGER, name = 'CE')
    DE = m.addVar(vtype = GRB.INTEGER, name = 'DE')
    ED = m.addVar(vtype = GRB.INTEGER, name = 'ED')
    
    # 목적 함수
    Z = 2*AB + 4*AC + 9*AD + 3*BC + CE + 3*DE + 2*ED
    
    # 제약 조건
    c0 = AB + AC + AD == 50
    c1 = -AB + BC == 40
    c2 = -AC - BC + CE == 0
    c3 = -AD +DE - ED == -30
    c4 = -CE -DE + ED == -60
    
    c5 = AB <= 10
    c6 = CE <= 80
    
    c7 = AB >= 0
    c8 = AC >= 0
    c9 = AD >= 0
    c10 = BC >= 0
    c11 = CE >= 0
    c12 = DE >= 0
    c13 = ED >= 0

    m.addConstr(c0,'c0')
    m.addConstr(c1,'c1')
    m.addConstr(c2,'c2')
    m.addConstr(c3,'c3')
    m.addConstr(c4,'c4')
    m.addConstr(c5,'c5')
    m.addConstr(c6,'c6')
    m.addConstr(c7,'c7')
    m.addConstr(c8,'c8')
    m.addConstr(c9,'c9')
    m.addConstr(c10,'c10')
    m.addConstr(c11,'c11')
    m.addConstr(c12,'c12')
    m.addConstr(c13,'c13')
    

    m.setObjective(Z, GRB.MINIMIZE)
    m.optimize()
    
    for v in m.getVars():
        if v.x != 0:
            print(v.varName, ':', v.x)
    print('Z :', m.objVal)

except GurobiError:
    print('Error reported')