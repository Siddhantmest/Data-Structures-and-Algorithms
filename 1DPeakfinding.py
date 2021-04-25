print('Welcome to the algorithm for finding any peak in 1D.')

def peakfinder(a):
    mid = len(a)//2
    if mid == 0:
        return float(a[0]) if len(a) == 1 else None
    elif len(a) == 2:
        if a[0] >= a[1]:
            return float(a[0])
        else:
            return float(a[1])
    else:
        if ((a[mid-1] <= a[mid]) and (a[mid] >= a[mid+1])):
            return float(a[mid])
        elif a[mid-1] <= a[mid]:
            return peakfinder(a[mid:])
        else:
            return peakfinder(a[:mid])
        
        
print("the peak of the list is: ", peakfinder(list(int(item) for item in input("Enter the list items separated by space: ").split())))