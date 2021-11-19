import tweepy
from tweepy.streaming import StreamListener
from tweepy import *
import pandas as pd

from .clean import cleanTweet


def extractTweets(keyword, count,item):
    api_key = "EmGjNutMOFkjcOJhrkiEkqVXq"
    api_secret = "XjElQEoclGogHUUlaicIbfYjbl1YNLLyhO5WkhjTVM4VmV1JpG"

    access_token = "1393248498502483968-Npak2qPjOGBRhaQRLEq1ZjmIwfKxol"
    access_secret = "XOKJiqKqn8VF7yTzq8LpXYFu4OcEaexqP6ns3yxtTuIYu"

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)

    apitweet = tweepy.API(auth)

    df = pd.DataFrame(columns=['DateTime', 'Tweet_Id', 'Tweet', 'User_Id', 'Retweet', 'Location', 'Label','Country'])

    n = 0
    tweets = tweepy.Cursor(apitweet.search, wait_on_rate_limit=True, q=keyword,
                           lang="en", count=count).items(item)
    for tw in tweets:

        try:
            if tw.text!="" and tw.id !="" and tw.entities['user_mentions'][0]['id']!="":
                df.loc[n, 'DateTime'] = tw.created_at
                df.loc[n, 'Location'] = tw.user.location
                df.loc[n, 'Retweet'] = tw.retweet_count
                df.loc[n, 'Tweet_Id'] = tw.id
                df.loc[n, 'User_Id'] = tw.entities['user_mentions'][0]['id']
                df.loc[n, 'Tweet'] = tw.text

            n += 1

        except:
            pass

    df.drop_duplicates(subset="Tweet", keep=False, inplace=True)

    df.reset_index(inplace=True)
    df = df.drop(columns=['index'])

    for i in range(len(df)):
        df['Tweet'][i] = cleanTweet(df['Tweet'][i])

    return df


def vaccine(list1, j):
    tempdf = pd.DataFrame(columns=['DateTime', 'Tweet_Id', 'Tweet', 'User_Id', 'Retweet', 'Location', 'Label','Country'])
    for i in list1:
        print(i)
        tempdf=tempdf.append(extractTweets(i, j,1000),ignore_index=True)
    return tempdf
