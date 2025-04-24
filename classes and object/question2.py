# question 2 -> implement matrix class...
class Matrix:
    def __init__(self):
        self.m=[[0,0,0],[0,0,0],[0,0,0]]
        
    def GetMatrixVal(self):
        print("Enter values of [3,3] matrix:")
        for i in range(3):
            for j in range(3):
                self.m[i][j]=int(input())

    def __add__(s,m):
        a=Matrix()
        for i in range(3):
            for j in range(3):
                a.m[i][j] = s.m[i][j] + m.m[i][j]
        return a
                
    def printMatrix(s):
        print(s.m[0][0],s.m[0][1],s.m[0][2],'\n',s.m[1][0],s.m[1][1],s.m[1][2],'\n',s.m[2][0],s.m[2][1],s.m[2][2])

m=Matrix()
m.GetMatrixVal()
m.printMatrix()

n=Matrix()
n.GetMatrixVal()
n.printMatrix()

o=Matrix()
o=m+n
o.printMatrix()
