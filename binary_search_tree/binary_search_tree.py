import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
       # print(self.value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            else:
                self = self.right
                return self.insert(value)
        else:
            value < self.value
            if self.left is None:
                self.left = BinarySearchTree(value)
                return
            else:
                self = self.left
                return self.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return(True)

        elif target > self.value:
            if self.right is None:
                return False
            else:
                self = self.right
                return self.contains(target) 
        else:    
            if self.left is None:
                return False
            else:
                self = self.left
                return self.contains(target)        
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            self = self.right
            return self.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self = self.right
            self.for_each(cb)
        if self.left is not None:
            self = self.left
            self.for_each(cb)
            

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

a = BinarySearchTree(5)

a.insert(6)

a.insert(7)

a.insert(-6)

a.insert(-7)

print(a.contains(5))
print(a.contains(6))
print(a.contains(7))
print(a.contains(-7))
print(a.contains(-8))
print(a.contains(10))
print(a.get_max())
