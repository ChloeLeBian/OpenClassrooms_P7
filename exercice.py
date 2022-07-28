from ast import Return
from hashlib import new
from typing import List
import pandas as pd
from itertools import combinations


data = pd.read_csv (r'/Users/chloelebian/Desktop/OpenClassrooms_P7/dataset1_Python_P7.csv').to_dict('records')

def calculateAverageProfitRate(x):
    y = len(x)
    totalProfitRate = 0
    for i in range(0, y):
        totalProfitRate += x[i]['profit']
    totalProfitRate = totalProfitRate / y
    print(totalProfitRate)

calculateAverageProfitRate(data)