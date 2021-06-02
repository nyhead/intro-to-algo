n = int(input())

i = 2
s = []

while i * i <= n:
  if n % i == 0:
    s.append(i)
    n = n // i
  else:
    i += 1
    
s.append(n)

fin_str = ''
for i in range(len(s)):
    if s[i] != 0:
        curr = s[i]
        count = 0       
        for j in range(len(s)):
            if curr == s[j]:
                count += 1
                s[j] = 0
        if count == 1:        
            fin_str = fin_str + str(curr) + ' * '
        else:
            fin_str = fin_str + str(curr) + '^' + str(count) + ' * '

f = len(fin_str)-2
print(fin_str[:f])


