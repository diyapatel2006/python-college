#create a function which will return true if the number is divisible by 10 otherwise false
def divby10(n):
    return True if n%10==0 else False
lst=[5,56,10,90,1010]
print(list(filter(divby10,lst)))
print(list(filter(lambda x:True if x%10==0 else False,lst)))
print(list(filter(lambda x:x%10==0,[5,56,10,90,1010])))
