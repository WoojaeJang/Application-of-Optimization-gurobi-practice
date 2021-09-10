#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:08:38 2021

@author: woojae-macbook13
"""
from gurobipy import *

try:
    
    m = Model("mip1")

    Z = LinExpr()
    A = m.addVar(vtype=GRB.CONTINUOUS, name='A')
    C = m.addVar(vtype=GRB.CONTINUOUS, name='C')

    Z = 20*A + 30*C
    c0 = A <= 60
    c1 = C <= 50
    c2 = A + 2*C <= 120
    
    m.setObjective(Z, GRB.MAXIMIZE)
    m.addConstr(c0, "c0")
    m.addConstr(c1, "c1")
    m.addConstr(c2, "c2")
    
    m.optimize()
    

    for v in m.getVars():
        print(v.varName, ':', v.x)
        
    print('Z:', m.objVal)
    
    
except GurobiError :
    print('Error reported')