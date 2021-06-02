import sys
from priority_queue import PriorityQueue

n = int(input())

pq = PriorityQueue()

count = 0
while True:
    if pq.count() == n:
        x = pq.remove_largest()
        print(x.elem, x.prio)

    line = sys.stdin.readline()

    if line: 
        line = line.split()
    else: 
        for _ in range(pq.count()):
            node = pq.remove_largest()
            print(node.elem, node.prio)            
        break

    pq.add(line[0], float(line[1]))