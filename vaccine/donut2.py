import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch


def donut2(d,e):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)

    for i in range(len(d)):
        ratios = [d["Positive_Tweets_per"][i],d["NonPositive_Tweets_per"][i]]
        labels = ['Positive_Tweets%', 'Non-positive Tweets%']
        explode = [0.1, 0]

        ax1.pie(ratios, autopct='%1.1f%%', startangle=90,counterclock=False,
                labels=labels, explode=explode)
        centre_circle = plt.Circle((0, 0), 0.60, fc='white')
        fig = plt.gcf()

        # Adding Circle in Pie chart
        fig.gca().add_artist(centre_circle)

        # bar chart parameters

        xpos = 0
        bottom = 0
        ratios = [e["Highly_Positive_Tweets_per"][i],e["Weakly_Positive_Tweets_per"][i]]
        width = .2
        colors = [[.1, .3, .5], [.1, .3, .9]]

        for j in range(len(ratios)):
            height = ratios[j]
            ax2.bar(xpos, height, width, bottom=bottom, color=colors[j])
            ypos = bottom + ax2.patches[j].get_height() / 2
            bottom += height
            ax2.text(xpos, ypos, "%d%%" % (ax2.patches[j].get_height() * 100),
                     ha='center')

        ax2.set_title('Age of approvers')
        ax2.legend(('50-65', 'Under 35'))
        ax2.axis('off')
        ax2.set_xlim(- 2.5 * width, 2.5 * width)

        # use ConnectionPatch to draw lines between the two plots
        # get the wedge data
        theta1, theta2 = ax1.patches[0].theta1, ax1.patches[0].theta2
        center, r = ax1.patches[0].center, ax1.patches[0].r
        bar_height = sum([item.get_height() for item in ax2.patches])

        # draw top connecting line
        x = r * np.cos(np.pi / 180 * theta2) + center[0]
        y = r * np.sin(np.pi / 180 * theta2) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                              xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        con.set_linewidth(4)
        ax2.add_artist(con)

        # draw bottom connecting line
        x = r * np.cos(np.pi / 180 * theta1) + center[0]
        y = r * np.sin(np.pi / 180 * theta1) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                              xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        ax2.add_artist(con)
        con.set_linewidth(4)
        k = i+5
        g=k
        plt.savefig("D:/vaccine/static/" + str(g) + ".png", bbox_inches='tight')
        plt.close()
    return True

