#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:42:17 2021

@author: woojae-macbook13
"""

from gurobipy import*

try :
    
    m = Model("Ex2_2")
    x = m.addVars(7, vtype = GRB.INTEGER, name='x')
    REQ = [20, 16, 13, 16, 19, 14, 12]
    Z = LinExpr() # 선언
    Z = x.sum('*') # x 를 모두 더해라
    c = (sum(x[(j-i)%7] for i in range(5)) >= REQ[j] for j in range(7))
    m.addConstrs(c, 'c')
    m.setObjective(Z, GRB.MINIMIZE)
    m.optimize()
    
    for v in m.getVars():
        print(v.varName, ':', v.x)
        
    print('Z : ', m.objVal)
    
except GurobiError :
    print('Error reported')    
    
