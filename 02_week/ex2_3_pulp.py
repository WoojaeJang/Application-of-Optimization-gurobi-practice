#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:12:52 2021

@author: woojae-macbook13
"""

from pulp import *
import numpy as np
import pandas as pd

# Read data from a excel file
df = pd.read_excel('예제파일.xlsx')

# 최적화 모델 생성 LpMaximize or LpMinimize
prob = LpProblem("ex2_3_p", LpMaximize)

# 변수생성
Pawn = LpVariable("Pawn",0)
Knight = LpVariable("Knight",0)
Bishop = LpVariable("Bishop",0)
King = LpVariable("King",0)

# 파라미터 설정
SUPPLY = (df.loc[:, 'Supply'])[0:2].values
PRICE = (df.loc[2,:])[1:5].values
PEANUT = (df.loc[0,:])[1:5].values
CASSHEW = (df.loc[1,:])[1:5].values

BRANDS = np.array([Pawn, Knight, Bishop, King])

# 첫 목적함수
prob += lpSum(BRANDS*PRICE)

# 제약조건들
prob += lpSum(BRANDS*PEANUT/16) <= SUPPLY[0]
prob += lpSum(BRANDS*CASSHEW/16) <= SUPPLY[1]

prob.writeLP("ex2_3_pulp.lp")

prob.solve()

print("Status :", LpStatus[prob.status])


data = {}

for v in prob.variables():
    #최적해에서의 각 변수 값
    print(v.name, "=", v.varValue)
    data[v.name]=[v.varValue]
    
# 최적해에서의 목적함수 값
print("Total profit = ", value(prob.objective))
df2 = pd.DataFrame(data, index=['value']).T
df2.to_excel('ex2_3_pulp_result.xlsx')


