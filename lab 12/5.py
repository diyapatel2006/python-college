class Time:
    def __init__(self,h,m,s):
        self.hours=h
        self.minutes=m
        self.seconds=s
    def convert_in_seconds(self):
        time=self.hours*3600+self.minutes*60+self.seconds
        return time
    def speed(self,distance):
        t=self.convert_in_seconds()
        speed=distance/t
        return speed
q=Time(1,1,10)
print(q.speed(10000))
