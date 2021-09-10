#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:59:53 2021

@author: woojae-macbook13
"""

from pulp import *

prob = LpProblem("Pr1_2", LpMaximize)

A=LpVariable("Astro",0)
C=LpVariable("Cosmo", cat='Integer')
imsi=LpVariable("imsi", cat='Integer')

prob += 20*A + 30*C

prob += A <= 60, "Astro Line Capacity"
prob += C <= 50, "Cosmo Line Capacity"
prob += A + 2*C <= 158, "Labor Capacity"
prob += C == 2*imsi

prob.writeLP("Pr1_2.lp")

prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)
    
print("Total profit = ", value(prob.objective))