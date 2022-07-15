from ast import Return
from hashlib import new
from typing import List
import pandas as pd
from itertools import combinations


data = pd.read_csv (r'/Users/chloelebian/Desktop/OpenClassrooms_P7/dataset1_Python_P7.csv').to_dict('records')

newdata = []

i = len(data)

for i in range(0,i):
    if data[i]['price'] > 0:
        newdata.append(data[i])

newdata = sorted(newdata, key=lambda d: d['profit'], reverse=True)
    
y = len(newdata)

new_list_of_combinations = []

total_cost = 0

for i in range(0, y):
    total_cost = total_cost + newdata[i]['price']
    if total_cost < 500:
        new_list_of_combinations.append(newdata[i])

q = len(new_list_of_combinations)

final_cost = 0

for i in range(0, q):
    final_cost = final_cost + new_list_of_combinations[i]['price']

for i in range(0, q):
    print(new_list_of_combinations[i]['name'])

print(final_cost)

z = len(new_list_of_combinations)

total_profit = 0

for y in range (0, z):
    profit_rate = new_list_of_combinations[y]['profit']
    profit_rate = profit_rate / 100
    profit_per_action = new_list_of_combinations[y]['price'] * profit_rate
    total_profit = total_profit + profit_per_action

print(total_profit)
