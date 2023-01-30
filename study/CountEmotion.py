# -*- coding: utf-8 -*-

from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import pandas as pd
# import numpy as np

def count_emotion(data):
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    messages = data#['text']
    results = model.predict(messages, k=2)
    df_emotion = pd.DataFrame(results)
    if "skip" in df_emotion.columns :
        df_emotion.drop("skip", axis=1, inplace=True)
    if "neutral" not in df_emotion.columns :
        df_emotion.insert(0, "neutral", 0)
    if "negative" not in df_emotion.columns :
        df_emotion.insert(1, "negative", 0)
    df_emotion = df_emotion.fillna(0)
    # df["label"] = data["label"]
    # res = [[key for key in results[0].keys()], *[list(idx.values()) for idx in results ]]
    #q = list(map(list, results.items()))
    return df_emotion


# df = df[((df.negative < 0.4) & (df.label == 0)) | (df.label == 1)]
# df.loc[(df.label == 0) & (df.negative > 0.02), ('negative')] = df.negative - 0.02

# df.to_csv('news_26_12.csv')



"""
Created on Wed Dec 28 10:55:12 2022

@author: ruchn
"""

