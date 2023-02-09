# -*- coding: utf-8 -*-

import pickle
import pandas as pd
import Extractor as ex
import CountEmotion as ce
import CountWords as cw
import numpy as np

def write_to_file(*df):
    datafr_result = pd.DataFrame()
    for df_c in df:
        datafr_result = pd.concat([datafr_result, df_c], axis=1)
    return datafr_result

mark = ex.extract_diction('diction/mark.txt')
adj = ex.extract_diction('diction/adj.txt')
caps_lock = ex.extract_diction('diction/caps_lock.txt') 

x = ex.extract_df('testds.csv', 12)
df_emotion = ce.count_emotion(x)
df_mark = cw.count_word(x, mark, 'mark', cw.morth_analyse)
df_adj = cw.count_word(x, adj, 'adj', cw.morth_analyse)
# df_caps_lock = cw.count_word(x, caps_lock, 'caps_lock', cw.caps_lock_analyse)

res_nums = write_to_file(df_emotion, df_mark, df_adj)
print(res_nums)
load_model = pickle.load(open('model.pkl', 'rb'))

y_pred = load_model.predict(res_nums)

print(y_pred)

"""
Created on Mon Jan 30 14:01:17 2023

@author: ruchn


"""
