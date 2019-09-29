'''
Created on Nov 22, 2018 

@author: doktorbrown

Modified on Sep 28, 2019 

@author: doktorbrown

'''

import time


class Hours():
        
    def __init__(self ):
        self.Hours = []
    
    def rulingPlanet(self,sunRise):
        chaldeanOrderDay=("Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn")
        if sunRise.strftime("%A") == "Sunday":
            ruler = chaldeanOrderDay[0]
        elif sunRise.strftime("%A") == "Monday":
            ruler = chaldeanOrderDay[1]
        elif sunRise.strftime("%A") == "Tuesday":
            ruler = chaldeanOrderDay[2]
        elif sunRise.strftime("%A") == "Wednesday":
            ruler = chaldeanOrderDay[3]
        elif sunRise.strftime("%A") == "Thursday":
            ruler = chaldeanOrderDay[4]
        elif sunRise.strftime("%A") == "Friday":
            ruler = chaldeanOrderDay[5]
        else: ruler = chaldeanOrderDay[6]
       
    
        return ruler
    
    def hourlyPlanet(self,rulingPlanet):
        chaldeanOrderDay=("Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn")
        chaldeanOrderHours=("Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars")
        if rulingPlanet == "Sun":
            hourlyPlanetOUT = chaldeanOrderHours[0:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:3]
        elif rulingPlanet == "Moon":
            hourlyPlanetOUT = chaldeanOrderHours[3:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:6]
        elif rulingPlanet == "Mars":
            hourlyPlanetOUT = chaldeanOrderHours[6:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:2]
        elif rulingPlanet == "Mercury":
            hourlyPlanetOUT = chaldeanOrderHours[2:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:-2]
        elif rulingPlanet == "Jupiter":
            hourlyPlanetOUT = chaldeanOrderHours[5:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:1]
        elif rulingPlanet == "Venus":
            hourlyPlanetOUT = chaldeanOrderHours[1:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:-3]
        else: hourlyPlanetOUT = chaldeanOrderHours[4:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours
        
        return hourlyPlanetOUT

            
    def hourOne(self,sunRise,planetaryHourDayLength,todaysDay,localtime):
        hourOne = sunRise + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= sunRise.strftime("%j:%H:%M") and tc <= hourOne.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""     
        return chaldean[0],chaldean[12],sunRise, hourOne, pHour, tcc
    
    def hourTwo(self, sunRise,planetaryHourDayLength,todaysDay,localtime):
        hourOne = self.hourOne(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourTwo = hourOne + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourOne.strftime("%j:%H:%M") and tc <= hourTwo.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""     
        return chaldean[1],chaldean[13],hourOne, hourTwo, pHour, tcc
    
    def hourThree(self, sunRise,planetaryHourDayLength,todaysDay,localtime):
        hourTwo = self.hourTwo(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourThree = hourTwo + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourTwo.strftime("%j:%H:%M") and tc <= hourThree.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""         
        return chaldean[2],chaldean[14],hourTwo, hourThree, pHour, tcc
    
    def hourFour(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourThree = self.hourThree(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourFour = hourThree + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourThree.strftime("%j:%H:%M") and tc <= hourFour.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[3],chaldean[15],hourThree, hourFour, pHour, tcc
    

    def hourFive(self, sunRise,planetaryHourDayLength,todaysDay,localtime):
        hourFour = self.hourFour(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourFive = hourFour + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourFour.strftime("%j:%H:%M") and tc <= hourFive.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False 
            tcc = "" 
        return chaldean[4],chaldean[16],hourFour, hourFive, pHour, tcc
    
    def hourSix(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourFive = self.hourFive(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourSix = hourFive + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourFive.strftime("%j:%H:%M") and tc <= hourSix.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[5],chaldean[17],hourFive, hourSix, pHour, tcc
    
    def hourSeven(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourSix = self.hourSix(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourSeven = hourSix + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourSix.strftime("%j:%H:%M") and tc <= hourSeven.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[6],chaldean[18],hourSix, hourSeven, pHour, tcc
    
    def hourEight(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourSeven = self.hourSeven(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourEight = hourSeven + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourSeven.strftime("%j:%H:%M") and tc <= hourEight.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc 
        else:
            pHour = False
            tcc = ""   
        return chaldean[7],chaldean[19],hourSeven,hourEight, pHour, tcc
       
    def hourNine(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourEight = self.hourEight(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourNine = hourEight + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourEight.strftime("%j:%H:%M") and tc <= hourNine.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc 
        else:
            pHour = False
            tcc = ""   
        return chaldean[8],chaldean[20],hourEight, hourNine, pHour, tcc
    
    def hourTen(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourNine = self.hourNine(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourTen = hourNine + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourNine.strftime("%j:%H:%M") and tc <= hourTen.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[9],chaldean[21], hourNine, hourTen, pHour, tcc
    
    def hourEleven(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourTen = self.hourTen(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourEleven = hourTen + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourTen.strftime("%j:%H:%M") and tc <= hourEleven.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[10],chaldean[22],hourTen, hourEleven, pHour, tcc
    
    def hourTwelve(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourEleven = self.hourEleven(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourTwelve = hourEleven + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourEleven.strftime("%j:%H:%M") and tc <= hourTwelve.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc 
        else:
            pHour = False
            tcc = ""   
        return chaldean[11],chaldean[23],hourEleven, hourTwelve, pHour, tcc

