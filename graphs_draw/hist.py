import pandas as pd
import matplotlib as plt
import numpy as np


data = pd.read_csv("C:/univer/course_work/processing/q1.csv")
"""
tr = data.groupby('label')['adj'].count()['ИСТИНА']
l = data.groupby('label')['adj'].count()['ЛОЖЬ']
tr_all = 1706
l_all = 1358


df = data[['adj', 'label']]
rslt_df = df[df['adj'] > 0]
ee = rslt_df[rslt_df['label']=='ИСТИНА']
ddd = rslt_df[rslt_df['adj']==1]
sss = ddd[ddd['label']=='ИСТИНА']
# data = data.fillna(0)
"""

# tr['adj'].hist(by=data['label'], edgecolor = 'black', density=True, sharey=True, range=[1, 20], grid=True)


# axarr = rslt_df['adj'].hist(by=data['label'], edgecolor = 'black', density=True, sharey=True, range=[1, 20], grid=True)
axarr = data['adj'].hist(by=data['label'], density=True, edgecolor = 'black', sharey=True, grid=True)
plt.suptitle("Эмоциональная лексика")

for ax in axarr.flatten():
    ax.set_xlabel("кол-во повторений маркера", fontsize=14)
    ax.set_ylabel("кол-во новостей")


# сor = data.corr()
# print(data.corr()) 
