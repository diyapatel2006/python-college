class Matrix:
    def __init__(self,r1,r2,r3):
        self.a=[r1,r2,r3]
       

    def __add__(self,other):
       
        addition=[[],[],[]]
        for i in range(len(self.a[0])):
            addition[0].append(self.a[0][i]+other.a[0][i])
        for i in range(len(self.a[1])):
            addition[1].append(self.a[1][i]+other.a[1][i])
        for i in range(len(self.a[2])):
            addition[2].append(self.a[2][i]+other.a[2][i])
        
        m=Matrix(addition[0],addition[1],addition[2])
        return m
    
    def __mul__(self,other):
        multi=[[0,0,0],[0,0,0],[0,0,0]]
        
        for i in range(3):
            for j in range(3):
                    multi[i][j]+=self.a[i][0]* other.a[0][j]+ self.a[i][1]*other.a[1][j]+ self.a[i][2]*other.a[2][j]
                    

        z=Matrix(multi[0],multi[1],multi[2])
        return z
    
    def transpose(self):
        ans=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                ans[i][j]=self.a[j][i]
        return ans
  
    
M1=Matrix([1,2,3],[0,0,1],[1,1,1])
M2=Matrix([2,2,2],[0,1,1],[0,2,0])
M3=M1+M2
M4=M1*M2
print(M3.a[0],M3.a[1],M3.a[2])
print(M4.a[0],M4.a[1],M4.a[2])
ans=M1.transpose()
print(ans)
