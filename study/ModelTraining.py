# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, ShuffleSplit, cross_val_score, learning_curve
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score, precision_score, recall_score
import pickle

MODEL_FILE_PATH = '../model3.pkl'

def get_classification_report(y_train_true, y_train_pred, y_test_true, y_test_pred):
    print('TRAIN\n\n' + classification_report(y_train_true, y_train_pred))
    print('TEST\n\n' + classification_report(y_test_true, y_test_pred))
    print('CONFUSION MATRIX\n')
    print(pd.crosstab(y_test_true, y_test_pred))

# df = pd.read_csv("C:/univer/course_work/rtr6_copy.csv")
df = pd.read_csv("C:/univer/course_work/processing/q1.csv")
TARGET_NAME = 'label'
BASE_FEATURE_NAMES = df.columns.drop([TARGET_NAME]).tolist()
FEATURE_NAMES_SELECTED = BASE_FEATURE_NAMES

X = df[FEATURE_NAMES_SELECTED]
y = df[TARGET_NAME]

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, test_size=0.25, random_state=211)

model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)

y_train_pred = model_lr.predict(X_train)
y_test_pred = model_lr.predict(X_test)

get_classification_report(y_train, y_train_pred, y_test, y_test_pred)

with open(MODEL_FILE_PATH, 'wb') as file:
    pickle.dump(model_lr, file)

'''
corr_with_target = df[BASE_FEATURE_NAMES + [TARGET_NAME]].corr().iloc[:-1, -1].sort_values(ascending=False)

sns.barplot(x=corr_with_target.values, y=corr_with_target.index)
'''






"""
Created on Wed Jan  4 14:41:02 2023

@author: ruchn
"""

