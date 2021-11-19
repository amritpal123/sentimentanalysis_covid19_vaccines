from textblob import TextBlob

import pandas as pd

from .labeling import sentiMent

def formula(dataset):
    l=0
    k=0
    for i in range(0, len(dataset)):
        if(dataset['Label']==Weakly_Positive or dataset['Label']==Highly_Positive):
            l+=1
        else:
            k+=1