#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:32:07 2021

@author: woojae-macbook13
"""

from pulp import *

prob = LpProblem("Pr1_1", LpMaximize)

A=LpVariable("Astro",0)
C=LpVariable("Cosmo",0)

prob += 20*A + 30*C, "Total Profit"

prob += A <= 60, "Astro Line Capacity"
prob += C <= 60, "Cosmo Line Capacity"
prob += A + 2*C <= 120, "Labor Capacity"

prob.writeLP("Pr1_1.lp")

prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)
    
print("Total profit = ", value(prob.objective))