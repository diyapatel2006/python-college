def frequency(s):
     lst = s.split()
     sub = list(set(lst))
     sub.sort()
     for i in sub:
         print(i,lst.count(i))
frequency(input("Enter a string"))
