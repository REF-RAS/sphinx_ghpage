
class Queue:
    """Models a FIFO queue
    """
    def __init__(self):
        """The constructor
        """
        self.data = list()  # create an empty list

    def enQueue(self, value):
        """Add a value at the end of the queue

        :param value: The value to be added
        :type value: any
        """
        self.data.append(value)

    def deQueue(self):
        """ Remove the value at the front of the queue

        :raises IndexError: The queue is empty
        :return: The data removed at the front
        :rtype: any
        """
        if len(self.data) == 0:
            raise IndexError('Attempt to deQueue an empty queue')
        value = self.data.pop(0)
        return value
        
    def isEmpty(self) -> bool:
        """Returns True if the queue is empty

        :return: True if the queue is empty
        :rtype: bool
        """
        return len(self.data) == 0

    def isFull(self) -> bool:
        """Returns True if the queue is full

        :return: True if the queue is full
        :rtype: bool
        """
        return False

    def print(self, sep=','):
        """ Print the content of the queue

        :param sep: The separating character between the values in the queue, defaults to ','
        :type sep: str, optional
        """
        isFirst = True
        for value in self.data:
            if not isFirst:
                print(sep, end='')
            print(value, end='')
            isFirst = False
        print() # add a new line at the end

if __name__ == "__main__":
    theQueue = Queue()
    theQueue.enQueue(20)
    theQueue.enQueue(15)
    theQueue.enQueue(36)
    theQueue.enQueue(8)
    theQueue.enQueue(26)
    print("Content of the queue: ", end='')
    theQueue.print()
    while not theQueue.isEmpty():
        print(theQueue.deQueue())

