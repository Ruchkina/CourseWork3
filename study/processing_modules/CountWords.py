# -*- coding: utf-8 -*-
import string
import pandas as pd
import pymorphy2 as pych

def count_word(df, diction, name, func):
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
        if element.isupper():
            p = morph.parse(element.lower())[0].normal_form
            if p in diction:
                count = count + 1
    return count

