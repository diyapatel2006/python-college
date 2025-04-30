#n numbers of fibonacci series
def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    while a+b<n:
        c=a+b
        print(c)
        a=b
        b=c
n=int(input("Enter the last number of series"))
fibonacci(n)    
