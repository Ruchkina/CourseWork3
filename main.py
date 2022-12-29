# -*- coding: utf-8 -*-
import Extractor as ex
import CountEmotion as ce
import CountWords as cw

df = ex.extract_df('translate/fake_hhh.csv', 3)
df_label = ex.extract_col('translate/fake_hhh.csv', 'label')
mark = ex.extract_diction('diction/mark.txt')

df_emotion = ce.count_emotion(df)
df_mark = cw.count_word(df, mark, 'mark')

path_file = 'rtrt3.csv'

ex.write_to_file(df_emotion, df_mark, df_label, path = path_file)



"""
Created on Wed Dec 28 17:42:32 2022

@author: ruchn
"""

