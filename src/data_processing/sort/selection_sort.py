# Selection sort (Ascending order)
def sortSelectionAsc(alist:list) -> None:
    """ Apply selection sort in ascending order on a list

    :param alist: The list to be sorted
    :type alist: list
    """
    size = len(alist)
    count = 0
    # unsortedEnd runs from size-1 to 1
    for unsortedEnd in range(size - 1, 0, -1):
        # search for largest value in unsorted part
        lindex = 0    # index of largest value
        for i in range(1, unsortedEnd + 1):
            count += 1
            if alist[i] > alist[lindex]:
                lindex = i
        # swap largest with end
        alist[lindex], alist[unsortedEnd] = alist[unsortedEnd], alist[lindex]
        # print(alist)    # print intermediate steps
    return count

# Selection sort (Descending order)
def sortSelectionDesc(alist:list) -> None:
    """ Apply selection sort in decending order on a list

    :param alist: The list to be sorted
    :type alist: list
    """
    size = len(alist)
    # unsortedEnd runs from size-1 to 1
    for unsortedEnd in range(size - 1, 0, -1):
        # search for smallest value in unsorted part
        sindex = 0    # index of smallest value
        for i in range(1, unsortedEnd + 1):
            if alist[i] < alist[sindex]:
                sindex = i
        # swap smallest with end
        alist[sindex], alist[unsortedEnd] = alist[unsortedEnd], alist[sindex] 
        # print(alist)    # print intermediate steps

if __name__ == "__main__":
    numlist = [20, 14, 36, 8, 56, 49]
    
    sortSelectionAsc(numlist)
    print(numlist)
    
    sortSelectionDesc(numlist)
    print(numlist)
