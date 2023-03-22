# -*- coding: utf-8 -*-

import PredictionByModel as pbm
import processing_modules.Extractor as ex
import processing_modules.CountEmotion as ce
import processing_modules.CountWords as cw


mark = ex.extract_diction('C:/univer/course_work/processing/diction/mark.txt')
adj = ex.extract_diction('C:/univer/course_work/processing/diction/adj.txt')
caps_lock = ex.extract_diction('C:/univer/course_work/processing/diction/caps_lock.txt') 
punctuation = ex.extract_diction('C:/univer/course_work/processing/diction/punctuation.txt') 


x = ex.extract_df('example.csv', 3)
print(x)
df_emotion = ce.count_emotion(x)
df_mark = cw.count_word(x, mark, 'mark', cw.morth_analyse)
df_adj = cw.count_word(x, adj, 'adj', cw.morth_analyse)
df_caps_lock = cw.count_word(x, caps_lock, 'caps_lock', cw.caps_lock_analyse)
df_punctuation = cw.count_punctuation(x, 'exclamation_mark')


res_nums = ex.concatenation(df_emotion, df_mark, df_adj, df_caps_lock, df_punctuation)
print(res_nums)

y_pred = pbm.prediction(res_nums)
print(y_pred)



"""
Created on Mon Jan 30 14:01:17 2023

@author: ruchn

"""
