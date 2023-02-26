# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:12:08 2023

@author: ruchn
"""
import Extractor as ex

import matplotlib.pyplot as plt
import numpy as np


data = ex.extract_df('translate/for_study_info.csv', 3070)

# print(data.groupby('label').count())

index = ['истина', 'ложь']
values = [1700, 1359]
plt.title('Распределение новостей')
color_rectangle = np.random.rand(6, 4)
plt.bar(index,values, color = color_rectangle)

plt.show()

"""
data['label'].hist(by=data['label'])
plt.suptitle("label")
сor = data.corr()
"""

