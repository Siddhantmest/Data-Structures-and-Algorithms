class docdistance:
    def __init__(self, doc):
        self.doc = doc
    
    def doc2words(self):
        self.wordlist = []
        for line in self.doc:
            word = ''
            for char in line:
                if char.isalnum():
                    word += char
                else:
                    if len(word)>0:
                        word = word.lower()
                        self.wordlist.append(word)
                        word = ''
    
    def wordfreq(self):
        val = 0
        self.wordfreqdict = dict.fromkeys(self.wordlist, val)
        for word in self.wordlist:
            if word in self.wordfreqdict:
                self.wordfreqdict[word] += 1
                
    def dotproduct(self, doc1dict, doc2dict):
        total = 0
        for key in doc1dict:
            if key in doc2dict:
                total += doc1dict[key] * doc2dict[key]
                    
        print("the dot product of 2 documents is ", total )
        
print('Welcome to the algorithm for implementing document distance. Input the path and name of your 1st document', sep = ' ')
doc1 = open(input()).readlines()
print('Input the path and name of your 2nd document', sep = ' ')
doc2 = open(input()).readlines()

dd = docdistance(doc1)
dd.doc2words()
dd.wordfreq()
dd1 = docdistance(doc2)
dd1.doc2words()
dd1.wordfreq()

dd.dotproduct(dd.wordfreqdict, dd1.wordfreqdict)
