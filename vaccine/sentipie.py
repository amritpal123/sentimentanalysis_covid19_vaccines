# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:02:38 2020

@author: aarus
"""

import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def sentiFig(dataset):
    count=0
    df2 = dict(dataset['Country'].value_counts())
    df1 = pd.DataFrame(columns=['DateTime', 'Tweet_Id', 'Tweet', 'User_Id', 'Retweet', 'Location', 'Label', 'Country'])
    for i in df2.keys():
        count=count+1
        for j in range(len(dataset)):
            if i == dataset['Country'][j]:
                df1 = df1.append(dataset.iloc[j])
        sentiment = df1['Label'].value_counts()

        print(sentiment)
        total = 0
        size = []

        for l in sentiment.values:
            total += l
            size.append(l)

        explode = []
        for m in range(len(sentiment)):
            explode.append(0.01)

        explode = tuple(explode)

        l2 = sentiment.keys()

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        ax.pie(size, labels=l2, autopct='%1.2f%%', explode=explode)
        k = count

        plt.savefig("D:/vaccine/static/pie" + str(k) + ".png", bbox_inches='tight')

        plt.close()

    return count

