from random import randrange

def partition(a, start, end):
    x = a[end]
    i = start - 1
    
    for j in range(start, end):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[end] = a[end], a[i+1]
    
    return i+1

def random_partition(a, start, end):
    ind = randrange(start, end)
    a[end], a[ind] = a[ind], a[end]
    
    return partition(a, start, end)

def select(a, start, end, i):
    if start == end:
        return a[start]
    else:
        q = random_partition(a, start, end)
        if i == q:
            return a[int(i)]
        elif i<q:
            return select(a, start, q-1, i)
        else:
            return select(a, q+1, end, i)
        
print('Welcome to the algorithm for Randomized Selection for ith smallest element')
print('Input the numbers in the list separated by space:')
inplist = [float(item) for item in input().split()]
print('Input the value of i for the ith smallest element:')
i = float(input())
if i <= len(inplist)-1:
    print('The {}th smallest element is {}'.format(int(i), select(inplist, 0, len(inplist) - 1, i)))
else:
    print('Number outside the list size')

