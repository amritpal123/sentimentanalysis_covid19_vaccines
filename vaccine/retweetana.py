# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:19:39 2020

@author: aarus
"""

import pandas as pd



import tweepy
from tweepy.streaming import StreamListener
from tweepy import *




def reTweetData(df):
    
    retweets=[]
    
    for i in range(3):

                
        a=df.loc[df['Retweet'] == df['Retweet'].max()]
        a=a.reset_index(drop=True)
        a=a.to_dict()
        
        for k in a.keys():
            a[k]=a[k][0]

        retweets.append(a)
        
        
        df=df[df.Retweet != df['Retweet'].max()]

    api_key = "EmGjNutMOFkjcOJhrkiEkqVXq"
    api_secret = "XjElQEoclGogHUUlaicIbfYjbl1YNLLyhO5WkhjTVM4VmV1JpG"

    access_token = "1393248498502483968-Npak2qPjOGBRhaQRLEq1ZjmIwfKxol"
    access_secret = "XOKJiqKqn8VF7yTzq8LpXYFu4OcEaexqP6ns3yxtTuIYu"

    auth=tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_secret)

    apitweet=tweepy.API(auth)

    for i in range(len(retweets)):

        user = apitweet.get_user(int(retweets[i]['User_Id']))
        retweets[i]['description']=user.description
        retweets[i]['name']=user.screen_name
        retweets[i]['followers_count']=user.followers_count
        retweets[i]['total_tweets']=user.statuses_count
        retweets[i]['following']=user.friends_count

    return retweets
