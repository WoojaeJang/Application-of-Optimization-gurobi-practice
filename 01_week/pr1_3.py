#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:06:20 2021

@author: woojae-macbook13
"""

from pulp import *

prob = LpProblem("Pr1_3", LpMaximize)

T=LpVariable("T", cat='Integer')
L=LpVariable("L", cat='Integer')

prob += 40*T + 30*L

prob += 3*T + 2*L <= 6000, "Delivery Capacity"
prob += 2*T >= L, "minimum production"

prob.writeLP("Pr1_3.lp")

prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)
    
print("Total profit = ", value(prob.objective))