class String:
    def __init__(self,word):
        self.word=word
    def __iadd__(self,other):
        self.word=self.word+other.word
        return self
    def toLower(self):
        w=""
        for letter in self.word:
            
            if(ord(letter)<=90 and ord(letter)>=65):
                ac=ord(letter)+32
                w+=chr(ac)
            else:
                w+=letter
        
        return w
    def toUpper(self):
        w=""
        for letter in self.word:
            if(ord(letter)>=97 and ord(letter)<=123):
                ac=ord(letter)-32
                w+=chr(ac)
            else:
                w+=letter
        return w



s1=String("HELLO")
s2=String("Antarctica")
s1+=s2
print(s1.word)
print(s1.toLower())
print(s2.toUpper())
