from ast import Return
from hashlib import new
from typing import List
import pandas as pd
from itertools import combinations


data = pd.read_csv (r'/Users/chloelebian/Desktop/OpenClassrooms_P7/dataset2_Python_P7.csv').to_dict('records')

newdata = []

z = len(data)

for i in range(0,z):
    if data[i]['price'] > 0 and data[i]['profit'] > 0:
        newdata.append(data[i])

newdata = sorted(newdata, key=lambda d: d['profit'], reverse=True)
    
y = len(newdata)

new_list_of_shares = []

total_cost = 0

i = 0

while i < y:
    if total_cost + newdata[i]['price'] <= 500:
        new_list_of_shares.append(newdata[i])
        total_cost += newdata[i]['price']
        i = i+1
        continue
    else:
        i = i+1
        continue

q = len(new_list_of_shares)

for i in range(0,q):
    print(new_list_of_shares[i]['name'])

print(total_cost)

total_profit = 0

for i in range (0, q):
    profit_rate = new_list_of_shares[i]['profit']
    profit_rate = profit_rate / 100
    profit_per_action = new_list_of_shares[i]['price'] * profit_rate
    total_profit += profit_per_action

print(total_profit)