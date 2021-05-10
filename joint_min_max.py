def joint_min_max(a):
    mini = min(a[0], a[1])
    maxi = max(a[0], a[1])
    
    n = len(a)
    
    for i in range(2, n, 2):
        
        try:
            min1 = min(a[i], a[i+1])
            max1 = max(a[i], a[i+1])
            
            if min1 < mini:
                mini = min1
            elif max1 > maxi:
                maxi = max1
        except:
            min1 = a[i]
            max1 = a[i]
            
            if min1 < mini:
                mini = min1
            elif max1 > maxi:
                maxi = max1
                
    return mini, maxi
    

print('Input the list to find it"s minimum and maximum')
lis = [int(item) for item in input().split()]
mini, maxi = joint_min_max(lis)
print('Minimum of the list is {} and maximum is {}'.format(mini, maxi))