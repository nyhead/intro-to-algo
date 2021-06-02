import sys

class Wagon:
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight
        self.next = None

class WagonQueue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0  # total length of all wagons in queue
        self.weight = 0  # total weight of all wagons in queue
    
    def enqueue(self, wagon):
        if self.head == None:
            self.head = self.tail = wagon
        else:
            self.tail.next = wagon
            self.tail = wagon
        self.length += wagon.length
        self.weight += wagon.weight
        
    def dequeue(self):
        self.length -= self.head.length
        self.weight -= self.head.weight
        self.head = self.head.next

bridge_length, capacity = [int(w) for w in input().split()]
queue = WagonQueue()

def read_train():
    count = 0
    for line in sys.stdin:
        nums = [int(w) for w in line.split()]
        for i in range(0, len(nums), 2):
            count += 1
            
            # Remove wagons until there is room for the next wagon to begin to enter.
            # We don't count the length of the wagon at the head in this calculation,
            # since only a tiny part of it might still be on the bridge when the
            # next wagon enters.
            while queue.head != None and queue.length - queue.head.length >= bridge_length:
                queue.dequeue()
                
            queue.enqueue(Wagon(nums[i], nums[i + 1]))
            
            if queue.weight > capacity:   # too heavy
                print(count)
                return
    print(-1)   # all wagons OK

read_train()
