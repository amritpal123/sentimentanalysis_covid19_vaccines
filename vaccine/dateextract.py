import tweepy
from tweepy.streaming import StreamListener
from tweepy import *
import pandas as pd
from datetime import datetime
from .clean import cleanTweet


def extractTweets(keyword, count):
    api_key = "EmGjNutMOFkjcOJhrkiEkqVXq"
    api_secret = "XjElQEoclGogHUUlaicIbfYjbl1YNLLyhO5WkhjTVM4VmV1JpG"

    access_token = "1393248498502483968-Npak2qPjOGBRhaQRLEq1ZjmIwfKxol"
    access_secret = "XOKJiqKqn8VF7yTzq8LpXYFu4OcEaexqP6ns3yxtTuIYu"

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)

    apitweet = tweepy.API(auth)

    start_date = datetime(2021, 3, 1)
    end_date = datetime(2021, 4, 1)

    df = pd.DataFrame(columns=['DateTime', 'Tweet_Id', 'Tweet', 'User_Id', 'Retweet', 'Location', 'Label'])

    n = 0
    tweets = tweepy.Cursor(apitweet.search, wait_on_rate_limit=True, q=keyword, start_date=start_date,end_date=end_date,
                           lang="en", count=count).items(200)
    for tw in tweets:

        try:
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


def vaccine1(list1, j):
    tempdf = pd.DataFrame(columns=['DateTime', 'Tweet_Id', 'Tweet', 'User_Id', 'Retweet', 'Location', 'Label'])
    for i in list1:
        tempdf=tempdf.append(extractTweets(i, j),ignore_index=True)
    return tempdf
