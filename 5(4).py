#1
import random
Lodd=[]
for i in range(1,6):
    x=random.randint(1,100)*2+1
    Lodd.append(x)
print(Lodd)    

    

Even=[]

for x in range(1,5):

    y=random.randint(1,100)*2
    Even.append(y)
    
print(Even)



Lodd.insert(6,Even)
print(Lodd)


    
