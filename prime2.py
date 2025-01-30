#question 4
def prime():
    a= int(input("Enter a number:")
           if a==0 or a==1:
           print("Not a prime number")
           elif a==2:
               print("Its a prime number")
           elif a>1:
               for i in range(3,a+1):
                   if(a%i)==0:
                       print("Not a prime number")
                       break
                    else:
                        print("Its a prime number")
                        break
prime()                    
