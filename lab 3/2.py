word2=input("enter a string to convert to lowercase/uppercase/togglecase")
def lowercase(word):
    w=""
    for letter in word:
        if (ord(letter)>=65 and ord(letter)<=90):#captial
            ac=ord(letter)+32
            w+=chr(ac)
        else:
            w+=letter
    return w
def uppercase(word):
    w=""
    for letter in word:
        if (ord(letter)>=97 and ord(letter)<=123):#csmall
            ac=ord(letter)-32
            w+=chr(ac)
        else:
            w+=letter
    return w

def togglecase(word):
    w=""
    for letter in word:
        if (ord(letter)>=65 and ord(letter)<=90):#captial
            ac=ord(letter)+32
            w+=chr(ac)
        elif(ord(letter)>=97 and ord(letter)<=123):#small
            ac2=ord(letter)-32
            w+=chr(ac2)
    return w
        
print('lowercase:',lowercase(word2))
print('uppercase:',uppercase(word2))
print('togglecase:',togglecase(word2))
