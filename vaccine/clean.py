# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:01:33 2020

@author: aarus
"""


import re
from textblob import TextBlob

def lemmatize_with_postag(sentence):
    sent = TextBlob(sentence)
    tag_dict = {"J": 'a',
                "N": 'n',
                "V": 'v',
                "R": 'r'}
    words_and_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]
    lemmatized_list = [wd.lemmatize(tag) for wd, tag in words_and_tags]
    return " ".join(lemmatized_list)


def cleanTweet(tweet):

    # Remove Links, Special Characters etc from tweet
    tweet=re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)

    tweet=re.sub('RT','',tweet)
    tweet=' '.join(re.sub("@[\w]*"," ",tweet).split())
        
    tweet=' '.join(re.sub("([^a-zA-Z0-9#])"," ",tweet).split())

    tweet=lemmatize_with_postag(tweet)
                             
    return tweet