"""p=lambda n: n**3
q=lambda a,b,c: (a+b+c)/3
r=lambda str : str.trim().upper()
print(p(4))
print(q(10,20,30))
print(r("pDeU"))"""


d={'o':230,'c':150,"s":175,"n":35}
d1=sorted(d.items(), key=lambda kv:kv[1])
print(d1)
