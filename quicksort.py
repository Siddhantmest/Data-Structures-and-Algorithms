print('Welcome to the algorithm for Quciksort')
print('Input the list you want to sort, numbers separated by space:')
inplist = [float(item) for item in input().split()]

def partition(a, start, end):
    x = a[end]
    i = start - 1
    
    for j in range(start, end):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[end] = a[end], a[i+1]
    
    return i+1

def quicksort(a, start, end):
    if start<end:
        q = partition(a, start, end)
        quicksort(a, start, q-1)
        quicksort(a, q+1, end)
        
quicksort(inplist, 0, len(inplist) - 1)

print('sorted array ', inplist)