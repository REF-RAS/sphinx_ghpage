

def pigeonHoleSortAsc(alist:list, maxvalue:int = 160000):
    """ Apply pigeon-hole sort in ascending order on a list 

    :param alist: The list to be sorted
    :type alist: list
    :param maxvalue: The maximum value in the list, defaults to 160000
    :type maxvalue: int, optional
    """
    # the working array used by pigeon Hole Sort
    # assume the largest value in the data array is 160000
    workarray = [0] * maxvalue
    pass
    # iterate through data list and update the working array (frequency)
    for value in alist:
        workarray[value] += 1
    # iterate through the working array and update the data list
    alist.clear()
    index = 0
    while index < len(workarray):
        freq = workarray[index]
        alist.extend([index] * freq)
        index += 1


if __name__ == "__main__":
    numlist = [20, 14, 36, 20, 8, 20, 56, 49, 3, 5, 3, 5, 6, 4]
    
    pigeonHoleSortAsc(numlist)
    print(numlist)
