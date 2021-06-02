from sys import stdin

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

def my_hash(s):
    h = 0
    for c in s:
        h = (1_000_003 * h + ord(c)) % (2 ** 32)
    return h

class HashMap:
    def __init__(self):
        self.a = 5 * [None]
        self.count = 0
    
    def find(self, key):
        b = my_hash(key) % len(self.a)
        n = self.a[b]
        while n != None:
            if n.key == key:
                break
            n = n.next
        return n
    
    def insert(self, key, value):
        b = my_hash(key) % len(self.a)
        self.a[b] = Node(key, value, self.a[b])   # prepend
    
    def rehash(self):
        old = self.a
        self.a = (2 * len(self.a)) * [None]
        print(f'resizing to {len(self.a)} buckets')
        for head in old:
            n = head
            while n != None:
                self.insert(n.key, n.value)
                n = n.next
    
    def set(self, key, value):
        n = self.find(key)
        if n != None:
            n.value = value
        else:
            if self.count >= len(self.a) * 4:
                self.rehash()
            self.insert(key, value)
            self.count += 1
    
    def get(self, key):
        n = self.find(key)
        if n != None:
            return n.value
        else:
            return None
        
    def remove(self, key):
        b = my_hash(key) % len(self.a)
        if self.a[b] == None:
            return
        n = self.a[b]
        if n.key == key:
            self.a[b] = n.next
            return
        while n.next != None:
            if n.next.key == key:
                n.next = n.next.next
                self.count -= 1
                return
            n = n.next

m = HashMap()

while True:
    line = stdin.readline()
    if line.strip() == '== END ==':
        break
    word = ''
    for c in line:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            word += c.lower()
        elif word:
            count = m.get(word)
            if count:
                m.set(word, count + 1)
            else:
                m.set(word, 1)
            word = ''

print('unique words =', m.count)

for line in stdin:
    word = line.strip()
    count = m.get(word)
    if count:
        print(word, count)
        m.remove(word)
    else:
        print(word, 'None')
