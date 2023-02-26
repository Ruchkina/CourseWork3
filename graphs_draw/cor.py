# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:17:43 2023

@author: ruchn
"""
import pandas as pd
import seaborn as sns
import matplotlib as plt

data = pd.read_csv("C:/univer/course_work/processing/quantitative_processing.csv")
data = data.fillna(0)

TARGET_NAME = 'label'
BASE_FEATURE_NAMES = data.columns.drop([TARGET_NAME, 'num']).tolist()
FEATURE_NAMES_SELECTED = BASE_FEATURE_NAMES
 
corr_with_target = data[BASE_FEATURE_NAMES + [TARGET_NAME]].corr().iloc[:-1, -1].sort_values(ascending=False)

plt.figure(figsize=(10, 8))

sns.barplot(x=corr_with_target.values, y=corr_with_target.index)

plt.title('Корреляция с целевым параметром')
plt.show()