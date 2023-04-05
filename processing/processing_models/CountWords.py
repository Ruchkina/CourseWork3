# -*- coding: utf-8 -*-
import string
import pandas as pd
import pymorphy2 as pych

def count_punctuation(df, name):
    mark = []
    for index in range(len(df)):
        text = str(df['text'].iloc[index])
        mark.append(text.count('!'))
    d_new = pd.DataFrame(mark, columns=[name])
    print(d_new)
    return d_new
        

def count_word(df, diction, name, func):
    #count = 0
    list_new = []
    
    for index in range(len(df)):
        text = str(df['text'].iloc[index])
        text = text.strip()
        # text = text.lower()
        text = text.translate(text.maketrans("", "", string.punctuation))
        words = text.split()
        list_new.append(func(words, diction))
    d_new = pd.DataFrame(list_new, columns=[name])
    return d_new
     
def morth_analyse(elements, diction):
    count = 0
    morph = pych.MorphAnalyzer()
    for element in elements:
        p = morph.parse(element.lower())[0].normal_form
        if p in diction:
            count = count + 1
    return count

def caps_lock_analyse(elements, diction):
    count = 0
    morph = pych.MorphAnalyzer()
    for element in elements:
        #print(element)
        if element.isupper():
            p = morph.parse(element.lower())[0].normal_form
            print(p)
            if p in diction:
                count = count + 1
    return count


            

"""


# any(x in string for x in search)
# Open the file in read mode
#text = open("sample.txt", "r")

'''
"""
