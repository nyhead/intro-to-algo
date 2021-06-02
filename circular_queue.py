class CircularQueue:
    def __init__(self, size):
        self.a = size * [None]
        self.head = 0   # points to first element
        self.tail = 0   # points to free slot after last element
        self.sum = 0
    
    def enqueue(self, x):
        self.a[self.tail] = x   # add element at tail
        self.tail = (self.tail + 1) % len(self.a)
        self.sum += x
        
        if self.head == self.tail:    # array is full
            old_size = len(self.a)
            self.a = self.a[self.head:] + self.a[:self.head] + old_size * [None]
            print('Resized to', 2 * old_size, 'elements')
            self.head = 0
            self.tail = old_size
    
    def dequeue(self):
        x = self.a[self.head]   # remove element at head
        self.head = (self.head + 1) % len(self.a)
        self.sum -= x
        return x

    def count(self):
        return (self.tail - self.head) % len(self.a)
        
    def avg(self):
        return self.sum / self.count()
