# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:26:40 2020

@author: amrit
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:50:58 2019

@author: amrit
"""

#import pandas as pd
#from nltk.stem import WordNetLemmatizer

#import wordninja
import math

import re

from wordcloud import WordCloud, STOPWORDS

from matplotlib import pyplot as plt

from collections import Counter
import random



def makeWordCloud(dataset):
    neg=''
    pos=''
    neu=''


    for i in range(0,len(dataset)):
        if dataset['Label'][i]=="Neutral":
            tweet=dataset['Tweet'][i]
            tweet=str(tweet)
            tweet = tweet.replace('RT', '')
            tweet = tweet.split(' ')
            for token in tweet:
                neu += token.lower() + ' '

        elif dataset['Label'][i] == "Highly_Positive" or dataset['Label'][i] == "Weakly_Positive":
            tweet = dataset['Tweet'][i]
            tweet = str(tweet)
            tweet = tweet.replace('RT', '')
            tweet = tweet.split(' ')
            for token in tweet:
                pos += token.lower() + ' '

        elif dataset['Label'][i] == "Highly_Negative" or dataset['Label'][i] == "Weakly_Negative":
            tweet = dataset['Tweet'][i]
            tweet = str(tweet)
            tweet = tweet.replace('RT', '')
            tweet = tweet.split(' ')
            for token in tweet:
                neg += token.lower() + ' '

    stopwords = set(STOPWORDS)


    wordcloud1=WordCloud(background_color='white',width=800,height=800,stopwords=stopwords,min_font_size=10).generate(pos)

    plt.imshow(wordcloud1)


    plt.savefig("D:/vaccine/static/pos.png",bbox_inches='tight')

    wordcloud2 = WordCloud(background_color='white',width=800, height=800, stopwords=stopwords, min_font_size=10).generate(neg)

    plt.imshow(wordcloud2)

    plt.savefig("D:/vaccine/static/neg.png", bbox_inches='tight')

    wordcloud3 = WordCloud(background_color='white',width=800, height=800, stopwords=stopwords, min_font_size=10).generate(neu)

    plt.imshow(wordcloud3)

    plt.savefig("D:/vaccine/static/neu.png", bbox_inches='tight')

    plt.close()
    
    return True


