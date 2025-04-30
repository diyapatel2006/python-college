def create_list(l1,l2):
     s1=set(l1)
     s2=set(l2)
     l=list(s1&s2)
     print("Intersected lists:",l)
create_list(list(input("Enter list 1: ")),list(input("Enter list 2: ")))
