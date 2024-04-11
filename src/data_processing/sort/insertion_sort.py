# Insertion sort (Ascending order)
def sortInsertionAsc(alist:list) -> None:
    """ Apply insertion sort in ascending order on a list

    :param alist: The list to be sorted
    :type alist: list
    """
    size = len(alist)
    # sortedEnd runs from 0 to size-1
    for sortedEnd in range(0, size):
        toInsert = alist[sortedEnd]
        # find suitable place to insert
        insertLoc = 0
        while insertLoc < sortedEnd:
            if toInsert < alist[insertLoc]:
                break
            insertLoc += 1
        # insertLoc is the location to insert
        # right shift the remainng elements in the sorted part
        for i in range(sortedEnd, insertLoc, -1):
            alist[i] = alist[i-1]
        alist[insertLoc] = toInsert
        
        # print(alist) 


# Insertion sort (Descending order)
def sortInsertionDesc(alist:list) -> None:
    """Apply insertion sort in decending order on a list

    :param alist: The list to be sorted
    :type alist: list
    """
    size = len(alist)
    # sortedEnd runs from 0 to size-1
    for sortedEnd in range(0, size):
        toInsert = alist[sortedEnd]
        # find suitable place to insert
        insertLoc = 0
        while insertLoc < sortedEnd:
            if toInsert > alist[insertLoc]:
                break
            insertLoc += 1
        # insertLoc is the location to insert
        # right shift the remainng elements in the sorted part
        for i in range(sortedEnd, insertLoc, -1):
            alist[i] = alist[i-1]
        alist[insertLoc] = toInsert


if __name__ == "__main__":
    numlist = [20, 14, 36, 8, 56, 49]
    
    sortInsertionAsc(numlist)
    print(numlist)
    
    sortInsertionDesc(numlist)
    print(numlist)
