from ast import Return
import pandas as pd
from itertools import combinations


data = pd.read_csv (r'/Users/chloelebian/Desktop/OpenClassrooms_P7/Data1.csv').to_dict('records')

list_of_combinations = []
for i in range(1, 21):
    a = combinations(data, i)
    list_of_combinations += list(a)

def calculate_cost(b):
    i = len(b)
    total_cost = 0
    for y in range(0,i):
        cost_per_action = b[y]['price']
        total_cost = total_cost + cost_per_action
    return total_cost
    
def calculate_profit(c):
    i = len(c)
    total_profit = 0
    for y in range (0, i):
        profit_rate = int(c[y]['profit'][:-1])
        profit_rate = profit_rate / 100
        profit_per_action = c[y]['price'] * profit_rate
        total_profit = total_profit + profit_per_action
    return total_profit

def calculate_profit_max(d):
    i = len(d)
    total_profit = 0
    for y in range (0, i):
        profit_rate = int(d[y]['profit'][:-1])
        profit_rate = profit_rate / 100
        profit_per_action = d[y]['price'] * profit_rate
        total_profit = total_profit + profit_per_action
    print(total_profit)

y = len(list_of_combinations)

new_list_of_combinations = []

for i in range(0, y):
    b = list_of_combinations[i]
    total_cost = calculate_cost(b)
    if total_cost <= 500:
        new_list_of_combinations.append(b)

z = len(new_list_of_combinations)
best_combination = new_list_of_combinations[0]

for i in range (1,z):
    c = new_list_of_combinations[i]
    if calculate_profit(c)>=calculate_profit(best_combination):
        best_combination = c
    else:
        best_combination = best_combination

print(best_combination)
calculate_profit_max(best_combination)

    
    

    





#une premiere fonction qui prend combi et calcule le cout
#une fonction qui prend la combinaison en paramettre et calcule le profit 

#on parcourt la liste des combinaison et on enlève toutes celles qui ont un prix sup à 500
#on parcourt la nouvelle liste nettoyée et on calcule le profit de chaque combi
#si profit actuel est sup au profit précédent, meilleur combi=combi actuelle