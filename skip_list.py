from random import random

class node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None]*(level+1)
        
class skip_list:
    def __init__(self, maxlevels, probability):
        self.max_level = maxlevels
        self.header = self.create_node(float('-inf'), self.max_level)
        self.prob = probability
        self.level = 0
        
    def create_node(self, key, level):
        return node(key, level)
    
    def rand_level(self):
        level = 0
        while (random() <= self.prob) and (level < self.max_level):
            level += 1
            
        return level
    
    def insert_element(self, key):
        update_level = [None]*(self.max_level+1)
        current_position = self.header
        
        for i in range(self.level, -1, -1):
            while current_position.forward[i] and current_position.forward[i].key < key:
                current_position = current_position.forward[i]
                
            update_level[i] = current_position
            
        current_position = current_position.forward[0]
        
        if current_position == None or current_position.key != key:
            lev = self.rand_level()
            
        if lev > self.level:
            for i in range(self.level+1, lev+1):
                update_level[i] = self.header
            self.level = lev
            
        nde = self.create_node(key, lev)
        
        for i in range(lev+1):
            nde.forward[i] = update_level[i].forward[i]
            update_level[i].forward[i] = nde
            
        print("Successfully inserted key {}".format(key))
        
    def delete_element(self, key):
        update_level = [None]*(self.max_level+1)
        current_position = self.header
        
        for i in range(self.level, -1, -1):
            while current_position.forward[i] and current_position.forward[i].key < key:
                current_position = current_position.forward[i]
                
            update_level[i] = current_position
            
        current_position = current_position.forward[0]
        
        if current_position != None and current_position.key == key:
            for i in range(self.level+1):
                if update_level[i].forward[i] != current_position:
                    break
                update_level[i].forward[i] = current_position.forward[i]
                
            while(self.level>0 and self.header.forward[self.level] == None):
                self.level -= 1
            print("Successfully deleted {}".format(key))
            
    def search_element(self, key):
        current_position = self.header
        
        for i in range(self.level, -1, -1):
            while current_position.forward[i] and current_position.forward[i].key < key:
                current_position = current_position.forward[i]
            
        current_position = current_position.forward[0]
        
        if current_position != None and current_position.key == key:
            print('Found key ', key)
        else:
            print('Could not find key ', key)
    
    def displayList(self):
        print("\n*****Skip List******")
        head = self.header
        for lvl in range(self.level+1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while(node != None):
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")
            
print('Enter the maximum level and the probability to increase the level separated by space')
a, b = input().split()
a = int(a)
b = float(b)
lst = skip_list(a, b)
print('Enter the number of elements to input in the skip list')
n = int(input())
print('Enter the elements to input in the skip list')
for i in range(n):
    lst.insert_element(int(input()))
lst.displayList()
print('Enter the element to search in the skip list')
lst.search_element(int(input()))
print('Enter the element to delete in the skip list')
lst.delete_element(int(input()))
lst.displayList()