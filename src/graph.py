import matplotlib.pyplot as plt
from convexhull import convexhull
import random

def plotcolor(n):
    '''Mengembalikan warna-warna sebanyak n'''
    colors = ['b','r','g','c','m','y','k']
    if n > len(colors):
        for i in (range(n-len(colors))):
            r = random.random()
            g = random.random()
            b = random.random()
            colors.append((r, g, b))
    return colors


def graph(df, graphtitle, xlabel, ylabel, xrow, yrow, labelnames, outputname):
    '''Memvisualisasikan grafik hasil convex hull dengan memplot
    titik-titik dan garis convex hull dan menyimpannya pada folder
    test'''

    plt.figure(figsize = (10, 6))
    labelsize = len(df['label'].unique())
    colors = plotcolor(labelsize)

    plt.title(graphtitle)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    for i in range(labelsize):
        bucket = df[df['label'] == i]
        bucket = bucket.iloc[:,[xrow,yrow]].values

        # Implementasi algoritma divide and conquer Convex Hull
        hull = convexhull(bucket)

        plt.scatter(bucket[:, 0], bucket[:, 1], label=labelnames[i], color=colors[i])
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color=colors[i])
    
    plt.legend()

    # Menyimpan grafik ke folder test
    plt.savefig('test/' + outputname)