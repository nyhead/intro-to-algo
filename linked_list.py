class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# Return True if the linked list p starts with the linked list q.
def starts_with(p, q):
    while q != None:
        if p == None or p.val != q.val:
            return False
        p = p.next
        q = q.next
    return True

class LinkedList:
    def __init__(self, a):
        n = None
        for i in range(len(a) - 1, -1, -1):
            n = Node(a[i], n)
        self.head = n
    
    def to_list(self):
        a = []
        p = self.head
        while p != None:
            a.append(p.val)
            p = p.next
        return a
    
    def len(self):
        n = 0
        p = self.head
        while p != None:
            n += 1
            p = p.next
        return n
    
    def get(self, n):
        p = self.head
        for i in range(n):
            p = p.next
        return p.val
    
    def has(self, x):
        p = self.head
        while p != None:
            if p.val == x:
                return True
            p = p.next
        return False

    def delete(self, x):
        p = self.head
        if p == None:   # empty list
            return
        if p.val == x:  # deleting the first element
            self.head = p.next
            return
        while p.next != None:
            if p.next.val == x:
                p.next = p.next.next
                return
            p = p.next

    def rotate(self):
        p = self.head
        if p == None or p.next == None:
            return
            
        while p.next.next != None:
            p = p.next
            
        # remove last node
        n = p.next
        p.next = None
        
        # prepend at beginning
        n.next = self.head
        self.head = n
        
    def starts_with(self, m):
        return starts_with(self.head, m.head)
    
    def contains(self, m):
        p = self.head
        while p != None:
            if starts_with(p, m.head):
                return True
            p = p.next
        return False
        
    def ends_with(self, m):
        self_len = self.len()
        m_len = m.len()
        p = self.head
        for i in range(self_len - m_len):
            p = p.next
        return starts_with(p, m.head)
