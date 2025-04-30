#multplication table of a given number
def table(x):
    for n in range(1,11):
        print(x,"*",n,"=",x*n)
x = int(input("Enter a number"))
table(x)
