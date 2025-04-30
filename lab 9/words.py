def words(s):
     lst=s.split()
     a=list(set(lst))
     a.sort()
     s = ""
     for i in a:
         s = s+" "+i
     return s
s= input("Enter a string")
print("New sentence is: ",words(s))
