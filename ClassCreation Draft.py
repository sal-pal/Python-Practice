"""Practice for creating classes"""

class Ph():
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.x = 5
        self.y = 7  
        self.n = 'new class'

    def Sal(self,call):
        call = call * self.y
        return call


Tu = Ph('sal',100)




class Weather(Ph):
    def __init__(self):
        self.rain = "rain"
        self.sun = "sun"

    def checkWeather(self,condition):
        """Checks whether the conditions mean rain or sunshine. Enter 'wet' for rain and 'sunshine' for sun"""
        if condition == "wet":
            print self.rain
        elif condition == "sunshine":
            print self.sun
        else:
            print "Need to enter whether there is sunshine or wet"






    
   
