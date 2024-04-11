from data_processing.sort.selection_sort import sortSelectionAsc
import random
import time
import matplotlib.pyplot as plt


def genlist(size):
    return random.sample(range(0, size * 10), size)

if __name__ == "__main__":

    # experimental parameters
    dataSizeList = [1000, 2000, 4000, 8000, 16000]
    epoch = 5
    # experimental results
    timeTakenResults = list()
    
    random.seed(1)
    for dataSize in dataSizeList:
        timeTaken = 0  # the total time for all epoches
        for e in range(0, epoch):
            # generate dataset
            numlist = genlist(dataSize)
            startTime = time.time()
            count = sortSelectionAsc(numlist)
            # sortInsertionAsc(numlist)

            endTime = time.time()
            timeTaken += (endTime - startTime)
        timeTaken /= epoch
        
        print("Time taken is {} s for data size {}".format(timeTaken, dataSize))
        print(count)
        timeTakenResults.append(timeTaken)
    

    plt.xlabel('Data Size')
    plt.ylabel('Time Lapse (s)')
    plt.axis([0, dataSizeList[-1], 0, timeTakenResults[-1]])
    plt.plot(dataSizeList, timeTakenResults, color='r', linewidth=2.0)
    plt.show()
