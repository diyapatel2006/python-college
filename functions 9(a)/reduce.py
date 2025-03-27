#find max of list using reduce
from functools import reduce

r=reduce(lambda p,q:p*q,[x for x in range(1,5)])
print(r)
