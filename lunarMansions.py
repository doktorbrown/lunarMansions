'''
Created on Feb 1, 2019

@author: catawbafellini
'''

'''
Created on Nov 22, 2018 

@author: catawbafellini
'''
# import datetime
import pyastro
#02/22/2019 modified with updated JPL keplerian elements from https://ssd.jpl.nasa.gov/txt/p_elem_t2.txt
#pip install pyastro
import time 
import datetime
import ephem
# https://rhodesmill.org/pyephem/  pip install ephem
from astral import Astral
import Tkinter as tk 
from Tkinter import *
import datetime

# root = Tk() 
# 
# lab = Label(root)
# lab.pack()


 
# https://github.com/sffjunkie/astral   pip install astral
# import swisseph as swe
# from Planetaries import Hours
root = tk.Tk()
canvas = tk.Canvas(root, width=1900, height=1000, borderwidth=0, highlightthickness=0, bg="#d3d3d3")
canvas.grid()


city_name = 'Spruce Creek'
# city_name = 'Chicago'

# print time.time()
# print time.time()+3600
yester= time.localtime(time.time()-86400)
# print time.localtime(time.time())
morrow= time.localtime(time.time()+86400)

def timeUpdate():
    return time.asctime( time.localtime(time.time()) )


localtime = timeUpdate()
print localtime

todayDate=datetime.date.today()
# print todayDate


dayOfWeek = todayDate.weekday()
yesterDayOfWeek = dayOfWeek -1
# print yesterDayOfWeek

if yesterDayOfWeek == 0:
    yesterDaysDay = "Monday       Moon"
elif yesterDayOfWeek == 1:
    yesterDaysDay = "Tuesday      Mars"
elif yesterDayOfWeek == 2:
    yesterDaysDay = "Wednesday    Mercury"
elif yesterDayOfWeek == 3:
    yesterDaysDay = "Thursday     Jupiter"
elif yesterDayOfWeek == 4:
    yesterDaysDay = "Friday       Venus"
elif yesterDayOfWeek == 5:
    yesterDaysDay = "Saturday     Saturn"
else:
    yesterDaysDay = "Sunday       Sun"
    
# print yesterDaysDay


# print dayOfWeek

if dayOfWeek == 0:
    todaysDay = "Monday       Moon"
elif dayOfWeek == 1:
    todaysDay = "Tuesday      Mars"
elif dayOfWeek == 2:
    todaysDay = "Wednesday    Mercury"
elif dayOfWeek == 3:
    todaysDay = "Thursday     Jupiter"
elif dayOfWeek == 4:
    todaysDay = "Friday       Venus"
elif dayOfWeek == 5:
    todaysDay = "Saturday     Saturn"
else:
    todaysDay = "Sunday       Sun"
    
# print todaysDay
    
dateE=str(todayDate)
# print dateE
# print todayDate + 1
# print todayDate - 1
dateSplit=dateE.split("-")
# print(dateSplit)
year = int(dateSplit[0])
# print(year)
month = int(dateSplit[1])
# print(month)
day = int(dateSplit[2])
# print(day)
# print(datetime.date.today())
# print(time.time()) 

sunTime =(year, month, day+29.53059)

m = ephem.Sun(sunTime)
# print m
sunConstellation = (ephem.constellation(m))
sunLoc = m.ra, m.dec
# print "sunLoc",sunLoc



a = Astral()
a.solar_depression = 'civil'

city = a[city_name]

# print('Information for %s/%s' % (city_name, city.region))
# Information for London/England

timezone = city.timezone
# print('Timezone: %s' % timezone)
# Timezone: Europe/London

# print('Latitude: %.02f; Longitude: %.02f' % (city.latitude, city.longitude))
# Latitude: 51.60; Longitude: 0.08
# print "Local current time :", localtime
now = localtime.split(" ")
# print now
# print now[4], "now"
hms = now[3]
# print hms

hour = int(hms.split(":")[0])
# print "hour",hour
minute = int(hms.split(":")[1])
# print "minute", minute
second = int(hms.split(":")[2])
# print second

# print "Sun is in",sunConstellation[1]
sun = city.sun(date=datetime.date(year, month, day), local=True)
# print('Dawn:    %s' % str(sun['dawn']))
# print('Sunrise: %s' % str(sun['sunrise']))
# print('Noon:    %s' % str(sun['noon']))
# print('Sunset:  %s' % str(sun['sunset']))
# print('Dusk:    %s' % str(sun['dusk']))

# print(sun)
sunRise = (sun['sunrise'])
# print sunRise, "sunRise"
sunSet = (sun['sunset'])
# print sunSet, "sunSet"
dayTime = sunSet - sunRise
# print dayTime, "dayTime"

sunTomorrow = city.sun(date=datetime.date(morrow[0],morrow[1],morrow[2]), local=True)
nextSunrise = sunTomorrow['sunrise']

sunYesterday = city.sun(date=datetime.date(yester[0],yester[1],yester[2]), local=True)
lastSunSet = sunYesterday['sunset']
lastSunrise = sunYesterday['sunrise']

# print lastSunrise, "lastSunrise"
# print lastSunset, "lastSunset"
lastDayTime = lastSunSet - lastSunrise
lastNightTime = sunRise - lastSunSet


