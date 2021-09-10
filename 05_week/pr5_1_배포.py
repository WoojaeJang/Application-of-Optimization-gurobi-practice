# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:49:16 2019

@author: Q908
"""

from gurobipy import *

try:
    m = Model("pr_5_1")
    
    Z = LinExpr()

    P = m.addVars(8, 25, vtype=GRB.INTEGER, name='P')
    I = m.addVars(8, 25, vtype=GRB.INTEGER, name='I')
    S = m.addVars(8, 25, vtype=GRB.BINARY, name='S')
    Y = m.addVars(8, 25, vtype=GRB.BINARY, name='Y')
    UC = [0,5,5,5,5,5,5,5,5,5,25,25,25,25,25,25,25,5,5,5,5,5,5,5,5]
    PC = [15,14,16,10,17,16,15,18]
    SC = 10
    BIGM = 1000000
    
    # 목적함수
    Z = 0
    for i in range(8):
        for j in range(1,25):
            Z += UC[j] * P[i,j] + SC * S[i,j]

    # 재고제약 기계 0 - 6



       
    
    # 재고 제약 마지막 기계            




         

    # 초기재고: 기계 0 - 기계 6




         

    #초기 재고: 기계 7



    
    # 기말재고: 기계 0 - 기계 6



        
    #기말 재고 (Throughput): 기계 7 

    
    
    # 재고에 의한 생산량 제약




    

    # 생산용량에 의한 생산량 제약





  
    # 가동여부       





 
            
    # 준비비용 발생 여부       




            
    # 첫 기간에 대한 준비 비용 발생여부




       
    
    m.setObjective(Z, GRB.MINIMIZE)
    
    m.optimize()
            
    for v in m.getVars():
        if v.x != 0:
            print(v.varName, v.x)
                
    print('Obj:', m.objVal)
    
    m.write("out.lp")
    m.write("out.sol")
        
except GurobiError:
    print('Error reported')
