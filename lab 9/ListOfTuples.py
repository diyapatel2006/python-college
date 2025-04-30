def l(x):
     lst=[]
     for i in range(1,x+1):
         t=(i,i**2,i**3)
         lst.append(t)
     print(lst)
x=int(input("Enter a number"))
l(x)
