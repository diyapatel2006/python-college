# question 1
def count_lower_upper():
    x=input("Enter the string")
    lower = 0
    upper = 0
    for char in x:
        if char.islower():
            lower +=1
        elif char.isupper():
            upper +=1
     return("lowercase letters" ,lower)
     
     return("uppercase letters" ,upper)
            
count_lower_upper()                
