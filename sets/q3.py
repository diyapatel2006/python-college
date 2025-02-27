# question 3

def set3():
    s=set()
    while len(s)<5:
        s.add(input("Enter a name"))
    print(s)
    nm=input("Enter a name to modify:")
    if nm in s:
        newnm=input("Enter another name:")
        s.remove(nm)
        s.add(newnm)
    else:
        print(nm,"is missing in the values")
    print("removing 2 names:")
    print(s.pop(),"is removed")
    print(s.pop(),"is removed")
    print("Finally Rahul, this is my set:",s)
set3()    
