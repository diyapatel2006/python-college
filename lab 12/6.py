class Date:
    def __init__(self,date):
        self.day=date[0]
        self.month=date[1]
        self.year=date[2]
        self.date=date

    def __eq__(self,other):
        if self.date==other.date:
            answer=True
        else:
            answer=False
        return answer
dt=Date([12,2,22])
dt2=Date([14,3,24])
dt3=Date([12,2,22])
print(dt==dt2,dt==dt3,dt3==dt)
