print('Welcome to the algorithm for Insertion Sort')
print('Input the list you want to sort, numbers separated by space:')
inplist = list(float(item) for item in input().split())

def insertionsort(a):
    for i in range(1,(len(a))):
        key = a[i]
        j = i - 1
        
        while (j >= 0) and (key < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        
    return a

print('Sorted list:', insertionsort(inplist))