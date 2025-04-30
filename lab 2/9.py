#largest smallest out of three
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
if a>b and b>c:
    print("Largest:",a,"Smallest:",c)
elif a>c and c>b:
    print("Largest:",a,"Smallest:",b)
elif b>c and c>a:
    print("Largest:",b,"Smallest:",a)
elif b>a and a>c:
    print("Largest:",b,"Smallest:",c)
elif c>a and a>b:
    print("Largest:",c,"Smallest:",b)
elif c>b and b>a:
    print("Largest:",c,"Smallest:",a)
