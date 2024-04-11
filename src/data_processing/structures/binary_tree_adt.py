# Binary Search Tree Implementation
# with separated key and data

class Node:
    """ Models a node in a binary search tree
    """
    def __init__(self, key, data=None):
        """The constructor

        :param key: The key for the binary search tree
        :type key: any immutable type
        :param data: The payload, defaults to None
        :type data: any, optional
        """
        self.key = key    # the key for BST
        self.data = data  # the payload
        self.left = None
        self.right = None

    def insert(self, key, data=None):
        """Insert data as a nodein the binary search tree

        :param key: The key for the binary search tree
        :type key: any immutable type
        :param data: The payload, defaults to None
        :type data: any, optional
        """
        if self.key is None:
            return
        if key < self.key:
            if self.left is None:
                self.left = Node(key, data)
            else:
                self.left.insert(key, data)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, data)
            else:
                self.right.insert(key, data)
        else:
            self.data = data # replace the data if duplicated key

    # searching for data based on key
    # return data
    def searchKey(self, key):
        """ Search for data using the query key

        :param key: The key for the binary search tree
        :type key: any immutable type
        :return: The data or None if the key is not found
        :rtype: any
        """
        if self.key is None:
            return None
        if key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.searchKey(key)            
        elif key > self.key:
            if self.right is None:
                return None
            else:
                return self.right.searchKey(key)
        else:
            return self.data  # the key is found        

    # pre-order traversal
    def printPreOrder(self):
        """ Print the data in a binary search tree in pre-order traveral
        """
        print(self.key, self.data)
        if self.left:
            self.left.printPreOrder()
        if self.right:
            self.right.printPreOrder()
            
    # in-order traversal
    def printInOrder(self):
        """ Print the data in a binary search tree in in-order traveral
        """
        if self.left:
            self.left.printInOrder()
        print(self.key, self.data)
        if self.right:
            self.right.printInOrder()

    # in-order traversal reverse
    def printInOrderReverse(self):
        """ Print the data in a binary search tree in reverse in-order traveral
        """
        if self.right:
            self.right.printInOrderReverse()
        print(self.key, self.data)
        if self.left:
            self.left.printInOrderReverse()
            
    # post-order traversal
    def printPostOrder(self):
        """ Print the data in a binary search tree in post-order traveral
        """
        if self.left:
            self.left.printPostOrder()
        if self.right:
            self.right.printPostOrder()
        print(self.key, self.data)

    # returns the number of nodes
    def countNodes(self) -> int:
        """Returns the number of nodes in a binary search tree

        :return: The number of nodes
        :rtype: int
        """
        count = 1
        if self.left:
            count += self.left.countNodes()
        if self.right:
            count += self.right.countNodes()
        return count

    # returns height of tree
    def treeHeight(self) -> int:
        """Returns the height of a binary search tree

        :return: The tree height
        :rtype: int
        """
        leftheight = rightheight = 0
        if self.left:
            leftheight = self.left.treeHeight() + 1
        if self.right:
            rightheight = self.right.treeHeight() + 1
        return max(leftheight, rightheight)


class BSTree:
    """Models a binary search tree (BST)
    """
    def __init__(self):
        """The constructor
        """
        self.root = None  # link to root node

    def insert(self, key, data=None):
        """Insert a data as a node in this BST

        :param key: The key for the binary search tree
        :type key: any immutable type
        :param data: The payload, defaults to None
        :type data: any, optional
        """
        if self.root is None:
            self.root = Node(key, data)
        else:
            self.root.insert(key, data)

    # searching for data based on key
    # return data
    def searchKey(self, key):
        """Search for the node that contains the key in this BST

        :param key: The key for the binary search tree
        :type key: any immutable type
        :return: The node or None if not found
        :rtype: any
        """
        if self.root:
            return self.root.searchKey(key)
        return None  

    def printPreOrder(self):
        """ Print the data in a binary search tree in pre-order traveral
        """
        if self.root:
            self.root.printPreOrder()

    def printInOrder(self):
        """ Print the data in a binary search tree in in-order traveral
        """
        if self.root:
            self.root.printInOrder()

    def printInOrderReverse(self):
        """ Print the data in a binary search tree in reverse in-order traveral
        """
        if self.root:
            self.root.printInOrderReverse()

    def printPostOrder(self):
        """ Print the data in a binary search tree in post-order traveral
        """
        if self.root:
            self.root.printPostOrder()
            
    # returns the number of nodes
    def countNodes(self) -> int:
        """Returns the number of nodes in a binary search tree

        :return: The number of nodes
        :rtype: int
        """
        if self.root:
            return self.root.countNodes()
        return 0

    # returns height of tree
    def treeHeight(self) -> int:
        """Returns the height of a binary search tree

        :return: The tree height
        :rtype: int
        """
        if self.root:
            return self.root.treeHeight()
        return None  # height is None for empty tree        

if __name__ == "__main__":
    tree = BSTree()
    numlist = [34, 23, 4, 15, 28, 53, 38, 36, 72]
    for num in numlist:    # add numbers to the binary tree
        tree.insert(num)
    print("Pre-order traversal")
    tree.printPreOrder()    
    print("In-order traversal")
    tree.printInOrder()
    print("Post-order traversal")
    tree.printPostOrder()

    print("In-order traversal reverse")
    tree.printInOrderReverse()
    print("Number of nodes = ", tree.countNodes())
    print("Height of tree = ", tree.treeHeight())
