import numpy as np
def rod_cutting(price):
    n = len(price)
    max_revenue = np.empty(n+1)
    config = np.empty(n)
    max_revenue[0] = 0
    
    for i in range(1, n+1):
        q = -float('inf')
        for j in range(1,i+1):
            if q < price[j-1] + max_revenue[i-j]:
                q = price[j-1] + max_revenue[i-j]
                config[i-1] = j
        max_revenue[i] = q
        print('Max revenue is %.2f corresponding to cut of length %d and %d' %(max_revenue[i], config[i-1], i-config[i-1]))
        
rod_cutting([1,5,8,9,10,17,17,20,24,30])