#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:21:22 2021

@author: woojae-macbook13
"""

from gurobipy import*

try:
    
    # Create a new model
    m = Model("mip1")
    
    # Create variables
    x = m.addVar(vtype=GRB.BINARY, name="x")
    y = m.addVar(vtype=GRB.BINARY, name="y")
    z = m.addVar(vtype=GRB.BINARY, name="z")
    
    # Set objective
    m.setObjective(x + y + 2*z, GRB.MAXIMIZE)
    
    # Add constraint : x + 2y + 3z <= 4
    m.addConstr(x + 2*y + 3*z <= 4, "c0")
    
    # Add constraint : x + y >= 1
    m.addConstr(x + y >= 1, "c1")
    
    
    m.optimize()
    
    for v in m.getVars():
        print(v.varName, v.x)
        
    print('Obj:', m.objVal)
    
    
    
except GurobiError:
    print('Error reported')
    