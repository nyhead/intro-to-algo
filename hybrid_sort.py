def report(level, s):
    print('    ' * level + s)

# insertion sort of a[d:e]
def insertion_sort(a, d, e, level):
    count = 0
    for i in range(d, e):
        t = a[i]
        j = i - 1
        while j >= d:
            count += 1      # we are about to compare two elements
            if a[j] <= t:
                break       # no need to shift this element
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t
    report(level, f'insertion sort ({count} compares)')

# merge sorted subarrays arr[d:e] and arr[e:f] into the subarray arr[d:f]
def merge(arr, d, e, f, level):
    if arr[e - 1] <= arr[e]:
        report(level, 'skipped merge!')
        return
    
    a = arr[d:e]            # copy of left half
    b = arr[e:f]            # copy of right half

    i = 0     # index into a
    j = 0     # index into b
    
    for k in range(d, f):
        if i == len(a):         # a has no more elements
            arr[k] = b[j]         
            j += 1
        elif j == len(b):     # b has no more elements
            arr[k] = a[i]         
            i += 1
        elif a[i] < b[j]:
            arr[k] = a[i]         
            i += 1
        else:
            arr[k] = b[j]         
            j += 1
            
    report(level, f'merged a[{d}:{e}] + a[{e}:{f}] -> a[{d}:{f}]')

def numrange(a, i, j):
    return ' '.join([str(a[k]) for k in range(i, j)])

def describe(a, i, j):
    if j - i <= 10:
        nums = numrange(a, i, j)
    else:
        nums = numrange(a, i, i + 5) + " ... " + numrange(a, j - 5, j)
    return f'a[{i}:{j}] = [{nums}]'

# sort only elements a[i:j], i.e. a[i .. (j - 1)]
def merge_sort_range(a, i, j, level):
    report(level, 'sorting ' + describe(a, i, j))
    
    if j - i < 2:
        pass
    elif j - i <= 10:
        insertion_sort(a, i, j, level + 1)
    else:
        mid = (i + j) // 2
        
        merge_sort_range(a, i, mid, level + 1)         # recursively sort left half
        merge_sort_range(a, mid, j, level + 1)         # recursively sort right half
        
        merge(a, i, mid, j, level + 1)     # merge left and right halves together

    report(level, 'sorted ' + describe(a, i, j))

def merge_sort(a):
    merge_sort_range(a, 0, len(a), 0)

nums = [int(x) for x in input().split()]
merge_sort(nums)
