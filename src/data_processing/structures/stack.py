
class Stack:
    """Models a FILO stack
    """
    def __init__(self):
        """The constructor
        """
        self.data = list()  # create an empty list

    def push(self, value):
        """Push the value on top of the stack

        :param value: The value to be pushed to the stack
        :type value: any
        """
        self.data.append(value)

    def pop(self):
        """Remove the value on the top of the stack

        :raises IndexError: The stack is empty
        :return: The value at the top of the stack
        :rtype: any
        """
        if len(self.data) == 0:
            raise IndexError('Attempt to pop an empty stack')
        value = self.data.pop()  # from last index
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

    theStack = Stack()
    theStack.push(20)
    theStack.push(15)
    theStack.push(36)
    theStack.push(8)
    theStack.push(26)
    print("Content of the stack (top at the end): ", end='')
    theStack.print()
    while not theStack.isEmpty():
        print(theStack.pop())

