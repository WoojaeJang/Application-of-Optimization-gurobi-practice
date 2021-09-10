#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:41:34 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    m = Model("pr3_2")
    
    Z = LinExpr()
    
    A = m.addVar(vtype=GRB.INTEGER, name='A')
    B = m.addVar(vtype=GRB.INTEGER, name='B')
    C = m.addVar(vtype=GRB.INTEGER, name='C')
    
    Z += 240*A + 225*B + 425*C
    
    c0 = 3*A + 5*B + 6*C <= 490
    c1 = 2*A + 1.5*B + 3*C <= 165 
    
    
    m.addConstr(c0, "c0")
    m.addConstr(c1, "c1")
    
    m.setObjective(Z, GRB.MAXIMIZE)
    m.optimize()
    
    for v in m.getVars():
        print(v.varName,':',v.x)
        
    print('Z:', m.objVal)
    


except GurobiError:
    print('Error reported')    
    
    