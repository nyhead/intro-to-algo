# Given a array of non-decreasing values, find the first one that is >= k.
def firstAtLeast(a, k):
  lo = 0
  hi = len(a) - 1

  while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] < k:
      lo = mid + 1
    else:   # a[mid] >= k
      hi = mid - 1

  return hi

n = int(input())

a = []
for w in input().split():
  a.append(int(w))

for w in input().split():
  i = int(w)
  print(firstAtLeast(a, i + 1) - firstAtLeast(a, i))
