# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:27:16 2020

@author: aarus
"""



from textblob import TextBlob

import pandas as pd


def sentiMent(dataset):

    
    for i in range(0,len(dataset)):
        tweet1 = dataset['Tweet'][i]
        analysis=TextBlob(tweet1)
        
        if analysis.polarity==0:
            l='Neutral'
        
        elif analysis.polarity > 0:
            if analysis.polarity<0.5:
                l='Weakly_Positive'
            else:
                l='Highly_Positive'
        elif analysis.polarity < 0 :
            if analysis.polarity>-0.5:
                l='Highly_Negative'
            else:
                l='Weakly_Negative'
        
            
         
        dataset['Label'][i]=l
       
        
    return dataset
        
        

