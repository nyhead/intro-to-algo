def sieve(n):
    isPrime = n * [True]
    isPrime[0] = isPrime[1] = False   # 0 and 1 are not prime

    i = 2
    while i * i <= n:
        if isPrime[i]:
            for j in range(2 * i, n, i):
                isPrime[j] = False
        i += 1

    return isPrime

words = input().split()
nums = []
for w in words:
    nums.append(int(w))

isPrime = sieve(max(nums) + 1)

s = ''
for n in nums:
    if n % 2 == 1:
        if n > 2 and isPrime[n - 2]:
            s += '1 '
        else:
            s += '0 '
    else:
        count = 0
        for i in range(2, n // 2 + 1):
            if isPrime[i] and isPrime[n - i]:
                count += 1
        s += str(count) + ' '

print(s)
