from random import randint

class open_addressing:
    def __init__(self):
        self.a = randint(0,100)
        self.capacity = 8
        self.table = [None]*8
        self.alpha = 1
        self.size = 0
        
    def load_factor(self):
        return self.size/self.capacity
    
    def hashing(self, key):
        if isinstance(key, (float, int)):
            return (key*self.a)%self.capacity
        else:
            keyint = int(''.join(format(ord(i)) for i in key))
            return (keyint*self.a)%self.capacity
    
    def insert(self,key):
        if self.load_factor >= self.alpha:
            self.capacity <<= 1 #doubling the table capacity and assigning it to capacity
            new_table = [None]*self.capacity
            for i in range(self.capacity >> 1):
                if (self.table[i] is not None) and self.table[i] != "Tombstone":
                    hashi = self.hashing(self.table[i])
                    while new_table[hashi] is not None:
                        hashi = (2*hashi+1)%self.capacity
                    new_table[hashi] = self.table[i]
                    
            self.table = new_table
            
        h = self.hashing(key)
        while self.table[h] is not None:
            h = (2*h+1)%self.capacity
            if self.table[h] == "Tombstone":
                break
            
        self.table[h] = key
        self.size += 1
        
    def search(self,key):
        h = self.hashing(key)
        while self.table[h] is not None:
            if self.table[h] == key:
                print(str(key) + ' exists!!')
                return
            h = (2*h+1)%self.capacity
            
        print(str(key) + ' does not exist')
        return
    
    def delete(self,key):
        h = self.hashing(key)
        while self.table[h] is not None:
            if self.table[h] == key:
                self.table[h] = "Tombstone"
                self.size -= 1
            else:
                h = (2*h+1)%self.capacity
            
        #resizing
        if self.load_factor <= self.alpha/4:
            self.capacity >>= 1 #halfing the table capacity and assigning it to capacity
            new_table = [None]*self.capacity
            for i in range(self.capacity << 1):
                if (self.table[i] is not None) and self.table[i] != "Tombstone":
                    hashi = self.hashing(self.table[i])
                    while new_table[hashi] is not None:
                        hashi = (2*hashi+1)%self.capacity
                    new_table[hashi] = self.table[i]
                    
            self.table = new_table