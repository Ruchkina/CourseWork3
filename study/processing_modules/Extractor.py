# -*- coding: utf-8 -*-

import pandas as pd

def concatenation(*df):
    datafr_result = pd.DataFrame()
    for df_c in df:
        datafr_result = pd.concat([datafr_result, df_c], axis=1)
    return datafr_result

def extract_df(path, rows_count):
    return pd.read_csv(path,  nrows = rows_count, encoding="utf8") 
#, encoding='cp1251')
# encoding="windows-1251",


def extract_diction(path):
    with open(path, 'r', encoding='utf-8') as file:
        diction = [line.strip() for line in file]
        return diction
    

    
    
        #a = []
    #for l in lst:
        #a.append(l)
    # a = zip(for qqq in lst)
    #df = pd.DataFrame(list(zip(lst1, lst2)),
    #           columns =['Name', 'val'])
    # df = pd.DataFrame(data = a).transpose()
    

"""
Created on Wed Dec 28 10:45:27 2022

@author: ruchn
"""