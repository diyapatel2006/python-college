#to check whter one string is there in another
def check():
    s1 = input("Enter the first string:")
    s2= input("Enter second string:")
    if (s2 in s1):
        print("Second string is present in first string")
    else:
        print("Second string is not present in first string")
check()