# print nextSunrise, "nextSunrise"
nightTime = nextSunrise - sunSet

# print lastNightTime, "lastNightTime"
# print nightTime, "nightTime"

# print lastDayTime, "lastDayTime"
# print(dayTime), "daytime"

planetaryHourDayLength = (dayTime/12)

lastPlanetaryHourDayLength = (lastDayTime/12)
# print lastPlanetaryHourDayLength, "lastPlanetaryHourDayLength"

planetaryHourNightLength = (nightTime/12)
lastPlanetaryHourNightLength = (lastNightTime/12)



def moonCheck(a, year, month, day):
    moon_phase = a.moon_phase(date=datetime.date(year, month, day))
    
    moonPercent = moon_phase/29.53059
#     print(moon_phase), "Moon Phase", moonPercent
    return moon_phase, "Moon Phase", moonPercent
moonTime = (year, month, day+29.53059)
mc = ephem.Moon(moonTime)

moonConstellation = (ephem.constellation(mc))
moonLoc = (mc.ra, mc.dec)
# print moonLoc
# print moonConstellation
# print "Moon is in",moonConstellation[1]
# print moonCheck(a, year, month, day)

class Hours:
        
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
        if tc >= hourOne.strftime("%j:%H:%M")[3] and tc <= hourTwo.strftime("%j:%H:%M"):
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


