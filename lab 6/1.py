name=[("Diya","jil",),("Saakshi"),("Dhruvi","Hetvi")]

boys_count=0
girls_count=0

for ele in name:
    if isinstance(ele,tuple):
        boys_count +=1
    else:
        girls_count +=1
        
print("Number of boys:",boys_count)
print("Number of girls:",girls_count)
