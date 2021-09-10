# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:26:18 2019

@author: Q908
"""

from gurobipy import *

try: 
    
    m = Model("tsp")
    
    nCity = 6
    
    DIST = [    [0, 702, 454, 842, 2396, 1196],
                [702, 0, 324, 1093, 2136, 764],
                [454, 324, 0, 1137, 2180, 798],
                [842, 1093, 1137, 0, 1616, 1857],
                [2396, 2136, 2180, 1616, 0, 2900],
                [1196, 764, 798, 1857, 2900, 0]
            ]
        
    X = m.addVars(nCity, nCity, vtype=GRB.BINARY, name='X')
    U = m.addVars(nCity, vtype=GRB.INTEGER, name='U')
    
    # 목적함수
    Z = 0
    for i in range(nCity):
        for j in range(nCity):
            Z += DIST[i][j] * X[i,j]
            
    # 제약조건
    # 도시 i로 한 번은 들어와야 한다.
        

           
    # 도시 i에서 한 번은 나와야 한다.        


        
    #방문 순서 제약

  
    #출발도시와의 관계



    m.setObjective(Z, GRB.MINIMIZE)    
    m.optimize()
    
    for v in m.getVars():
         if v.x != 0:
            print(v.varName,': ', v.x)
            
    print('Z:', m.objVal)
    
    m.write("pr6_1.lp")
    m.write("pr6_1.sol")
        
except GurobiError:
    print('Error reported')