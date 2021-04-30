print('Welcome to the algorithm for Heap Sort')
print('Input the list you want to create a Maxheap, numbers separated by space:')
inplist = [float(item) for item in input().split()]

class heapsort():
    def __init__(self, a):
        self.n = len(a)
        self.a = a
        
    def sort(self):
        self.buildheap()
        
        for i in range(self.n -1 , 0, -1):
            self.swap(0,i)
            self.n -= 1
            self.heapify(0)
            
    def buildheap(self):
        for i in range(self.n//2, -1, -1):
            self.heapify(i)
            
    def swap(self, l, r):
        self.a[l], self.a[r] = self.a[r], self.a[l]
            
    def heapify(self, i):
        left_child = 2*i + 1
        right_child = 2*i + 2
        
        if ((left_child < self.n) and (self.a[left_child] > self.a[i])):
            largest = left_child
        else:
            largest = i
            
        if ((right_child < self.n) and (self.a[right_child] > self.a[largest])):
            largest = right_child
        
        if largest != i:
            self.swap(i, largest)
            self.heapify(largest)
            
            
hs = heapsort(inplist)
hs.sort()
print('Sorted list:', hs.a)