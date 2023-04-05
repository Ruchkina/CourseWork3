# -*- coding: utf-8 -*-
import processing_models.Extractor as ex
import processing_models.CountEmotion as ce
import processing_models.CountWords as cw

n = 3072

df = ex.extract_df('translate/for_study_info.csv', n)
df_label = ex.extract_col('translate/for_study_info.csv', 'label')
mark = ex.extract_diction('diction/mark.txt')
adj = ex.extract_diction('diction/adj.txt')
caps_lock = ex.extract_diction('diction/caps_lock.txt')
exclamation_mark = ex.extract_diction('diction/punctuation.txt')

df_emotion = ce.count_emotion(df)
df_mark = cw.count_word(df, mark, 'processing_models/mark', cw.morth_analyse)
df_adj = cw.count_word(df, adj, 'processing_models/adj', cw.morth_analyse)
df_caps_lock = cw.count_word(df, caps_lock, 'processing_models/caps_lock', cw.caps_lock_analyse)
df_exclamation_mark = cw.count_punctuation(df, 'processing_models/exclamation_mark')

path_file = 'quantitative_processing.csv'

ex.write_to_file(df_emotion, df_mark, df_adj, df_caps_lock, df_exclamation_mark, df_label, path = path_file)



"""
Created on Wed Dec 28 17:42:32 2022

@author: ruchn
"""

