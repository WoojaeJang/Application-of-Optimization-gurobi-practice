#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:28:54 2021

@author: woojae-macbook13
"""

from pandas import*
import pandas as pd
import numpy as np


# path = ".\\"
filename = "ex1.xlsx"
# filename = "pr1.xlsx"

# dataset = pd.read_excel(path+filename)
dataset = pd.read_excel(filename)
order = "고객"
itemcode = "itemcode"
qty = "quantity"

orderSet = Series(dataset[order].drop_duplicates().sort_values().values)
itemSet = Series(dataset[itemcode].drop_duplicates().sort_values().values)

nOrders = len(orderSet)
nItem = len(itemSet)

orderitemSetVector = {}
orderSetQtyVector = {}



#주문(key) : [아이템벡터] (value)dictionary 생성 (루프)
for i in orderSet :
    
    # 각 주문에 대한 아이템 수 크기의 0벡터 생성: one-zero 벡터 용
    tempOZvector = np.zeros(len(itemSet))
    # 각 주문에 대한 아이템 수 크기의 0벡터 생성: 수량 벡터 용
    tempQtyVector = np.zeros(len(itemSet))
    # 고객 번호가 i 인 주문이 포함하는 아이템 목록
    tempItemList = dataset[dataset[order] == i][itemcode]
    # 고객 번호가 i 인 주문이 포함하는 아이템 목록
    tempQtyList = dataset[dataset[order] == i][qty]
    
    #각 고객이 포함한 아이템에 대하여 반복
    for j in range(len(tempItemList)) :
        # 고객 번호가 i 인 주문이 포함하는 아이템을 하나씩 가져옴. 
        tempItem = tempItemList.iloc[j]
        # 현재 선택된 아이템의 위치(행번호)를 가져옴 
        tempItemIndex = itemSet[itemSet == tempItem].index[0]
        # 각 주문에 대한 ONE-ZERO 벡터를 생성: 아이템 수량 > 0 ==> 1, otherwise 0 
        # 해당 아이템을 가지므로 1을 assign 함 
        tempOZvector[tempItemIndex] = 1
        # item벡터와 같은위치에 1,0 대신 수량을 assign함
        # 각 주문에 대한 수량 벡터를 생성 
        tempQtyVector[tempItemIndex] = tempQtyList.iloc[j]
        
    orderitemSetVector[i] = tempOZvector
    orderSetQtyVector[i] = tempQtyVector
    
# 결과 확인
dfOrderItemVector = DataFrame(orderitemSetVector).T
dfOrderQtyVector = DataFrame(orderSetQtyVector).T



# 유사성 계산 함수 만들기
def calSimilarity(v1, v2) :
    inner_sum = 0
    size1 = 0.0
    size2 = 0.0
    
    for i in range(nItem) :
        size1 += v1[i]*v1[i]
        size2 += v2[i]*v2[i]
        inner_sum += v1[i]*v2[i]
        
    return inner_sum/(size1**(1/2)*size2**(1/2))



# 작업 1 : 모든 사용자 조합간 유사성 지표 계산
setSimilarity = {}

for i in orderSet :
    tempSim = np.zeros(nOrders)
    
    k = 0
    for j in orderSet :
        if i != j :
            tempSim[k] = calSimilarity(dfOrderItemVector.T[i], dfOrderItemVector.T[j])
    
        k += 1
    
    setSimilarity[i] = tempSim
    
dfSimilarity = DataFrame(setSimilarity)



# 작업 2 : 각 사용자와 가장 유사한 사용자 선정
similarone = np.zeros(nOrders)

k = 0
for i in orderSet :
    idx = 0
    value = 0.0
    for j in range(nOrders) :
        if dfSimilarity[i][j] > value :
            idx = j
            value = dfSimilarity[i][j]
            
    similarone[k] = idx
    
    k += 1
    
    print("user %d -> idx : %d" %(i, orderSet[idx]))
    
print()


    
# 작업 3 : 유사한 사용자가 구매했으나 기준 사용는 구매하지 않은 아이템

for i in range(nOrders) :
    idx = similarone[i]
    for j in range(nItem) :
        if dfOrderItemVector.T[orderSet[i]][j] == 0 and dfOrderItemVector.T[orderSet[idx]][j] != 0 :
            print("We recommend this item %d for user %d" %(j, i+1))















