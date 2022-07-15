from ast import Return
from hashlib import new
from typing import List
import pandas as pd
from itertools import combinations


data = pd.read_csv (r'/Users/chloelebian/Desktop/OpenClassrooms_P7/dataset2_Python_P7.csv').to_dict('records')

newdata = []
zero = []

i = len(data)

for i in range(0,i):
    if data[i]['price'] > 0:
        newdata.append(data[i])

newdata = sorted(newdata, key=lambda d: d['profit'], reverse=True)
    
y = len(newdata)

new_list_of_actions = []

total_cost = 0

i = 0

while i < y:
    if total_cost + newdata[i]['price'] <= 500:
        new_list_of_actions.append(newdata[i])
        total_cost = total_cost + newdata[i]['price']
        i = i+1
        continue
    else:
        i = i+1
        continue

q = len(new_list_of_actions)

for i in range(0,q):
    print(new_list_of_actions[i]['name'])

print(total_cost)

total_profit = 0

for y in range (0, q):
    profit_rate = new_list_of_actions[y]['profit']
    profit_rate = profit_rate / 100
    profit_per_action = new_list_of_actions[y]['price'] * profit_rate
    total_profit = total_profit + profit_per_action

print(total_profit)
