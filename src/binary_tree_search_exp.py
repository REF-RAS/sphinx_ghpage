import random
import time
import matplotlib.pyplot as plt
import math
from data_processing.structures.binary_tree_adt import BSTree

def genlist(size):
    return random.sample(range(0, size), size)

# main program
if __name__ == "__main__":
    # experimental parameters
    dataSizeList = [2500, 5000, 10000, 20000, 40000]
    epoch = 1000
    # experimental results
    timeTakenResults = list()
    timeTaken = 0
    random.seed(1)

    bsTree = BSTree() # create a new BSTree object
    
    for dataSize in dataSizeList:
        # generate dataset
        numlist = genlist(dataSize)
        # build binary search tree
        for num in numlist:
            bsTree.insert(num, random.randint(0, dataSize * 10))

        startTime = time.time()
        for e in range(0, epoch):
            target = math.inf  # forces the worst case
            # target = random.choice(numlist)  # forces the average case
            # bsTree.searchKey(target)
            bsTree.countNodes()
        timeTaken = (time.time() - startTime) / epoch
        
        print("Time taken is {} ms for data size {}".format(timeTaken, dataSize))
        timeTakenResults.append(timeTaken)
    
    plt.xlabel('Data Size')
    plt.ylabel('Time Lapse (ms)')
    plt.axis([0, dataSizeList[-1], 0, timeTakenResults[-1]])
    plt.plot(dataSizeList, timeTakenResults, color='r', linewidth=2.0)
    plt.show()
