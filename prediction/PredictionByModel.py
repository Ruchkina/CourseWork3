# -*- coding: utf-8 -*-

import pickle

def prediction(df):
    load_model = pickle.load(open('model3.pkl', 'rb'))
    y_pred = load_model.predict(df)
    return(y_pred)





"""
Created on Thu Feb  9 11:50:16 2023

@author: ruchn
"""