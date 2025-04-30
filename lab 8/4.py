s={"Aashi","Aditya","Bharti","Ali","Bitu","Batuk"}
print(s)

s1={item for item in s if item.startswith('A')}
s2={item for item in s if item.startswith('B')}

print(s1)
print(s2)
