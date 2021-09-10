#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:29:29 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model("Pr2_1")
    x = m.addVars(24, vtype = GRB.INTEGER, name='x')
    REQ = [2, 2, 2, 2, 2, 2, 8, 8, 8, 8, 4, 4, 3, 3, 3, 3, 6, 6, 5, 5, 5, 5, 3, 3]
    
    Z = LinExpr()
    Z = x.sum('*') 
    
    c = (sum(x[(j-i)%24] for i in range(0,9) if i !=4) >= REQ[j] for j in range(0,24))
    
    m.addConstrs(c, 'c')
    m.setObjective(Z, GRB.MINIMIZE)
    m.optimize()
    
    for v in m.getVars():
        if v.x != 0 :
            print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
   
    
except GurobiError :
    print('Error reported')  