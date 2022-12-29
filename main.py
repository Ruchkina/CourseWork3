# -*- coding: utf-8 -*-
import Extractor as ex
import CountEmotion as ce
import CountWords as cw

df = ex.extract_df('translate/for_study_info.csv', 25)
df_label = ex.extract_col('translate/for_study_info.csv', 'label')
mark = ex.extract_diction('diction/mark.txt')

df_emotion = ce.count_emotion(df)
df_mark = cw.count_word(df, mark, 'mark', cw.morth_analyse)
df_caps_lock = cw.count_word(df, mark, 'caps_lock', cw.caps_lock_analyse)

path_file = 'rtrt7.csv'

ex.write_to_file(df_emotion, df_mark, df_caps_lock, df_label, path = path_file)



"""
Created on Wed Dec 28 17:42:32 2022

@author: ruchn
"""
