class Node:
    def __init__(self, elem, prio):
        self.elem = elem
        self.prio = prio

class PriorityQueue:
    def __init__(self):
        self.a = []
        self.currentSize = 0

    def add(self, elem, prio):
        self.a.append(Node(elem, prio))
        self.up_heap(self.currentSize)
        self.currentSize += 1
    
    def up_heap(self, i):
        a = self.a
        while i != 0:
            if a[i].prio > a[parent(i)].prio:
                a[i], a[parent(i)] = a[parent(i)], a[i]
            i = parent(i)
    def down_heap(self, i):
        a = self.a
        while True:
            m = a[i].prio
            if left(i) < len(a):   # left child exists
                m = max(m, a[left(i)].prio)
            if right(i) < len(a):  # right child exists
                m = max(m, a[right(i)].prio)
            if m == a[i].prio:  # a[i] is larger than any children
                break
            if m == a[left(i)].prio:   # left child is largest
                a[i], a[left(i)] = a[left(i)], a[i]   # swap with left child
                i = left(i)
            else:   # right child is largest
                a[i], a[right(i)] = a[right(i)], a[i]  # swap with right child
                i = right(i)

    def remove_largest(self):
        if len(self.a) == 1:
            return self.a.pop()
        x = self.a[0]
        self.a[0] = self.a.pop()
        self.currentSize -= 1
        self.down_heap(0)
        return x
    
    def count(self): return self.currentSize
def left(i):
    return (2 * i + 1)
    
def right(i):
    return (2 * i + 2)
    
def parent(i):
    return ((i - 1) // 2)