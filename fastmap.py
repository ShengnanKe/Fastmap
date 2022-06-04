import pandas as pd
import numpy as np
import random
import math
import matplotlib.pyplot as plt


# random.seed(2022)

class fastMapImplementation():
    def __init__(self, f_data, f_words, k):
        self.data = pd.read_csv(f_data, sep='\t', header=None, names=['w1', 'w2', 'dist'])
        self.words = pd.read_csv(f_words, header=None)[0].tolist()
        self.N = len(self.words)  # number of objects
        self.k = k  # number of dimensions
        self.coordinates = np.zeros((self.N, self.k))
        
        
    def getDomainSpecificDist(self, i, j):
        if i > j:
            i, j = j, i
        elif i == j:  # D(a, a) = 0
            return 0
        # print('i is:', i, 'j is: ', j)
        return self.data.loc[(self.data.w1==i) & (self.data.w2==j), 'dist'].values[0]
    
    
    def computeDistance(self, i, j):  # todo
        dij2 = math.pow(self.getDomainSpecificDist(i,j), 2)  # square of domain specijic distance
        sum_lij2 = 0 # sum of square of (li-lj)
        for k in range(self.k):
            sum_lij2 += math.pow(self.coordinates[i-1,k] - self.coordinates[j-1,k], 2)
        # try:
        #     math.pow(dij2 - sum_lij2, 0.5)
        # except:
        #     print('dif2:', dij2, 'sum_lij2', sum_lij2)
        return math.pow(dij2 - sum_lij2, 0.5)
    
    
    def pickFarthestPair(self):  # todo
        max_pivots = 5
        pivot = random.randint(1, self.N)  # a random starting pivot
        farthest = ''
        a, b = pivot, farthest
        for iteration in range(max_pivots):  # change pivot for at most max_pivots times
            # find the farthest object from the pivot
            max_dist = float('-inf')
            for idx in range(1, self.N+1):
                dist_pivot_idx = self.computeDistance(pivot, idx)
                if dist_pivot_idx > max_dist:
                    farthest = idx
                    max_dist = dist_pivot_idx
            if a == farthest and b == pivot:  # if converge
                # print('converge! pivot is:', pivot, 'farthest is:', farthest)
                break
            else:
                a, b = pivot, farthest
                pivot = farthest  # change pivot
                # print('pivot is:', a, 'farthest is:', b)
        return a, b
    
    
    def runFastMap(self):
        for k in range(self.k):
            print('--------iteration ', k+1, '--------')
            # pick the farthest pair of objects
            a, b = self.pickFarthestPair()
            # compute the kth dimension coordinates of all N data
            dab = self.computeDistance(a, b)  
            coordinates_1d = []
            for i  in range(1, self.N+1):
                coordinates_1d.append(max(0, (math.pow(self.computeDistance(i, a), 2) + math.pow(dab, 2) - math.pow(self.computeDistance(i, b), 2))/(2 * dab)))
            self.coordinates[:, k] = coordinates_1d
            
            
    def plot(self):
        fig, ax = plt.subplots()
        for i in range(self.N):
            ax.scatter(self.coordinates[i][0], self.coordinates[i][1])
            ax.annotate(self.words[i], (self.coordinates[i][0], self.coordinates[i][1]))
        plt.show()

                
k = 2        
fastmap = fastMapImplementation('fastmap-data.txt', 'fastmap-wordlist.txt', k)
fastmap.runFastMap()
fastmap.plot()








# N = 10
# k = 2
# coordinates = []

# self.data = pd.read_csv(filename, sep='\t', header=None, names=['w1', 'w2', 'dist'])

# def getDomainSpecificDist(i, j):
#     if i > j:
#         i, j = j, i
#     return data.loc[(data.w1==i) & (data.w2==j), 'dist'].values[0]


# def computeDistance(i, j):
#     return


# def pickFarthestPair():
#     return a, b

# set K as the number of dimensions of data after implementing FastMap
# def fastMap(k):
#     for k = 1, 2, ..., K:
#         set a, b to the farthest pair of objects
#         compute the kth dimension coordinate of each object
#         update the distance function