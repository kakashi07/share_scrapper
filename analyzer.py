import numpy as np
import pandas as pd

# filename = '../input/datas.csv'
filename = 'datas.csv'
datas = pd.read_csv(filename, sep='|', header=0)

# this column gives : How low is the current price from TY Highest i.e. 10% means the CCP is 10% lower than TY HP.
datas['d_highest%'] = 100 * (datas['TY Highest'] - datas['Closing Price']) / datas['TY Highest']

'''This column gives : How higher is the current price from TY Lowest Price i.e. 10 % means the price has rose 10% 
from its lowest value'''
datas['d_lowest%'] = 100 * (datas['Closing Price'] - datas['TY Lowest']) / datas[
    'TY Lowest']  # change with respect to LV


def rankers(n=7):
    high_rankers_head = datas.sort_values(by=['d_highest%']).head(n)
    high_rankers_tail = datas.sort_values(by=['d_highest%']).tail(n)
    low_rankers_head = datas.sort_values(by=['d_lowest%']).head(n)
    low_rankers_tail = datas.sort_values(by=['d_lowest%']).tail(n)

    rankers = [high_rankers_head,high_rankers_tail,low_rankers_head,low_rankers_tail]
    return  rankers

data = rankers()
# data[0]


