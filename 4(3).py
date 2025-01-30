#question 3
def count():
    y=0
    x=0
    a=input("Enter a string:")
    for ch in a:
        if ch.isdigit():
            x=x+1
        else:
            ch.isalpha()
            y=y+1
    print(y)
    print(x)

count()
             
