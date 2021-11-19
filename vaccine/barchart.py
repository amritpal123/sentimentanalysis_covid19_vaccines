import numpy as np
import matplotlib.pyplot as plt

def bar(dataset):
    list1=[]
    list2=[]
    for i in range(len(dataset)):
        list1.append(dataset['Name'][i])

    for i in range(len(dataset)):
        list2.append(dataset["Positive_Tweets_per"][i])
    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(list1, list2, color='orange',
            width=0.4)

    plt.xlabel("Vaccine Name")
    plt.ylabel("Positive Tweets %")
    plt.title("Vaccine ranking based on positive tweets %")

    plt.savefig("D:/vaccine/static/bar.png", bbox_inches='tight')
    plt.close()
    return True