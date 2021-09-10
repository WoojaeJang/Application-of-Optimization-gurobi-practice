#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:55:25 2021

@author: woojae-macbook13
"""

from gurobipy import*
import numpy as np
import pandas as pd

try : 
    
    # Create a new model
    df = pd.read_excel('예제파일.xlsx')
    m = Model("ex2_3")
    
    # Create variables
    Pawn = m.addVar(lb=0.0, ub=GRB.INFINITY, obj=0.0, vtype=GRB.CONTINUOUS, name="Pawn")
    Knight = m.addVar(lb=0.0, ub=GRB.INFINITY, obj=0.0, vtype=GRB.CONTINUOUS, name="Knight")
    Bishop = m.addVar(lb=0.0, ub=GRB.INFINITY, obj=0.0, vtype=GRB.CONTINUOUS, name="Bishop")
    King = m.addVar(lb=0.0, ub=GRB.INFINITY, obj=0.0, vtype=GRB.CONTINUOUS, name="King")
    
    SUPPLY = (df.loc[:, 'Supply'])[0:2].values
    BRANDS = np.array([Pawn, Knight, Bishop, King])
    PRICE = (df.loc[2, :])[1:5].values
    PEANUT = (df.loc[0, :])[1:5].values
    CASSHEW = (df.loc[1, :])[1:5].values
    
    # Set objective
    Z = LinExpr()
    Z += np.sum(BRANDS*PRICE)
    c0 = np.sum(BRANDS*PEANUT/16) <= SUPPLY[0]
    c1 = np.sum(BRANDS*CASSHEW/16) <= SUPPLY[1]
    
    m.addConstr(c0, "const0")
    m.addConstr(c1, "const1")
    m.setObjective(Z, GRB.MAXIMIZE)
    m.optimize()
    
    data={}
    for v in m.getVars():
        print(v.varName, v.x)
        data[v.varName] = [v.x]
    
    print('Obj : ', m.objVal)
        
    
    df2 = pd.DataFrame(data, index=['value']).T
    df2.to_excel('ex2_3_result.xlsx')
    
    
except GurobiError :
    print('Error reproted')
    
    