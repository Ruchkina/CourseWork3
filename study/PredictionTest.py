# -*- coding: utf-8 -*-
import pickle
import numpy as np


x = ["Внимание! Ужасная трагедия произошла сегодня"]
"""
load_model = pickle.load(open('model.pkl', 'rb'))

y_pred = load_model.predict(x)

print(y_pred)
"""

to_predict = np.array(x).reshape(1,12)
loaded_model = pickle.load(open("model.pkl","rb"))
result = loaded_model.predict(to_predict)
print(result[0])

"""
Created on Mon Jan 30 14:01:17 2023

@author: ruchn
"""

