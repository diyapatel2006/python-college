import random
s={random.randint(15,45)for num in range(11)}

a={num for num in s if num<30}
print(a)

b={num for num in s if num>30}
print(b)

print(s^b)
