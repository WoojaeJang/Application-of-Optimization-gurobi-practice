#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:25:52 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    m = Model("pr3_1")
    
    Z = LinExpr()
    
    B = m.addVar(vtype = GRB.INTEGER, name='B')
    S = m.addVar(vtype = GRB.INTEGER, name='S')
    
    Z += 4800*B + 5250*S - 600*B - 750*S
    
    c0 = 4*B + 2*S <= 160
    c1 = 2*B + 3*S <= 180
    
    m.addConstr(c0, "c0")
    m.addConstr(c1, "c1")
    
    m.setObjective(Z, GRB.MAXIMIZE)
    m.optimize()
    
    for v in m.getVars():
        print(v.varName,':',v.x)
        
    print('Z:', m.objVal)
    


except GurobiError:
    print('Error reported')