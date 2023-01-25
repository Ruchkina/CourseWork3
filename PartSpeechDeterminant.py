# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:13:02 2023

@author: ruchn
"""
import pymorphy2 as pych
import pandas as pd
import string


df = pd.read_csv('translate/for_study_info.csv',  nrows = 25)
list_new = []
morph = pych.MorphAnalyzer()
for index in range(len(df)):
    text = str(df['text'].iloc[index])
    text = text.strip()
    # text = text.lower()
    text = text.translate(text.maketrans("", "", string.punctuation))
    words = text.split()
    count = 0
    for element in words:
        p = morph.parse(element.lower())[0]
        if (p.tag.POS in ['ADVB', 'ADJF','ADJS','PRTF']):
            list_new.append(p.normal_form)
            
        #[0].normal_form
        #print(p)
