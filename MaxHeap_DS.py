print('Welcome to the code for Heap Data Structure')
print('Input the list you want to create a Maxheap, numbers separated by space:')
inplist = [float(item) for item in input().split()]

class MaxHeap:
    def __init__(self, a):
        self.n = len(a)
        self.a = a
        
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
            
    def extract_max(self):
        maxed = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n -= 1
        self.heapify(0)
        return maxed
    
    def return_max(self):
        return print('The maximum value of heap is ', self.a[0])
    
    def parent(self, position):
        # The condition is because of the insert_element, when it reaches the root 
        # it points the parent at the last element of the heap
        if (position-1)//2 >= 0:
            return (position-1)//2
        else:
            return 0
    
    def insert_element(self, elem):
        self.a.append(elem)
        self.n += 1
        
        current = self.n - 1 
        
        while self.a[self.parent(current)] < self.a[current]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
            
    def Print(self):
        for i in range(0, (self.n//2)):
            if (2*i + 2) < (self.n):
                print(" PARENT : "+ str(self.a[i])+" LEFT CHILD : "+
                                str(self.a[2 * i + 1])+" RIGHT CHILD : "+
                                str(self.a[2 * i + 2]))
            elif (2*i + 1) == (self.n - 1):
                print(" PARENT : "+ str(self.a[i])+" LEFT CHILD : "+
                                str(self.a[2 * i + 1]))
            
mh = MaxHeap(inplist)
mh.buildheap()
mh.Print()
mh.return_max()
print('Press 1 to insert more elements')
print('Press 2 to quit')
key = int(input())
while key == 1:
    print('How many more elements you want to input')
    num = int(input())
    for i in range(num):
        print('Press enter after each element you input')
        mh.insert_element(int(input()))
    #mh.buidheap()
    mh.Print()
    mh.return_max()
    print('Press 1 to insert more elements')
    print('Press 2 to quit')
    key = int(input())