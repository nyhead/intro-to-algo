a = int(input())
b = int(input())

p = 0
min = None
max = None
for i in range(a, b+1):
    prime = True
    j = 2
    while j * j  <= i:
        if i % j == 0:
            prime = False
            break
        j += 1
    if prime:
        max = i
        p += 1
    if prime and p == 1:
        min = i

per = (p / (b - a + 1)) * 100

print(f'Number of primes: {p}\nSmallest prime: {min}\nLargest prime: {max}\nPercentage of numbers that are prime: {per:.1f}')