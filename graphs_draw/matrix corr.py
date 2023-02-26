# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:19:46 2023

@author: ruchn
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("C:/univer/course_work/processing/quantitative_processing.csv")

TARGET_NAME = 'label'
BASE_FEATURE_NAMES = df.columns.drop([TARGET_NAME, 'num']).tolist()
FEATURE_NAMES_SELECTED = BASE_FEATURE_NAMES

plt.figure(figsize = (17,17))

sns.set(font_scale=2)
sns.heatmap(df[BASE_FEATURE_NAMES].corr().round(3), annot=True, linewidths=.5, cmap='GnBu')

plt.title('Матрица корреляции')
plt.show()