# -*- coding: utf-8 -*-
import string
import pandas as pd
import pymorphy2 as pych
# import csv

def count_word(df, diction, name):
    count = 0
    list_new = []
    morph = pych.MorphAnalyzer()
    
    for index in range(len(df)):
        text = str(df['text'].iloc[index])
        text = text.strip()
        text = text.lower()
        text = text.translate(text.maketrans("", "", string.punctuation))
        words = text.split()
        for word in words:
            p = morph.parse(word)[0].normal_form
            # print(p.normal_form)
            if p in diction:
                count = count + 1
        list_new.append(count)
        count = 0
    d_new = pd.DataFrame(list_new, columns=[name])
    return d_new
        
"""


# any(x in string for x in search)
# Open the file in read mode
#text = open("sample.txt", "r")

'''
"""
