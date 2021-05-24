from random import randint

class Hash:
    def __init__(self):        
        self.a = randint(0,100)
        print(self.a)
        self.lentable = 7
        self.table = [[] for _ in range(self.lentable)]
        
    def insert(self, key, value):
        index = self.hashing(key)
        self.table[index].append(value)

    def hashing(self, key):
        if isinstance(key, (float, int)):
            return (key*self.a)%self.lentable
        else:
            keyint = int(''.join(format(ord(i)) for i in key))
            return (keyint*self.a)%self.lentable
        
    def delete(self, key, value):
        index = self.hashing(key)
        self.table[index].remove(value)
        
    def display_hash(self):
      
        for i in range(self.lentable):
            print(i, end = " ")
              
            for j in self.table[i]:
                print("-->", end = " ")
                print(j, end = " ")
                  
            print()