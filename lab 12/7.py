class Weather:
    def __init__(self,wpara):
        self.parameters=wpara

    def __contains__(self,search):
        if search in self.parameters:
            return True
        else:
            return False
india=Weather(["humidity","precipitation","temperature","windspeed"])
print("rainfall" in india)
print("humidity" in india)
