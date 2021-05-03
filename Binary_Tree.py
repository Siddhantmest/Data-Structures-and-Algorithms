print('Welcome to the code for implementing Binary Tree')

class tree:
    def __init__(self, a):
        self.left = None
        self.right = None
        self.data = a
        self.size = 1
        self.parent = None
        
    def insert_element(self, a):
        self.size += 1
        if self.data is not None:
            if a < self.data:
                if self.left is None:
                    self.left = tree(a)
                    self.left.parent = self
                else:
                    self.left.insert_element(a)
                    
            else:
                if self.right is None:
                    self.right = tree(a)
                    self.right.parent = self
                else:
                    self.right.insert_element(a)
                    
        else:
            self.data = a
            
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()
            
    def iterative_search(self, r, b):
        while r is not None:
            if b < r.data:
                r = r.left
                
            elif b > r.data:
                r = r.right 
                
            else:
                return True
            
        return False
    
    def minimum(self):
        while self.left is not None:
            self = self.left
            
        return self.data
    
    def return_subtree(self, r, b):
        while r is not None:
            if b < r.data:
                r = r.left
                
            elif b > r.data:
                r = r.right 
                
            else:
                return r
            
        return False
    
    #x should be a tree
    def successor(self, x):
        x1 = x
        if x.right is not None:
            return (x.right.minimum())
        
        else:
            y = x.parent
            while (y is not None) and (x == y.right):
                x = y
                y = y.parent
                
            if (y is None) and (self.data >= x1.data):
                return self.data
            elif y is not None:
                return y.data
            
    def deleteNode(self, key):
        if self is None:
            return self

        if key < self.data:
            self.left = self.left.deleteNode(key)
     
        elif(key > self.data):
            self.right = self.right.deleteNode(key)
     
        else:
            if self.left is None:
                return self.right
     
            elif self.right is None:
                return self.left

            temp = self.right.minimum()

            self.data = temp
  
            self.right = self.right.deleteNode(temp)
      
        return self
    
print('How many elements you want to input:')
n = int(input())
for i in range(n):
    print('Press enter after each element you input')
    if i == 0:
        a = tree(float(input()))
    else:
        a.insert_element(float(input()))
        
print('Elements in increasing order are:')
a.inorder_traversal()

#a.data is the first element that you input
#while performing search you need to pass r to be the tree object not a float (a.data)

print('Input the element you want to search:')
if a.iterative_search(a, float(input())):
    print('element found')
else:
    print('element not found')
    
print('Minimum key in the binary tree is: ', a.minimum())

print('Input the element whos successor needs to be output:')
inp = float(input())
if a.return_subtree(a, inp):
    tr = a.return_subtree(a, inp)
    if a.successor(tr):
        print('The successor of %.2f is %.2f'%(inp, a.successor(tr)))
    else:
        print('The successor of %.2f doesnt exist'%(inp))
else:
    print('The input element is not in the tree')
    
print('Input the element that needs to be deleted from the tree:')
inp = float(input())
if a.iterative_search(a, inp):
    print('Element found')
    a.deleteNode(inp)
    print('Element Successfully deleted')
    print('Element in the increasing order are:')
    a.inorder_traversal()
else:
    print('element not found')