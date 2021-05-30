print('Welcome to the algorithm for Merge Sort')
print('Input the list you want to sort, numbers separated by space:')
inplist = list(float(item) for item in input().split())

def mergesort(a):
    n = len(a)
    if n > 1:
        mid = n//2
        l1 = a[:mid]
        l2 = a[mid:]
        
        mergesort(l1)
        mergesort(l2)
        
        i = j = k = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                a[k] = l1[i]
                i += 1
            else:
                a[k] = l2[j]
                j += 1
            k += 1
            
        while i < len(l1):
            a[k] = l1[i]
            i += 1
            k += 1
 
        while j < len(l2):
            a[k] = l2[j]
            j += 1
            k += 1
            
mergesort(inplist)
print('Sorted list:', inplist)