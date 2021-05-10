def counting_sort(a):
    b = []
    c = []
    n = len(a)
    k = max(a)
    for i in range(k):
        c.append(0)
    for j in range(n):
        c[a[j]-1] += 1
        b.append(0)
    for i in range(1, k):
        c[i] += c[i-1]
    for j in range(n-1, -1, -1):
        b[c[a[j]-1]-1] = a[j]
        c[a[j]-1] -= 1
        
    return b
        
print('Input the intergers greater than 0 to be sorted separated by space')
lis = [int(item) for item in input().split()]
print('Sorted list is ', counting_sort(lis))