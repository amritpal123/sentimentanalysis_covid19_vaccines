import numpy as np
import matplotlib.pyplot as plt

def barcompare(dataset):
    X = ['Positive_Tweets', 'Negative_Tweets', 'Neutral_Tweets']
    v1 = [dataset['Positive_Tweets_per'][0], dataset['Negative_Tweets_per'][0], dataset['Neutral_Tweets_per'][0]]
    v2 = [dataset['Positive_Tweets_per'][1], dataset['Negative_Tweets_per'][1], dataset['Neutral_Tweets_per'][1]]

    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, v1, 0.4, label=dataset['Name'][0])
    plt.bar(X_axis + 0.2, v2, 0.4, label=dataset['Name'][1])

    plt.xticks(X_axis, X)
    plt.xlabel("Vaccines")
    plt.ylabel("Percentage")
    plt.title("Sentiment%")
    plt.legend()

    plt.savefig("D:/vaccine/static/barchartcompare1.png", bbox_inches='tight')
    print(dataset)
    plt.close()
    return True