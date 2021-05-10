def counting_sort(a, div):
    b = []
    c = []
    n = len(a)
    k = 10 # 0 to 9 for digits
    for i in range(k):
        c.append(0)
    for j in range(n):
        digit = a[j]/div
        c[int(digit%10)] += 1
        b.append(0)
    for i in range(1, k):
        c[i] += c[i-1]
    for j in range(n-1, -1, -1):
        digit = a[j]/div
        b[c[int(digit%10)]-1] = a[j]
        c[int(digit%10)] -= 1
    for j in range(n):
        a[j] = b[j]
    

def radix_sort(a):
    max_elem = max(a)
    div = 1
    
    while max_elem/div > 0:
        counting_sort(a, div)
        div *= 10
        
        
print('Input the intergers greater than 0 to be sorted separated by space')
lis = [int(item) for item in input().split()]
radix_sort(lis)
print('Sorted list is ', lis)