def yesterHours(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime): 
    h = Hours() 
    # print h 
    
    # Previous day so we can show from 00:00 to sunrise
    pI = h.hourOne(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pII = h.hourTwo(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIII = h.hourThree(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIV = h.hourFour(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pV = h.hourFive(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVI = h.hourSix(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVII = h.hourSeven(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVIII = h.hourEight(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIX = h.hourNine(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pX = h.hourTen(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pXI = h.hourEleven(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pXII = h.hourTwelve(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    print " "
    print "lastPlanetaryHourNightLength:", lastPlanetaryHourNightLength, localtime
    print " "
    print pI[1],pI[2].strftime("%H:%M"),pI[3].strftime("%H:%M"),pI[4],pI[5]
    print pII[1],pII[2].strftime("%H:%M"),pII[3].strftime("%H:%M"),pII[4],pII[5]
    print pIII[1],pIII[2].strftime("%H:%M"),pIII[3].strftime("%H:%M"),pIII[4],pIII[5]
    print pIV[1],pIV[2].strftime("%H:%M"),pIV[3].strftime("%H:%M"),pIV[4],pIV[5]
    print pV[1],pV[2].strftime("%H:%M"),pV[3].strftime("%H:%M"),pV[4],pV[5]
    print pVI[1],pVI[2].strftime("%H:%M"),pVI[3].strftime("%H:%M"),pVI[4],pVI[5]
    print pVII[1],pVII[2].strftime("%H:%M"),pVII[3].strftime("%H:%M"),pVII[4],pVII[5]
    print pVIII[1],pVIII[2].strftime("%H:%M"),pVIII[3].strftime("%H:%M"),pVIII[4],pVIII[5]
    print pIX[1],pIX[2].strftime("%H:%M"),pIX[3].strftime("%H:%M"),pIX[4],pIX[5]
    print pX[1],pX[2].strftime("%H:%M"),pX[3].strftime("%H:%M"),pX[4],pX[5]
    print pXI[1],pXI[2].strftime("%H:%M"),pXI[3].strftime("%H:%M"),pXI[4],pXI[5]
    print pXII[1],pXII[2].strftime("%H:%M"),pXII[3].strftime("%H:%M"),pXII[4],pXII[5]
    print" "
    return


def todayHours(sunRise, planetaryHourDayLength, todaysDay, localtime):
    h = Hours() 
    dI = h.hourOne(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dII = h.hourTwo(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIII = h.hourThree(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIV = h.hourFour(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dV = h.hourFive(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVI = h.hourSix(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVII = h.hourSeven(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVIII = h.hourEight(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIX = h.hourNine(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dX = h.hourTen(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dXI = h.hourEleven(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dXII = h.hourTwelve(sunRise, planetaryHourDayLength, todaysDay, localtime)
    
    print "planetaryHourDayLength:", planetaryHourDayLength, localtime
    print " "
    print dI[0],dI[2].strftime("%H:%M"),dI[3].strftime("%H:%M"),dI[4],dI[5]
    print dII[0],dII[2].strftime("%H:%M"),dII[3].strftime("%H:%M"),dII[4],dII[5]
    print dIII[0],dIII[2].strftime("%H:%M"),dIII[3].strftime("%H:%M"),dIII[4],dIII[5]
    print dIV[0],dIV[2].strftime("%H:%M"),dIV[3].strftime("%H:%M"),dIV[4],dIV[5]
    print dV[0],dV[2].strftime("%H:%M"),dV[3].strftime("%H:%M"),dV[4],dV[5]
    print dVI[0],dVI[2].strftime("%H:%M"),dVI[3].strftime("%H:%M"),dVI[4],dVI[5]
    print dVII[0],dVII[2].strftime("%H:%M"),dVII[3].strftime("%H:%M"),dVII[4],dVII[5]
    print dVIII[0],dVIII[2].strftime("%H:%M"),dVIII[3].strftime("%H:%M"),dVIII[4],dVIII[5]
    print dIX[0],dIX[2].strftime("%H:%M"),dIX[3].strftime("%H:%M"),dIX[4],dIX[5]
    print dX[0],dX[2].strftime("%H:%M"),dX[3].strftime("%H:%M"),dX[4],dX[5]
    print dXI[0],dXI[2].strftime("%H:%M"),dXI[3].strftime("%H:%M"),dXI[4],dXI[5]
    print dXII[0],dXII[2].strftime("%H:%M"),dXII[3].strftime("%H:%M"),dXII[4],dXII[5]
    
    print " "
    return

def toniteHours(sunSet, planetaryHourNightLength, todaysDay, localtime):
    h=Hours()
    I = h.hourOne(sunSet, planetaryHourNightLength, todaysDay, localtime)
    II = h.hourTwo(sunSet, planetaryHourNightLength, todaysDay, localtime)
    III = h.hourThree(sunSet, planetaryHourNightLength, todaysDay, localtime)
    IV = h.hourFour(sunSet, planetaryHourNightLength, todaysDay, localtime)
    V = h.hourFive(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VI = h.hourSix(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VII = h.hourSeven(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VIII = h.hourEight(sunSet, planetaryHourNightLength, todaysDay, localtime)
    IX = h.hourNine(sunSet, planetaryHourNightLength, todaysDay, localtime)
    X = h.hourTen(sunSet, planetaryHourNightLength, todaysDay, localtime)
    XI = h.hourEleven(sunSet, planetaryHourNightLength, todaysDay, localtime)
    XII = h.hourTwelve(sunSet, planetaryHourNightLength, todaysDay, localtime)
    
    print "planetaryHourNightLength:", planetaryHourNightLength, localtime 
    print " "
    print I[1],I[2].strftime("%H:%M"),I[3].strftime("%H:%M"),I[4],I[5]
    print II[1],II[2].strftime("%H:%M"),II[3].strftime("%H:%M"),II[4],II[5]
    print III[1],III[2].strftime("%H:%M"),III[3].strftime("%H:%M"),III[4],III[5]
    print IV[1],IV[2].strftime("%H:%M"),IV[3].strftime("%H:%M"),IV[4],IV[5]
    print V[1],V[2].strftime("%H:%M"),V[3].strftime("%H:%M"),V[4],V[5]
    print VI[1],VI[2].strftime("%H:%M"),VI[3].strftime("%H:%M"),VI[4],VI[5]
    print VII[1],VII[2].strftime("%H:%M"),VII[3].strftime("%H:%M"),VII[4],VII[5]
    print VIII[1],VIII[2].strftime("%H:%M"),VIII[3].strftime("%H:%M"),VIII[4],VIII[5]
    print IX[1],IX[2].strftime("%H:%M"),IX[3].strftime("%H:%M"),IX[4],IX[5]
    print X[1],X[2].strftime("%H:%M"),X[3].strftime("%H:%M"),X[4],X[5]
    print XI[1],XI[2].strftime("%H:%M"),XI[3].strftime("%H:%M"),XI[4],XI[5]
    print XII[1],XII[2].strftime("%H:%M"),XII[3].strftime("%H:%M"),XII[4],XII[5]
    return

def sunDegree(sunRise, planetaryHourDayLength):
    h=Hours()
    I = h.hourOne(sunRise, planetaryHourDayLength, todaysDay, localtime)
#     print I[0],I[2].strftime("%H:%M"),I[3].strftime("%H:%M"),I[4],I[5]
    dayStart = (int(I[2].strftime("%H") )/12.0) + (int(I[2].strftime("%M"))/60.0)
#     dayStart =  (int(I[2].strftime("%M"))/60.0)
    print 360.0/dayStart
    
    return 360.0/dayStart

def pHourDegree(planetaryHourDayLength):
#     (int(planetaryHourDayLength.strftime("%H") )/24.0)
    phd = str(planetaryHourDayLength)
    h = 30.0 * int(phd.split(":")[0]) 
    m = int(phd.split(":")[1]) / 60.0
#     s = float(phd.split(":")[2]) / 3600.0
    degree =  30.0 * (h + m )
    return degree

def pNightDegree(planetaryHourNightLength):
#     print planetaryHourNightLength, "phnl"
    phd = str(planetaryHourNightLength)
    h = 30.0*int(phd.split(":")[0])
#     print "hhhhhh", h
#     h = 24-h 
    m = int(phd.split(":")[1]) / 60.0
#     s = float(phd.split(":")[2]) / 3600.0
    degree =  (h + m )
    return degree


def clockPosition(time):
#     print time
    print dayTime
    t = time.split(":")
#     print t
    h = int(t[0])
#     print h
    m = int(t[1])
#     print m
    hDegree = -(360.0/12.0)*h
    
#     hDegree = (24.0/h)*3-60
    hMinute = 30*-(float(m/60.0))
    print "timey wimey"
    print h, hDegree
    print m, hMinute
    position = (hDegree - hMinute) -55
    print "position", position 
    return position

def clockPositionNight(time):
#     print time
    print nightTime
    t = time.split(":")
#     print t
    h = int(t[0])
#     print h
    m = int(t[1])
#     print m
    hDegree = -(360.0/24.0)*h
    
#     hDegree = (24.0/h)*3-60
    hMinute = 30*(float(m/60.0))
    print "timey wimey"
    print h, hDegree
    print m, hMinute
    position = (hDegree + hMinute) -300
    print "position", position 
    return position



def zodiacDegree(planetPosition):

    planetPositionString = str(planetPosition)

    positionChrA = planetPositionString[0] + planetPositionString[1]
    positionChrB = planetPositionString[2] + planetPositionString[3]
    positionChrC = planetPositionString[4] + planetPositionString[5]
    zodDegPos= int(positionChrA)
    
    if str(positionChrB) == "AR":
        zodSignDegree = 0
    elif str(positionChrB) == "TA":
        zodSignDegree = 30
    elif str(positionChrB) == "GM":
        zodSignDegree = 60
    elif str(positionChrB) == "CN":
        zodSignDegree = 90
    elif str(positionChrB) == "LE":
        zodSignDegree = 120
    elif str(positionChrB) == "VI":
        zodSignDegree = 150
    elif str(positionChrB) == "LI":
        zodSignDegree = 180
    elif str(positionChrB) == "SC":
        zodSignDegree = 210
    elif str(positionChrB) == "SG":
        zodSignDegree = 240
    elif str(positionChrB) == "CP":
        zodSignDegree = 270
    elif str(positionChrB) == "AQ":
        zodSignDegree = 300
    else:
        zodSignDegree = 330
    zodMinPos =  float(positionChrC)/60
    zD = zodDegPos + zodMinPos + zodSignDegree
    return zD
    

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc

def planetaryColor(planet):
    if planet == "Saturn":
        color ="#8A2BE2"
    elif planet =="Jupiter":
        color ="#EE82EE"
    elif planet =="Mars":
        color = "#FF0000"
    elif planet =="Sun":
        color = "#FFA500"
    elif planet =="Venus":
        color = "#008000"
    elif planet =="Mercury":
        color = "#FFFF00"

    else:
        color = "#c0c0c0"
    return color

def App():
    h = Hours() 
    
    #offset 90 moves Aries 0 to 12 o'clock  position
#     offSet = 0
    offSet = 90
    offsetB = -270
#     offSet = 180
    correctionFactorA = 1.3

#     yesterHours(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
#     todayHours(sunRise, planetaryHourDayLength, todaysDay, localtime)
#     toniteHours(sunSet, planetaryHourNightLength, todaysDay, localtime)
#

    pI = h.hourOne(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pII = h.hourTwo(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIII = h.hourThree(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIV = h.hourFour(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pV = h.hourFive(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVI = h.hourSix(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVII = h.hourSeven(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVIII = h.hourEight(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIX = h.hourNine(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pX = h.hourTen(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pXI = h.hourEleven(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pXII = h.hourTwelve(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
         
    dI = h.hourOne(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dII = h.hourTwo(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIII = h.hourThree(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIV = h.hourFour(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dV = h.hourFive(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVI = h.hourSix(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVII = h.hourSeven(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVIII = h.hourEight(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIX = h.hourNine(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dX = h.hourTen(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dXI = h.hourEleven(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dXII = h.hourTwelve(sunRise, planetaryHourDayLength, todaysDay, localtime) 
       

    I = h.hourOne(sunSet, planetaryHourNightLength, todaysDay, localtime)
    II = h.hourTwo(sunSet, planetaryHourNightLength, todaysDay, localtime)
    III = h.hourThree(sunSet, planetaryHourNightLength, todaysDay, localtime)
    IV = h.hourFour(sunSet, planetaryHourNightLength, todaysDay, localtime)
    V = h.hourFive(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VI = h.hourSix(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VII = h.hourSeven(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VIII = h.hourEight(sunSet, planetaryHourNightLength, todaysDay, localtime)
    IX = h.hourNine(sunSet, planetaryHourNightLength, todaysDay, localtime)
    X = h.hourTen(sunSet, planetaryHourNightLength, todaysDay, localtime)
    XI = h.hourEleven(sunSet, planetaryHourNightLength, todaysDay, localtime)
    XII = h.hourTwelve(sunSet, planetaryHourNightLength, todaysDay, localtime)
    
    print I[1],I[2].strftime("%H:%M"),I[3].strftime("%H:%M")
    print II[1],II[2].strftime("%H:%M"),II[3].strftime("%H:%M"),II[4],II[5]
    print III[1],III[2].strftime("%H:%M"),III[3].strftime("%H:%M"),III[4],III[5]
    print IV[1],IV[2].strftime("%H:%M"),IV[3].strftime("%H:%M"),IV[4],IV[5]
    print V[1],V[2].strftime("%H:%M"),V[3].strftime("%H:%M"),V[4],V[5]
    print VI[1],VI[2].strftime("%H:%M"),VI[3].strftime("%H:%M"),VI[4],VI[5]
    print VII[1],VII[2].strftime("%H:%M"),VII[3].strftime("%H:%M"),VII[4],VII[5]
    print VIII[1],VIII[2].strftime("%H:%M"),VIII[3].strftime("%H:%M"),VIII[4],VIII[5]
    print IX[1],IX[2].strftime("%H:%M"),IX[3].strftime("%H:%M"),IX[4],IX[5]
    print X[1],X[2].strftime("%H:%M"),X[3].strftime("%H:%M"),X[4],X[5]
    print XI[1],XI[2].strftime("%H:%M"),XI[3].strftime("%H:%M"),XI[4],XI[5]
    print XII[1],XII[2].strftime("%H:%M"),XII[3].strftime("%H:%M"),XII[4],XII[5]
    
    print planetaryColor(I[1])
    
    print  planetaryHourDayLength
    print (sunRise)
    print sunSet
    print sunDegree(sunRise, planetaryHourDayLength), "sunDegree"
    sunUp = (offSet+42) - sunDegree(sunRise, planetaryHourDayLength)
#     print sunUp, "sunUp"
#     print clockPosition(dI[2].strftime("%H:%M"))
#     print "start", clockPosition(dI[2].strftime("%H:%M"))+offSet 
#     print "end", clockPosition(dI[3].strftime("%H:%M"))+offSet
    sunUpPlus = pHourDegree(planetaryHourDayLength)
    print sunUpPlus, "sunUpPlus"
#     sunDown = (offSet/2) - sunDegree(sunSet, planetaryHourNightLength)
    sunDown = (-sunDegree(sunSet, planetaryHourNightLength)-(3*offSet) )-24.5-0.010409712
   
    print pHourDegree(planetaryHourDayLength), "pHourDegree"
    print pNightDegree(planetaryHourNightLength) , "pNightDegree"

    sunDownPlus = pNightDegree(planetaryHourNightLength)
#     print sunDown, "sunDown"
#     print sunDownPlus , "sunDownPlus"
#     print (sunDownPlus - sunDown )
    
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
#     print time, "this is the mofo"
    hour = int(datetime.datetime.now().strftime("%H"))
    minute = int(datetime.datetime.now().strftime("%M"))
    second = int(datetime.datetime.now().strftime("%S"))
    #positions

    dtime = datetime.datetime(year, month, day, hour, minute, second, 0, pyastro.UTC())
    # print year
    # print month
    # print day
    # print hour 
    # print minute
#     print dtime, "dtime now"
    mon = pyastro.Moon(dtime)
    mer = pyastro.Mercury(dtime)
    ven = pyastro.Venus(dtime)
    sol = pyastro.Sun(dtime)
    mar = pyastro.Mars(dtime)
    jup = pyastro.Jupiter(dtime)
    sat = pyastro.Saturn(dtime)
    nep = pyastro.Neptune(dtime)
    ura = pyastro.Uranus(dtime)
    plu = pyastro.Pluto(dtime)
    
    
    monrasc = (mon.right_ascension(formatted=False))
    # ms=mon.rec_to_sph()
    merrasc = (mer.right_ascension(formatted=False))
    venrasc = (ven.right_ascension(formatted=False))
    solrasc = (sol.right_ascension(formatted=False))
    marrasc = (mar.right_ascension(formatted=False))
    juprasc = (jup.right_ascension(formatted=False))
    satrasc = (sat.right_ascension(formatted=False))
    neprasc = (nep.right_ascension(formatted=False))
    urarasc = (ura.right_ascension(formatted=False))
    plurasc = (plu.right_ascension(formatted=False))
    
    
    moonPosition = pyastro.rasc_to_zodiac(monrasc)
    mercuryPosition = pyastro.rasc_to_zodiac(merrasc)
    venusPosition = pyastro.rasc_to_zodiac(venrasc)
    solPosition = pyastro.rasc_to_zodiac(solrasc)
    marsPosition = pyastro.rasc_to_zodiac(marrasc)
    jupiterPosition = pyastro.rasc_to_zodiac(juprasc)
    saturnPosition = pyastro.rasc_to_zodiac(satrasc)
    neptunePosition = pyastro.rasc_to_zodiac(neprasc)
    uranusPosition = pyastro.rasc_to_zodiac(urarasc)
    plutoPosition = pyastro.rasc_to_zodiac(plurasc)
    
    
    # print "Moon:    ",moonPosition 
    # print "Mercury: ",mercuryPosition
    # print "Venus:   ",venusPosition 
    # print "Sun:     ",solPosition 
    # print "Mars:    ",marsPosition
    # print "Jupiter: ",jupiterPosition
    # print "Saturn:  ",saturnPosition
    # print "Neptune: ",neptunePosition
    # print "Uranus:  ",uranusPosition 
    # print "Pluto:   ",plutoPosition 
    
    moPo = zodiacDegree(moonPosition)
    mePo = zodiacDegree(mercuryPosition)
    vePo = zodiacDegree(venusPosition)
    soPo = zodiacDegree(solPosition)
    maPo = zodiacDegree(marsPosition)
    juPo = zodiacDegree(jupiterPosition)
    saPo = zodiacDegree(saturnPosition)
    nePo = zodiacDegree(neptunePosition)
    urPo = zodiacDegree(uranusPosition)
    plPo = zodiacDegree(plutoPosition)
    #invert for clockwise rotation
    
#     print hour, minute
    hourLargeDegree = -((360/12)*hour)
#     print hourLargeDegree, "hourLargeDegree"
#     print minute
    
    hourSmallDegree = float(minute/60.0)*-30.0
#     print hourSmallDegree, "hourSmallDegree"
    #     hourHand = -((360/12)*hour)+(-30*(minute/60))
    hourHand = hourLargeDegree + hourSmallDegree
    
#     print "hourHand", hourHand
    minuteHand = -((360/60)*minute) + (float(second/60.0)*-6.0)
    secondHand = -((360/60)*second)
    
 

#outer clock rim
    canvas.create_circle(950, 500, 495, fill="white", outline="#000000", width=5)
    
#  minute tick  
    for m in range(0,360,6): 
        
        canvas.create_circle_arc(950, 500, 473, fill="#0000FF", outline="#000000", start=m-1, end=m)
#         m=m+6
#         print (m)
 
#  hour tick  
    for m in range(0,360,30): 
        
        canvas.create_circle_arc(950, 500, 490, fill="#000000", outline="#000000", start=m-1, end=m)
#         m=m+6
#         print (m)
   
#precessed lunar mansions
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=0+33+offSet, end=12+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=12+33+offSet, end=25+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=25+33+offSet, end=38.5+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=38.5+33+offSet, end=52+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=52+33+offSet, end=64+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=64+33+offSet, end=77.5+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=77.5+33+offSet, end=90+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=90+33+offSet, end=102+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=102+33+offSet, end=115+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=115+33+offSet, end=128.5+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=128.5+33+offSet, end=142+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=142+33+offSet, end=154+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=154+33+offSet, end=167.5+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=167.5+33+offSet, end=180+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=180+33+offSet, end=192+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=192+33+offSet, end=205+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=205+33+offSet, end=218.5+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=218.5+33+offSet, end=232+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=232+33+offSet, end=244+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=244+33+offSet, end=257.5+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=257.5+33+offSet, end=270+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=270+33+offSet, end=282+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=282+33+offSet, end=295+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=295+33+offSet, end=308.5+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=308.5+33+offSet, end=322+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=322+33+offSet, end=334+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="#696969", outline="#dcdcdc", start=334+33+offSet, end=347.5+33+offSet)
    canvas.create_circle_arc(950, 500, 450, fill="white", outline="#dcdcdc", start=347.5+33+offSet, end=360+33+offSet)
     
#     
# #traditional lunar mansions
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=0+offSet, end=12+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=12+offSet, end=25+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=25+offSet, end=38.5+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=38.5+offSet, end=52+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=52+offSet, end=64+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=64+offSet, end=77.5+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=77.5+offSet, end=90+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=90+offSet, end=102+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=102+offSet, end=115+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=115+offSet, end=128.5+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=128.5+offSet, end=142+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=142+offSet, end=154+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=154+offSet, end=167.5+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=167.5+offSet, end=180+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=180+offSet, end=192+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=192+offSet, end=205+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=205+offSet, end=218.5+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=218.5+offSet, end=232+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=232+offSet, end=244+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=244+offSet, end=257.5+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=257.5+offSet, end=270+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=270+offSet, end=282+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=282+offSet, end=295+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=295+offSet, end=308.5+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=308.5+offSet, end=322+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=322+offSet, end=334+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#696969", outline="#dcdcdc", start=334+offSet, end=347.5+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=347.5+offSet, end=360+offSet)
   
#planetary clock hands bottom layer 

    canvas.create_circle_arc(950, 500, 475, fill="#8b0000", outline="", start=plPo-1+offSet, end=plPo+offSet)
    canvas.create_circle_arc(950, 500, 475, fill="#006400", outline="", start=urPo-1+offSet, end=urPo+offSet)
    canvas.create_circle_arc(950, 500, 475, fill="blue", outline="", start=nePo-1+offSet, end=nePo+offSet)
    canvas.create_circle_arc(950, 500, 475, fill="#8A2BE2", outline="", start=saPo-1+offSet, end=saPo+offSet)
    canvas.create_circle_arc(950, 500, 475, fill="#EE82EE", outline="", start=juPo-1+offSet, end=juPo+offSet)
    canvas.create_circle_arc(950, 500, 475, fill="#FF0000", outline="", start=maPo-1+offSet, end=maPo+offSet)
    canvas.create_circle_arc(950, 500, 475, fill="#FFA500", outline="", start=soPo-1+offSet, end=soPo+offSet)
    canvas.create_circle_arc(950, 500, 475, fill="#008000", outline="", start=vePo-1+offSet, end=vePo+offSet)
    canvas.create_circle_arc(950, 500, 475, fill="#FFFF00", outline="", start=mePo-1+offSet, end=mePo+offSet)     
    canvas.create_circle_arc(950, 500, 475, fill="#c0c0c0", outline="", start=moPo-1+offSet, end=moPo+offSet)

    
    
    
    #backround cover
    canvas.create_circle(950, 500, 275, fill="white", outline="white", width=10)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=moPo-5+offSet, end=moPo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=mePo-5+offSet, end=mePo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=vePo-5+offSet, end=vePo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=soPo-5+offSet, end=soPo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=maPo-5+offSet, end=maPo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=juPo-5+offSet, end=juPo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=saPo-5+offSet, end=saPo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=nePo-5+offSet, end=nePo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=urPo-5+offSet, end=urPo+offSet)
    canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=plPo-5+offSet, end=plPo+offSet)

    #seasonzodiac boundaries
     
    canvas.create_circle_arc(950, 500, 390, fill="#191970", outline="#000000", start=0+offSet, end=90+offSet)
    canvas.create_circle_arc(950, 500, 390, fill="#FF0000", outline="#000000", start=90+offSet, end=1800+offSet)
    canvas.create_circle_arc(950, 500, 390, fill="#808000", outline="#000000", start=180+offSet, end=270+offSet)
    canvas.create_circle_arc(950, 500, 390, fill="#FFFF00", outline="#000000", start=270+offSet, end=360+offSet)
     
    #zodiac boundaries
     
    canvas.create_circle_arc(950, 500, 370, fill="#FF0000", outline="#000000", start=0+offSet, end=30+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#808000", outline="#000000", start=30+offSet, end=60+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#FFFF00", outline="#000000", start=60+offSet, end=90+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#191970", outline="#000000", start=90+offSet, end=120+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#FF0000", outline="#000000", start=120+offSet, end=150+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#808000", outline="#000000", start=150+offSet, end=180+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#FFFF00", outline="#000000", start=180+offSet, end=210+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#191970", outline="#000000", start=210+offSet, end=240+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#FF0000", outline="#000000", start=240+offSet, end=270+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#808000", outline="#000000", start=270+offSet, end=300+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#FFFF00", outline="#000000", start=300+offSet, end=330+offSet)
    canvas.create_circle_arc(950, 500, 370, fill="#191970", outline="#000000", start=330+offSet, end=360+offSet)

#  decan tick  
    for m in range(0,360,10): 
        
        canvas.create_circle_arc(950, 500, 380, fill="#000000", outline="#000000", start=m, end=m)
#         m=m+6
#        print (m)


#previous night hours

    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pI[1]), outline="#000000", start=clockPositionNight(pI[2].strftime("%H:%M"))+offSet, end=clockPositionNight(pI[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pII[1]), outline="#000000", start=clockPosition(pII[2].strftime("%H:%M"))+offSet, end=clockPosition(pII[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIII[1]), outline="#000000", start=clockPosition(pIII[2].strftime("%H:%M"))+offSet, end=clockPosition(pIII[3].strftime("%H:%M"))+offSet) 
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIV[1]), outline="#000000", start=clockPosition(pIV[2].strftime("%H:%M"))+offSet, end=clockPosition(pIV[3].strftime("%H:%M"))+offSet)    
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pV[1]), outline="#000000", start=clockPosition(pV[2].strftime("%H:%M"))+offSet, end=clockPosition(pV[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVI[1]), outline="#000000", start=clockPosition(pVI[2].strftime("%H:%M"))+offSet, end=clockPosition(pVI[3].strftime("%H:%M"))+offSet)
#     canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVII[1]), outline="#000000", start=clockPosition(pVII[2].strftime("%H:%M"))+offSet, end=clockPosition(pVII[3].strftime("%H:%M"))+offSet)
#     canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVIII[1]), outline="#000000", start=clockPosition(pVIII[2].strftime("%H:%M"))+offSet, end=clockPosition(pVIII[3].strftime("%H:%M"))+offSet)
#     canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIX[1]), outline="#000000", start=clockPosition(pIX[2].strftime("%H:%M"))+offSet, end=clockPosition(pIX[3].strftime("%H:%M"))+offSet)
#     canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pX[1]), outline="#000000", start=clockPosition(pX[2].strftime("%H:%M"))+offSet, end=clockPosition(pX[3].strftime("%H:%M"))+offSet)
#     canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pXI[1]), outline="#000000", start=clockPosition(pXI[2].strftime("%H:%M"))+offSet, end=clockPosition(pXI[3].strftime("%H:%M"))+offSet)
#     canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pXII[1]), outline="#000000", start=clockPosition(pXII[2].strftime("%H:%M"))+offSet, end=clockPosition(pXII[3].strftime("%H:%M"))+offSet)


#day hours

    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dI[0]), 
                             outline="#000000", 
                             start= offsetB + clockPosition(dI[2].strftime("%H:%M")), 
                             end=offsetB - sunUpPlus + clockPosition(dI[2].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dII[0]), 
                             outline="#000000", 
                             start=offsetB - sunUpPlus + clockPosition(dI[2].strftime("%H:%M")), 
                             end=offsetB - sunUpPlus  + clockPosition(dII[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dIII[0]), 
                             outline="#000000", 
                             start=offsetB -sunUpPlus  + clockPosition(dII[2].strftime("%H:%M")),
                             end=offsetB - sunUpPlus + clockPosition(dIII[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dIV[0]), 
                             outline="#000000", 
                             start=offsetB -sunUpPlus+ clockPosition(dIII[2].strftime("%H:%M")), 
                             end= offsetB -sunUpPlus + clockPosition(dIV[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dV[0]), 
                             outline="#000000", 
                             start=offsetB -sunUpPlus + clockPosition(dIV[2].strftime("%H:%M")), 
                             end=offsetB -sunUpPlus + clockPosition(dV[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dVI[0]), 
                             outline="#000000", 
                             start=offsetB -sunUpPlus + clockPosition(dV[2].strftime("%H:%M")), 
                             end=offsetB -sunUpPlus + clockPosition(dVI[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dVII[0]), 
                             outline="#000000", 
                             start=offsetB + clockPosition(dVII[2].strftime("%H:%M")), 
                             end=offsetB + clockPosition(dVII[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dVIII[0]), 
                             outline="#000000", 
                             start=offsetB + clockPosition(dVIII[2].strftime("%H:%M")), 
                             end=offsetB + clockPosition(dVIII[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dIX[0]), 
                             outline="#000000", 
                             start=offsetB + clockPosition(dIX[2].strftime("%H:%M")), 
                             end=offsetB + clockPosition(dIX[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, fill=planetaryColor(dX[0]), 
                             outline="#000000", 
                             start=offsetB + clockPosition(dX[2].strftime("%H:%M")), 
                             end=offsetB + clockPosition(dX[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, fill=planetaryColor(dXI[0]), 
                             outline="#000000", 
                             start=offsetB + clockPosition(dXI[2].strftime("%H:%M")), 
                             end=offsetB + clockPosition(dXI[3].strftime("%H:%M")))
    canvas.create_circle_arc(950, 500, 320, fill=planetaryColor(dXII[0]), 
                             outline="#000000", 
                             start=offsetB + clockPosition(dXII[2].strftime("%H:%M")), 
                             end=offsetB + clockPosition(dXII[3].strftime("%H:%M")))
#     print "sunset", ((sunUp)-(12 * sunUpPlus))
    
#night hours

    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(I[1]), 
                             outline="#000000", 
                             start=clockPositionNight(I[2].strftime("%H:%M"))+offSet, 
                             end=clockPositionNight(I[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(II[1]), 
                             outline="#000000", 
                             start=clockPosition(II[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(II[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(III[1]), 
                             outline="#000000", 
                             start=clockPosition(III[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(III[3].strftime("%H:%M"))+offSet) 
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(IV[1]), 
                             outline="#000000", 
                             start=clockPosition(IV[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(IV[3].strftime("%H:%M"))+offSet)    
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(V[1]), 
                             outline="#000000", 
                             start=clockPosition(V[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(V[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(VI[1]), 
                             outline="#000000", 
                             start=clockPosition(VI[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(VI[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(VII[1]), 
                             outline="#000000", 
                             start=clockPosition(VII[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(VII[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(VIII[1]), 
                             outline="#000000", 
                             start=clockPosition(VIII[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(VIII[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(IX[1]), 
                             outline="#000000", 
                             start=clockPosition(IX[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(IX[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(X[1]), 
                             outline="#000000", 
                             start=clockPosition(X[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(X[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(XI[1]), 
                             outline="#000000", 
                             start=clockPosition(XI[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(XI[3].strftime("%H:%M"))+offSet)
    canvas.create_circle_arc(950, 500, 300, 
                             fill=planetaryColor(XII[1]), 
                             outline="#000000", 
                             start=clockPosition(XII[2].strftime("%H:%M"))+offSet, 
                             end=clockPosition(XII[3].strftime("%H:%M"))+offSet)






    
#inner circle    
    canvas.create_circle(950, 500, 270, fill="white", outline="white", width=10)
        
#planetary planet hands top layer
    canvas.create_circle_arc(950, 500, 420, fill="#8b0000", outline="", start=plPo-1+offSet, end=plPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#006400", outline="", start=urPo-1+offSet, end=urPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="blue", outline="", start=nePo-1+offSet, end=nePo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#8A2BE2", outline="", start=saPo-1+offSet, end=saPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#EE82EE", outline="", start=juPo-1+offSet, end=juPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#FF0000", outline="", start=maPo-1+offSet, end=maPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#FFA500", outline="", start=soPo-1+offSet, end=soPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#008000", outline="", start=vePo-1+offSet, end=vePo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#FFFF00", outline="", start=mePo-1+offSet, end=mePo+offSet)    
    canvas.create_circle_arc(950, 500, 420, fill="#c0c0c0", outline="", start=moPo-1+offSet, end=moPo+offSet)

      
#clock

    canvas.create_circle_arc(950, 500, 340, fill="black", outline="", start=(hourHand -5+offSet), end=(hourHand+offSet))
    canvas.create_circle_arc(950, 500, 450, fill="black", outline="", start=(minuteHand -3+offSet), end=(minuteHand+offSet))
    canvas.create_circle_arc(950, 500, 495, fill="black", outline="", start=(secondHand -1+offSet), end=(secondHand+offSet))

    
    

    root.wm_title("astronomical lunar mansion clock")
    root.update_idletasks()
    root.after(1000, App)
    return




App()  
root.update_idletasks()
root.after(1000, App)
root.mainloop() 


#  
# def main():
#     app = App()
#     app.mainloop()
# 
# if __name__ == "__main__":
#     main()
