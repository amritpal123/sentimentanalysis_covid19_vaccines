import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import matplotlib.patches as p
def donut(d):
    for i in range(len(d)):
        list1=[d["Positive_Tweets_per"][i],d["NonPositive_Tweets_per"][i]]
        colors = ['#00FF00', '#fedc02']
        explode = (0.03, 0.03)
        l2=["Positive_Tweets_per","NonPositive_Tweets_per"]
# Pie Chart
        angle = -180 * list1[0]
        plt.pie(list1, colors=colors, labels=l2, startangle= angle,
            autopct='%1.1f%%', pctdistance=0.85,
            explode=explode)

# draw circle
        centre_circle = plt.Circle((0, 0), 0.60, fc='white')
        fig = plt.gcf()

# Adding Circle in Pie chart
        fig.gca().add_artist(centre_circle)


        # Adding Title of chart
        plt.title('Positive Tweets % vs Non-Positive Tweets %')

# Displaing Chart
        k = i
        plt.savefig("D:/vaccine/static/"+str(k)+".png", bbox_inches='tight')
        plt.close()
    return True

