def insertionsort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        
        while (j>=0) and (key<a[j]):
            a[j+1] = a[j]
            j -=1
            
        a[j+1] = key
        
    return a

def bucket_sort(a):
    mini = min(a)
    maxi = max(a)
    buckets = 10
    b = []
    
    for i in range(buckets):
        b.append([])
        
    for i in range(len(a)):
        b[int(((a[i] - mini)/(maxi))*buckets)].append(a[i])
        
    for i in range(buckets):
        b[i] = insertionsort(b[i])
     
    k = 0
    for i in range(buckets):
        for j in range(len(b[i])):
            a[k] = b[i][j]
            k += 1
            
    return a

print('Welcome to the algorithm for Bucket Sort')
print('Input the list you want to sort, numbers separated by space:')
inplist = list(float(item) for item in input().split())
print('Sorted list:', bucket_sort(inplist))