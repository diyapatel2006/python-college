def ispangram(s):
     n = set(s)
     alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
     if alpha.issubset(n):
         return(True)
     else:
         return(False)
print(ispangram("the quick brown fox jumps over the lazy"))
