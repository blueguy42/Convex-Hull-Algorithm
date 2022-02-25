import matplotlib.pyplot as plt
from myConvexHull import myConvexHull
import random

def plotColor(n):
    '''Generasi warna sebanyak n'''
    colors = ['b','r','g','c','m','y','k']
    if n > len(colors):
        for i in (range(n-len(colors))):
            r = random.random()
            g = random.random()
            b = random.random()
            colors.append((r, g, b))
    return colors


def graph(df, data, graphtitle, xlabel, ylabel, xrow, yrow, labelnames):
    '''Memvisualisasikan grafik hasil convex hull dengan memplot
    titik-titik dan garis convex hull dan menyimpannya pada folder
    test'''

    plt.figure(figsize = (10, 6))
    labelsize = len(df['label'].unique())
    colors = plotColor(labelsize)

    plt.title(graphtitle)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    for i in range(labelsize):
        bucket = df[df['label'] == i]
        bucket = bucket.iloc[:,[xrow,yrow]].values

        # Implementasi algoritma divide and conquer Convex Hull
        hull = myConvexHull(bucket)

        plt.scatter(bucket[:, 0], bucket[:, 1], label=labelnames[i], color=colors[i])
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color=colors[i])
    
    plt.legend()
    print("\nShowing graph of convex hull...")
    print("Make sure to close the graph pop-up so the program can continue!")
    fig1 = plt.gcf()
    plt.show()
    
    outputcondition = input("\nWould you like to save the convex hull graph? (Y/N): ")
        
    if outputcondition.upper() == "Y":
        output = input("\nOutput file name: ") + ".png"
        fig1.savefig('test/' + output)
        print(f"Your convex hull graph of {data.feature_names[xrow]} vs. {data.feature_names[yrow]} at {output} has successfully been made at folder test!")
    plt.close('all')
    
