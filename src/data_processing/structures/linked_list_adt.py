
class Node:
    """Models the node of a linked list
    """
    def __init__(self, data=None):
        self.data = data
        self.nextobj = None
        
class LinkedList:
    """Models a linkdd list
    """
    def __init__(self):
        """The constructor
        """
        self.head = None   # the head variable is set to None

    def insert(self, data): 
        """Insert new data at the front of linked list

        :param data: The data to be inserted
        :type data: any
        """
        newnode = Node(data)
        newnode.nextobj = self.head
        self.head = newnode

    def insertEnd(self, data):  # insert new data at the end
        """Insert new data at the end of linked list

        :param data: The data to be inserted
        :type data: any
        """
        if self.head is None:       # if linked list has no node
            self.head = Node(data)  # simply add a new node
            return
        temp = self.head        # traverse to the last node
        while temp.nextobj != None:
            temp = temp.nextobj
        # now at last node
        temp.nextobj = Node(data)

    def delete(self, index:int):   # index is the position of the target node
        """Delete the node at a given index

        :param index: The index of the node to be deleted
        :type index: int
        :raises IndexError: The index is out of range
        """
        if self.head is None:
            return
        if index < 0:
            raise IndexError("Attempt to use negative index")
        # first case
        temp = self.head
        if index == 0:
            self.head = temp.nextobj
            del temp
            return
        # second case
        while index > 0:
            ptr = temp
            temp = temp.nextobj
            index -= 1  
        ptr.nextobj = temp.nextobj
        del temp

    def deleteNodeOfData(self, targetdata):
        """ Delete the node containing the target data

        :param targetdata: The target data of which the node is to be deleted
        :type targetdata: any
        """
        if self.head is None:
            return
        # first case
        temp = self.head
        if temp.data == targetdata:
            self.head = temp.nextobj
            del temp
            return
        # second case
        while temp != None and temp.data != targetdata:
            ptr = temp
            temp = temp.nextobj
        if temp is None:
            return
        ptr.nextobj = temp.nextobj
        del temp

    def print(self):   
        """ Printing all nodes by traversal
        """
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.nextobj

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert('Anders')
    linkedlist.insert('Betsy')
    linkedlist.insert('Chris')
    print("Content of linked list:")
    linkedlist.print()

    linkedlist.insertEnd('Doris')
    linkedlist.insertEnd('Eva')
    linkedlist.insertEnd('Frances')
    print("Content of linked list:")
    linkedlist.print()

    linkedlist.delete(4)
    print("Content of linked list:")
    linkedlist.print()

    linkedlist.deleteNodeOfData('Doris')
    print("Content of linked list:")
    linkedlist.print()
