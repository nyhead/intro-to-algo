import math
import copy

class Node:
    def __init__(self, left, val, right):
        self.left = left
        self.val = val
        self.right = right

class TreeSet:
    def __init__(self):
        self.root = None
        self.len = 0

    def contains(self, x):
        n = self.root
        while n != None:
            if x == n.val:
                return True
            if x < n.val:
                n = n.left
            else:
               n = n.right
        return False
    
    def add(self, x):
        new_node = Node(None, x, None)
        
        n = self.root
        if n == None:
            self.root = new_node
            self.len += 1
            return
        
        while True:
            if x == n.val:
                return  # already present
            elif x < n.val:
                if n.left == None:
                    n.left = new_node
                    self.len += 1
                    return
                else:
                    n = n.left
            else:
                if n.right == None:
                    n.right = new_node
                    self.len += 1
                    return
                else:
                    n = n.right    

    # Given a node n and its parent (if any), replace n with a node p.
    def replace(self, parent, n, p):
        if parent == None:      # n is the root
            self.root = p
        elif parent.left == n:  # n is the left child
            parent.left = p
        elif parent.right == n: # n is the right child
            parent.right = p
        else:
            assert False, 'not a child'

    # Given a node n and its parent, remove the smallest value from
    # the subtree rooted at n, and return it.
    def remove_smallest(self, parent, n):
        while n.left != None:
            parent = n
            n = n.left
        self.replace(parent, n, n.right)  # replace n with its right child
        return n.val

    def remove(self, x):
        parent =  None
        n = self.root

        while n and n.val != x:
            parent = n
            if x < n.val:
                n = n.left
            elif x > n.val:
                n = n.right            

        if n == None or n.val != x:
            return
        elif n.left == None and n.right == None:
            self.replace(parent, n, None)
        elif n.left and n.right == None:
            self.replace(parent, n, n.left)
        elif n.left == None and n.right:
            self.replace(parent, n, n.right)
        else:
            removed = self.remove_smallest(n, n.right)
            n.val = removed
        self.len -= 1
    
    def max(self):
        max_return = max_in_tree(self.root)
        return None if max_return == -math.inf else max_return  
    
    def min(self):
        min_return = min_in_tree(self.root)
        return None if min_return == math.inf else min_return        

    def size(self):
        return self.len
    
    def count(self, lo, hi):
        return count_in_tree(self.root, lo, hi)
    
    def ceil(self, x):
        ceil = ceil_in_tree(self.root, x)
        return None if ceil == -math.inf else ceil

    def floor(self, x):
        floor = floor_in_tree(self.root, x)
        return None if floor == math.inf else floor

    def avg_tree_depth(self):
        if self.len == 0:
            return None
        return average_depth(self.root, 0) / self.len

def replace(root, parent, n, p):
    if parent == None:      # n is the root
        root = p
    elif parent.left == n:  # n is the left child
        parent.left = p
    elif parent.right == n: # n is the right child
        parent.right = p
    else:
        assert False, 'not a child'

def count_in_tree(root, lo, hi):
    if root == None:
        return 0

    if root.val == hi and root.val == lo:
        return 1

    if root.val <= hi and root.val >= lo:
        return (1 + count_in_tree(root.left, lo, hi) +
                count_in_tree(root.right, lo, hi))

    elif root.val < lo:
        return count_in_tree(root.right, lo, hi)

    else:
        return count_in_tree(root.left, lo, hi)

def max_in_tree(root):
    if root == None:
        return - math.inf
    
    left_max = max_in_tree(root.left)
    right_max = max_in_tree(root.right)

    return max(left_max, root.val, right_max)

def min_in_tree(root):
    if root == None:
        return math.inf
    
    left_min = min_in_tree(root.left)
    right_min = min_in_tree(root.right)

    return min(left_min, root.val, right_min)

def ceil_in_tree(root, x):
    if root == None:
        return - math.inf

    if root.val == x:
        return root.val
    elif root.val < x:
        return ceil_in_tree(root.right, x)

    ceil = ceil_in_tree(root.left, x)
    return ceil if ceil >= x else root.val

def floor_in_tree(root, x):
    if root == None:
        return math.inf

    if root.val == x:
        return root.val
    elif root.val > x:
        return floor_in_tree(root.left, x)
    floor = floor_in_tree(root.right, x)
    return floor if floor <= x else root.val    

def average_depth(root, accum):
    if root == None:
        return 0
        
    leftDepth = average_depth(root.left, accum + 1)
    rightDepth = average_depth(root.right, accum + 1)

    return accum + leftDepth + rightDepth    