'''
Created on Feb 1, 2019

@author: catawbafellini

Created on Nov 22, 2018 

@author: catawbafellini

Created on March 6, 2018 

@author: catawbafellini

Created on April 27, 2018

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
import time as chron
import logger

# root = Tk() 
# 
# lab = Label(root)
# lab.pack()


 
# https://github.com/sffjunkie/astral   pip install astral
# import swisseph as swe

# from Planetaries import Hours

log = logger.Logger()

log.logMsg("starting up...")

prev_entry = 0
this_entry = 0

root = tk.Tk()
canvas = tk.Canvas(root, width=1900, height=1000, borderwidth=0, highlightthickness=0, bg="#d3d3d3")
canvas.grid()
root.wm_title("astronomical lunar mansion clock")

#currently this needs to be added to the 


city_name = 'Spruce Creek'
#city_name = 'Chicago'

# #print time.time()
# #print time.time()+3600
julianC = time.localtime(time.time()-(86400*13))
#print "julianC=",julianC
yester= time.localtime(time.time()-86400)
# #print time.localtime(time.time())
morrow= time.localtime(time.time()+86400)

def timeUpdate():
    return time.asctime( time.localtime(time.time()) )


localtime = timeUpdate()
# #print localtime

todayDate=datetime.date.today()
# #print todayDate


dayOfWeek = todayDate.weekday()
yesterDayOfWeek = dayOfWeek -1
# #print yesterDayOfWeek

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
    
# #print yesterDaysDay


# #print dayOfWeek

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
    
# #print todaysDay
    
dateE=str(todayDate)
# #print dateE
# #print todayDate + 1
# #print todayDate - 1
dateSplit=dateE.split("-")
# #print(dateSplit)
year = int(dateSplit[0])
# #print(year)
month = int(dateSplit[1])
# #print(month)
day = int(dateSplit[2])
# #print(day)
# #print(datetime.date.today())
# #print(time.time()) 

sunTime =(year, month, day+30.53059)

m = ephem.Sun(sunTime)
# #print m
sunConstellation = (ephem.constellation(m))
sunLoc = m.ra, m.dec
# #print "sunLoc",sunLoc



a = Astral()
a.geocoder.add_locations([("Spruce Creek","USA",40.646256,-78.090935,"US/Eastern",282)])
a.solar_depression = 'civil'

city = a[city_name]

# #print('Information for %s/%s' % (city_name, city.region))
# Information for London/England

timezone = city.timezone
# #print('Timezone: %s' % timezone)
# Timezone: Europe/London

# #print('Latitude: %.02f; Longitude: %.02f' % (city.latitude, city.longitude))
# Latitude: 51.60; Longitude: 0.08
#print "Local current time :", localtime
now = localtime.split(" ")
#print now

# weird shit happens here....sometimes [3]....sometimes [4]??? single vs. double digit date?
#print (now[4]), "now4"
#print (now[3]), "now3"
#MAYBE THIS FIXES?
if len(now[4])== 4:

    hms = now[3]
else:
    hms = now[4]
    
#print hms ,"hms "

hour = int(hms.split(":")[0])
#print "hour",hour
#print (hms.split(":")[0])
minute = int(hms.split(":")[1]) 
#print "minute", minute
second = int(hms.split(":")[2])
#print second

# #print "Sun is in",sunConstellation[1]
sun = city.sun(date=datetime.date(year, month, day), local=True)
# #print('Dawn:    %s' % str(sun['dawn']))
# #print('Sunrise: %s' % str(sun['sunrise']))
# #print('Noon:    %s' % str(sun['noon']))
# #print('Sunset:  %s' % str(sun['sunset']))
# #print('Dusk:    %s' % str(sun['dusk']))

# #print(sun)
sunRise = (sun['sunrise'])
#print sunRise, "sunRise"
#print sunRise.hour, "sunRise.hour"
#print sunRise.minute, "sunRise.minute"
sunSet = (sun['sunset'])
#print sunSet, "sunSet"
dayTime = sunSet - sunRise
#print dayTime, "dayTime"

sunTomorrow = city.sun(date=datetime.date(morrow[0],morrow[1],morrow[2]), local=True)
#print sunTomorrow, "sunTomorrow"
nextSunrise = sunTomorrow['sunrise']

sunYesterday = city.sun(date=datetime.date(yester[0],yester[1],yester[2]), local=True)
lastSunSet = sunYesterday['sunset']
lastSunrise = sunYesterday['sunrise']

#print lastSunrise, "lastSunrise"
#print lastSunSet, "lastSunset"
lastDayTime = lastSunSet - lastSunrise
lastNightTime = sunRise - lastSunSet


#print nextSunrise, "nextSunrise"
nightTime = nextSunrise - sunSet

#print lastNightTime, "lastNightTime"
#print nightTime, "nightTime"

#print lastDayTime, "lastDayTime"
#print(dayTime), "daytime"

planetaryHourDayLength = (dayTime/12)

lastPlanetaryHourDayLength = (lastDayTime/12)
#print lastPlanetaryHourDayLength, "lastPlanetaryHourDayLength"

planetaryHourNightLength = (nightTime/12)
lastPlanetaryHourNightLength = (lastNightTime/12)
#print nightTime, "nightTime"
#print planetaryHourNightLength, "planetaryHourNightLength"
#print lastPlanetaryHourNightLength, "lastPlanetaryHourNightLength"



def moonCheck(a, year, month, day):
    moon_phase = a.moon_phase(date=datetime.date(year, month, day))
    
    moonPercent = moon_phase/29.53059
#     #print(moon_phase), "Moon Phase", moonPercent
    return moon_phase, "Moon Phase", moonPercent
moonTime = (year, month, day+30.53059)
mc = ephem.Moon(moonTime)

moonConstellation = (ephem.constellation(mc))
moonLoc = (mc.ra, mc.dec)
# #print moonLoc
# #print moonConstellation
# #print "Moon is in",moonConstellation[1]
# #print moonCheck(a, year, month, day)

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


def yesterHours(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime): 
    h = Hours() 
    # #print h 
    
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
    #print " "
    #print "lastPlanetaryHourNightLength:", lastPlanetaryHourNightLength, localtime
    #print " "
    #print pI[1],pI[2].strftime("%H:%M"),pI[3].strftime("%H:%M"),pI[4],pI[5]
    #print pII[1],pII[2].strftime("%H:%M"),pII[3].strftime("%H:%M"),pII[4],pII[5]
    #print pIII[1],pIII[2].strftime("%H:%M"),pIII[3].strftime("%H:%M"),pIII[4],pIII[5]
    #print pIV[1],pIV[2].strftime("%H:%M"),pIV[3].strftime("%H:%M"),pIV[4],pIV[5]
    #print pV[1],pV[2].strftime("%H:%M"),pV[3].strftime("%H:%M"),pV[4],pV[5]
    #print pVI[1],pVI[2].strftime("%H:%M"),pVI[3].strftime("%H:%M"),pVI[4],pVI[5]
    #print pVII[1],pVII[2].strftime("%H:%M"),pVII[3].strftime("%H:%M"),pVII[4],pVII[5]
    #print pVIII[1],pVIII[2].strftime("%H:%M"),pVIII[3].strftime("%H:%M"),pVIII[4],pVIII[5]
    #print pIX[1],pIX[2].strftime("%H:%M"),pIX[3].strftime("%H:%M"),pIX[4],pIX[5]
    #print pX[1],pX[2].strftime("%H:%M"),pX[3].strftime("%H:%M"),pX[4],pX[5]
    #print pXI[1],pXI[2].strftime("%H:%M"),pXI[3].strftime("%H:%M"),pXI[4],pXI[5]
    #print pXII[1],pXII[2].strftime("%H:%M"),pXII[3].strftime("%H:%M"),pXII[4],pXII[5]
    #print" "
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
    
    #print "planetaryHourDayLength:", planetaryHourDayLength, localtime
    #print " "
    #print dI[0],dI[2].strftime("%H:%M"),dI[3].strftime("%H:%M"),dI[4],dI[5]
    #print dII[0],dII[2].strftime("%H:%M"),dII[3].strftime("%H:%M"),dII[4],dII[5]
    #print dIII[0],dIII[2].strftime("%H:%M"),dIII[3].strftime("%H:%M"),dIII[4],dIII[5]
    #print dIV[0],dIV[2].strftime("%H:%M"),dIV[3].strftime("%H:%M"),dIV[4],dIV[5]
    #print dV[0],dV[2].strftime("%H:%M"),dV[3].strftime("%H:%M"),dV[4],dV[5]
    #print dVI[0],dVI[2].strftime("%H:%M"),dVI[3].strftime("%H:%M"),dVI[4],dVI[5]
    #print dVII[0],dVII[2].strftime("%H:%M"),dVII[3].strftime("%H:%M"),dVII[4],dVII[5]
    #print dVIII[0],dVIII[2].strftime("%H:%M"),dVIII[3].strftime("%H:%M"),dVIII[4],dVIII[5]
    #print dIX[0],dIX[2].strftime("%H:%M"),dIX[3].strftime("%H:%M"),dIX[4],dIX[5]
    #print dX[0],dX[2].strftime("%H:%M"),dX[3].strftime("%H:%M"),dX[4],dX[5]
    #print dXI[0],dXI[2].strftime("%H:%M"),dXI[3].strftime("%H:%M"),dXI[4],dXI[5]
    #print dXII[0],dXII[2].strftime("%H:%M"),dXII[3].strftime("%H:%M"),dXII[4],dXII[5]
    
    #print " "
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
    
    #print "planetaryHourNightLength:", planetaryHourNightLength, localtime 
    #print " "
    #print I[1],I[2].strftime("%H:%M"),I[3].strftime("%H:%M"),I[4],I[5]
    #print II[1],II[2].strftime("%H:%M"),II[3].strftime("%H:%M"),II[4],II[5]
    #print III[1],III[2].strftime("%H:%M"),III[3].strftime("%H:%M"),III[4],III[5]
    #print IV[1],IV[2].strftime("%H:%M"),IV[3].strftime("%H:%M"),IV[4],IV[5]
    #print V[1],V[2].strftime("%H:%M"),V[3].strftime("%H:%M"),V[4],V[5]
    #print VI[1],VI[2].strftime("%H:%M"),VI[3].strftime("%H:%M"),VI[4],VI[5]
    #print VII[1],VII[2].strftime("%H:%M"),VII[3].strftime("%H:%M"),VII[4],VII[5]
    #print VIII[1],VIII[2].strftime("%H:%M"),VIII[3].strftime("%H:%M"),VIII[4],VIII[5]
    #print IX[1],IX[2].strftime("%H:%M"),IX[3].strftime("%H:%M"),IX[4],IX[5]
    #print X[1],X[2].strftime("%H:%M"),X[3].strftime("%H:%M"),X[4],X[5]
    #print XI[1],XI[2].strftime("%H:%M"),XI[3].strftime("%H:%M"),XI[4],XI[5]
    #print XII[1],XII[2].strftime("%H:%M"),XII[3].strftime("%H:%M"),XII[4],XII[5]
    return

def sunDegree(sunRise, planetaryHourDayLength):
    h=Hours()
    I = h.hourOne(sunRise, planetaryHourDayLength, todaysDay, localtime)
#     #print I[0],I[2].strftime("%H:%M"),I[3].strftime("%H:%M"),I[4],I[5]
    dayStart = (int(I[2].strftime("%H") )/12.0) + (int(I[2].strftime("%M"))/60.0)
#     dayStart =  (int(I[2].strftime("%M"))/60.0)
#     #print 360.0/dayStart
    
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
#     #print planetaryHourNightLength, "phnl"
    phd = str(planetaryHourNightLength)
    h = 30.0*int(phd.split(":")[0])
#     #print "hhhhhh", h
#     h = 24-h 
    m = int(phd.split(":")[1]) / 60.0
#     s = float(phd.split(":")[2]) / 3600.0
    degree =  (h + m )
    return degree


def clockPosition(time):
#     #print time, "time in clock position"
    clockY = str(dayTime/12)
#     #print clockY, "clockY"
    t = clockY.split(":")
#     #print t, "t"
    h = int(t[0])
#     #print h, "h"
    m = int(t[1])
#     #print m, "m"
    hDegree = (30)*h
    
#     hDegree = (24.0/h)*3-60
    hMinute = 30*(float(m/60.0))
#     #print "timey wimey"
#     #print h, hDegree, "h, hDegree"
#     #print m, hMinute, "m, hMinute"
#check for less than or greater than 1 hour 
    if hDegree == 0:
        position = (hDegree - hMinute) #less than 30 degrees
    else:
        position =  (hDegree + hMinute) #more than 30 degrees
#     #print "position", position 
    return position

def clockPositionNight(time):
#     #print time
    clockY = str(nightTime/12)
#     #print clockY
    t = clockY.split(":")
#     #print t
    h = int(t[0])
#     #print h
    m = int(t[1])
#     #print m
    hDegree = (30*h)
    
#     hDegree = (24.0/h)*3-60
    hMinute = 30*(float(m/60.0))
#     #print "timey wimey"
#     #print h, hDegree
#     #print m, hMinute
#check for less than or greater than 1 hour 
    if hDegree == 0:
        position = (hDegree - hMinute) #less than 30 degrees
    else:
        position =  (hDegree + hMinute) #more than 30 degrees
#     #print "position", position 
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
    elif str(positionChrB) == "GE":
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
 
def retroCheck(planetPosition, planetPositionD):
    if planetPosition < planetPositionD:
        retro = True
        #print "RETROGRADE",planetPosition
    else: 
        retro = False
    return retro
    

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
    
    canvas.delete("all")
    
    global prev_entry
    global this_entry
    
    prev_entry = this_entry
    this_entry = chron.clock()
    interval = this_entry - prev_entry
    
    log.logMsg("Top of app(): " + repr(interval))
    h = Hours() 
    
    #offset 90 moves Aries 0 to 12 o'clock  position
#     offSet = 0
    offSet = 90
    
#     offSet = 180
#     correctionFactorA = 1.3

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
    
    previouS =("lastPlanetaryHourNightLength:", lastPlanetaryHourNightLength,"\n",  
               " ","\n", 
               pI[1],pI[2].strftime("%H:%M"),pI[3].strftime("%H:%M"),pI[5],"\n", 
               pII[1],pII[2].strftime("%H:%M"),pII[3].strftime("%H:%M"),pII[5],"\n", 
               pIII[1],pIII[2].strftime("%H:%M"),pIII[3].strftime("%H:%M"),pIII[5],"\n", 
               pIV[1],pIV[2].strftime("%H:%M"),pIV[3].strftime("%H:%M"),pIV[5],"\n", 
               pV[1],pV[2].strftime("%H:%M"),pV[3].strftime("%H:%M"),pV[5],"\n", 
               pVI[1],pVI[2].strftime("%H:%M"),pVI[3].strftime("%H:%M"),pVI[5],"\n", 
               pVII[1],pVII[2].strftime("%H:%M"),pVII[3].strftime("%H:%M"),pVII[5],"\n", 
               pVIII[1],pVIII[2].strftime("%H:%M"),pVIII[3].strftime("%H:%M"),pVIII[5],"\n", 
               pIX[1],pIX[2].strftime("%H:%M"),pIX[3].strftime("%H:%M"),pIX[5],"\n", 
               pX[1],pX[2].strftime("%H:%M"),pX[3].strftime("%H:%M"),pX[5],"\n", 
               pXI[1],pXI[2].strftime("%H:%M"),pXI[3].strftime("%H:%M"),pXI[5],"\n", 
               pXII[1],pXII[2].strftime("%H:%M"),pXII[3].strftime("%H:%M"),pXII[5],"\n", 
               " ","\n", )
         
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

    dayS = ("planetaryHourDayLength:", planetaryHourDayLength, "\n",
#             "julianC=",julianC.weekday(),julianC.month(),"\n",
            localtime,"\n",
            " ","\n",
            dI[0],dI[2].strftime("%H:%M"),dI[3].strftime("%H:%M"),dI[5],"\n",
            dII[0],dII[2].strftime("%H:%M"),dII[3].strftime("%H:%M"),dII[5],"\n",
            dIII[0],dIII[2].strftime("%H:%M"),dIII[3].strftime("%H:%M"),dIII[5],"\n",
            dIV[0],dIV[2].strftime("%H:%M"),dIV[3].strftime("%H:%M"),dIV[5],"\n",
            dV[0],dV[2].strftime("%H:%M"),dV[3].strftime("%H:%M"),dV[5],"\n",
            dVI[0],dVI[2].strftime("%H:%M"),dVI[3].strftime("%H:%M"),dVI[5],"\n",
            dVII[0],dVII[2].strftime("%H:%M"),dVII[3].strftime("%H:%M"),dVII[5],"\n",
            dVIII[0],dVIII[2].strftime("%H:%M"),dVIII[3].strftime("%H:%M"),dVIII[5],"\n",
            dIX[0],dIX[2].strftime("%H:%M"),dIX[3].strftime("%H:%M"),dIX[5],"\n",
            dX[0],dX[2].strftime("%H:%M"),dX[3].strftime("%H:%M"),dX[5],"\n",
            dXI[0],dXI[2].strftime("%H:%M"),dXI[3].strftime("%H:%M"),dXI[5],"\n",
            dXII[0],dXII[2].strftime("%H:%M"),dXII[3].strftime("%H:%M"),dXII[5],"\n",
    
            " " ,"\n")      

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
    
#     #print I[1],I[2].strftime("%H:%M"),I[3].strftime("%H:%M"),"/n",
#     #print II[1],II[2].strftime("%H:%M"),II[3].strftime("%H:%M"),II[4],II[5],"/n",
#     #print III[1],III[2].strftime("%H:%M"),III[3].strftime("%H:%M"),III[4],III[5],"/n",
#     #print IV[1],IV[2].strftime("%H:%M"),IV[3].strftime("%H:%M"),IV[4],IV[5],"/n",
#     #print V[1],V[2].strftime("%H:%M"),V[3].strftime("%H:%M"),V[4],V[5],"/n",
#     #print VI[1],VI[2].strftime("%H:%M"),VI[3].strftime("%H:%M"),VI[4],VI[5],"/n",
#     #print VII[1],VII[2].strftime("%H:%M"),VII[3].strftime("%H:%M"),VII[4],VII[5],"/n",
#     #print VIII[1],VIII[2].strftime("%H:%M"),VIII[3].strftime("%H:%M"),VIII[4],VIII[5],"/n",
#     #print IX[1],IX[2].strftime("%H:%M"),IX[3].strftime("%H:%M"),IX[4],IX[5],"/n",
#     #print X[1],X[2].strftime("%H:%M"),X[3].strftime("%H:%M"),X[4],X[5],"/n",
#     #print XI[1],XI[2].strftime("%H:%M"),XI[3].strftime("%H:%M"),XI[4],XI[5],"/n",
#     #print XII[1],XII[2].strftime("%H:%M"),XII[3].strftime("%H:%M"),XII[4],XII[5],"/n",
    
    nightS = ("planetaryHourNightLength:", planetaryHourNightLength,"\n",
              localtime,"\n",
              I[1],I[2].strftime("%H:%M"),I[3].strftime("%H:%M"),I[5],"\n",
              II[1],II[2].strftime("%H:%M"),II[3].strftime("%H:%M"),II[5],"\n",
              III[1],III[2].strftime("%H:%M"),III[3].strftime("%H:%M"),III[5],"\n",
              IV[1],IV[2].strftime("%H:%M"),IV[3].strftime("%H:%M"),IV[5],"\n",
              V[1],V[2].strftime("%H:%M"),V[3].strftime("%H:%M"),V[5],"\n",
              VI[1],VI[2].strftime("%H:%M"),VI[3].strftime("%H:%M"),VI[5],"\n",
              VII[1],VII[2].strftime("%H:%M"),VII[3].strftime("%H:%M"),VII[5],"\n",
              VIII[1],VIII[2].strftime("%H:%M"),VIII[3].strftime("%H:%M"),VIII[5],"\n",
              IX[1],IX[2].strftime("%H:%M"),IX[3].strftime("%H:%M"),IX[5],"\n",
              X[1],X[2].strftime("%H:%M"),X[3].strftime("%H:%M"),X[5],"\n",
              XI[1],XI[2].strftime("%H:%M"),XI[3].strftime("%H:%M"),XI[5],"\n",
              XII[1],XII[2].strftime("%H:%M"),XII[3].strftime("%H:%M"),XII[5],"\n")
    
    #print planetaryColor(I[1])
    
#     #print  planetaryHourDayLength
#     #print (sunRise)
#     #print sunSet
#     #print sunDegree(sunRise, planetaryHourDayLength), "sunDegree"
    sunUp = (offSet+75) - sunDegree(sunRise, planetaryHourDayLength)
    #print sunUp, "sunUp"
#     #print clockPosition(dI[2].strftime("%H:%M"))
#     #print "start", clockPosition(dI[2].strftime("%H:%M"))+offSet 
#     #print "end", clockPosition(dI[3].strftime("%H:%M"))+offSet
    sunUpPlus = pHourDegree(planetaryHourDayLength)
#     #print sunUpPlus, "sunUpPlus"
#     sunDown = (offSet/2) - sunDegree(sunSet, planetaryHourNightLength)
    sunDown = (-sunDegree(sunSet, planetaryHourNightLength)-(3*offSet) )-25.5-0.010409712
   
    #print pHourDegree(planetaryHourDayLength), "pHourDegree"
    #print pNightDegree(planetaryHourNightLength) , "pNightDegree"

    sunDownPlus = pNightDegree(planetaryHourNightLength)
#     #print sunDown, "sunDown"
#     #print sunDownPlus , "sunDownPlus"
#     #print (sunDownPlus - sunDown )
    
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    #print time, "this is the mofo"
    hour = int(datetime.datetime.now().strftime("%H"))
    minute = int(datetime.datetime.now().strftime("%M"))
    second = int(datetime.datetime.now().strftime("%S"))
    #positions

    dtime = datetime.datetime(year, month, day, hour, minute, second, 0, pyastro.UTC())
    dtimeYesterday = datetime.datetime(year, month, day-1, hour, minute, second, 0, pyastro.UTC())
    # #print year
    # #print month
    # #print day
    # #print hour 
    # #print minute
    #print dtime, "dtime now"
    #print dtimeYesterday, "dtimeYesterday"
#     break
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
    
# #planetary correction offsets 03.19.19
    moonOffset = 0.23 #vernal equinox full moon calibration 0.23  03.20.19
    mercuryOffset = 0.47
    venusOffset = -2.04
    solOffset = 0.28
    marsOffset =  3.03
    jupiterOffset = 0.85
    saturnOffset = -1.3
    neptuneOffset = -0.6
    uranusOffset = 1.25
    plutoOffset = -1.62

#planetary correction offsets 04.04.19
#     moonOffset = 0 #vernal equinox full moon calibration 0.23  03.20.19
#     mercuryOffset = 0
#     venusOffset = 0
#     solOffset = 0
#     marsOffset =  0
#     jupiterOffset = 0
#     saturnOffset = 0
#     neptuneOffset = 0
#     uranusOffset = 0
#     plutoOffset = 0
    
    monrasc = (mon.right_ascension(formatted=False)) + moonOffset
#     #print monrasc
    merrasc = (mer.right_ascension(formatted=False)) + mercuryOffset
    venrasc = (ven.right_ascension(formatted=False)) + venusOffset
    solrasc = (sol.right_ascension(formatted=False)) + solOffset
    marrasc = (mar.right_ascension(formatted=False)) + marsOffset
    juprasc = (jup.right_ascension(formatted=False)) + jupiterOffset
    satrasc = (sat.right_ascension(formatted=False)) + saturnOffset
    neprasc = (nep.right_ascension(formatted=False)) + neptuneOffset
    urarasc = (ura.right_ascension(formatted=False)) + uranusOffset
    plurasc = (plu.right_ascension(formatted=False)) + plutoOffset 
    
    
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
    
    
    #retro check
    monD = pyastro.Moon(dtimeYesterday) 
    merD = pyastro.Mercury(dtimeYesterday) 
    venD = pyastro.Venus(dtimeYesterday) 
    solD = pyastro.Sun(dtimeYesterday) 
    marD = pyastro.Mars(dtimeYesterday) 
    jupD = pyastro.Jupiter(dtimeYesterday) 
    satD = pyastro.Saturn(dtimeYesterday) 
    nepD = pyastro.Neptune(dtimeYesterday) 
    uraD = pyastro.Uranus(dtimeYesterday) 
    pluD = pyastro.Pluto(dtimeYesterday)
    
    
    monrascD = (monD.right_ascension(formatted=False)) + moonOffset
    merrascD = (merD.right_ascension(formatted=False)) + mercuryOffset
    venrascD = (venD.right_ascension(formatted=False)) + venusOffset
    solrascD = (solD.right_ascension(formatted=False)) + solOffset
    marrascD = (marD.right_ascension(formatted=False)) + marsOffset
    juprascD = (jupD.right_ascension(formatted=False)) + jupiterOffset
    satrascD = (satD.right_ascension(formatted=False)) + saturnOffset
    neprascD = (nepD.right_ascension(formatted=False)) + neptuneOffset
    urarascD = (uraD.right_ascension(formatted=False)) + uranusOffset
    plurascD = (pluD.right_ascension(formatted=False)) + plutoOffset
    
    
    moonPositionD = pyastro.rasc_to_zodiac(monrascD)
    mercuryPositionD = pyastro.rasc_to_zodiac(merrascD)
    venusPositionD = pyastro.rasc_to_zodiac(venrascD)
    solPositionD = pyastro.rasc_to_zodiac(solrascD)
    marsPositionD = pyastro.rasc_to_zodiac(marrascD)
    jupiterPositionD = pyastro.rasc_to_zodiac(juprascD)
    saturnPositionD = pyastro.rasc_to_zodiac(satrascD)
    neptunePositionD = pyastro.rasc_to_zodiac(neprascD)
    uranusPositionD = pyastro.rasc_to_zodiac(urarascD)
    plutoPositionD = pyastro.rasc_to_zodiac(plurascD)
    
    
    #print "Moon:    ",moonPosition 
    #print "Mercury: ",mercuryPosition
    #print "Venus:   ",venusPosition 
    #print "Sun:     ",solPosition 
    #print "Mars:    ",marsPosition
    #print "Jupiter: ",jupiterPosition
    #print "Saturn:  ",saturnPosition
    #print "Neptune: ",neptunePosition
    #print "Uranus:  ",uranusPosition 
    #print "Pluto:   ",plutoPosition 
    
#     planetPos = ("Moon:    ",moonPosition,"\n", 
#                  "Mercury: ",mercuryPosition,"\n",
#                  "Venus:   ",venusPosition ,"\n",
#                  "Sun:     ",solPosition ,"\n",
#                  "Mars:    ",marsPosition,"\n",
#                  "Jupiter: ",jupiterPosition,"\n",
#                  "Saturn:  ",saturnPosition,"\n",
#                  "Neptune: ",neptunePosition,"\n",
#                  "Uranus:  ",uranusPosition ,"\n",
#                  "Pluto:   ",plutoPosition,"\n" )



#  + degree offset to correct position error. this should be in original calculation in pyastro core. not here    
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

    planetPos = ("Moon:    ", moonPosition, moPo, "\n", 
                 "Mercury: ",mercuryPosition, mePo, "\n",
                 "Venus:   ",venusPosition , vePo, "\n",
                 "Sun:     ",solPosition , soPo, "\n",
                 "Mars:    ",marsPosition, maPo, "\n",
                 "Jupiter: ",jupiterPosition,juPo, "\n",
                 "Saturn:  ",saturnPosition,saPo, "\n",
                 "Neptune: ",neptunePosition,nePo, "\n",
                 "Uranus:  ",uranusPosition ,urPo, "\n",
                 "Pluto:   ",plutoPosition,plPo, "\n" )
    
    #planet position 24 hours ago
    moPoD = zodiacDegree(moonPositionD) 
    mePoD = zodiacDegree(mercuryPositionD) 
    vePoD = zodiacDegree(venusPositionD) 
    soPoD = zodiacDegree(solPositionD) 
    maPoD = zodiacDegree(marsPositionD) 
    juPoD = zodiacDegree(jupiterPositionD) 
    saPoD = zodiacDegree(saturnPositionD) 
    nePoD = zodiacDegree(neptunePositionD) 
    urPoD = zodiacDegree(uranusPositionD) 
    plPoD = zodiacDegree(plutoPositionD) 
    

    planetPosD = ("Moon:    ",retroCheck(moPo, moPoD),moonPositionD, moPoD, "\n", 
                 "Mercury: ",retroCheck(mePo, mePoD),mercuryPositionD, mePoD, "\n",
                 "Venus:   ",retroCheck(vePo, vePoD),venusPositionD , vePoD, "\n",
                 "Sun:     ",retroCheck(soPo, soPoD),solPositionD , soPoD, "\n",
                 "Mars:    ",retroCheck(maPo, maPoD),marsPositionD, maPoD, "\n",
                 "Jupiter: ",retroCheck(juPo, juPoD),jupiterPositionD,juPoD, "\n",
                 "Saturn:  ",retroCheck(saPo, saPoD),saturnPositionD,saPoD, "\n",
                 "Neptune: ",retroCheck(nePo, nePoD),neptunePositionD,nePoD, "\n",
                 "Uranus:  ",retroCheck(urPo, urPoD),uranusPositionD ,urPoD, "\n",
                 "Pluto:   ",retroCheck(plPo, plPoD),plutoPositionD,plPoD, "\n" )
     

    
    #print hour, minute, "hour, minute"
    hourLargeDegree = -((360/12)*hour)
    #print hourLargeDegree, "hourLargeDegree"
#     #print minute
    
    hourSmallDegree = float(minute/60.0)*-30.0
    #print hourSmallDegree, "hourSmallDegree"
    #     hourHand = -((360/12)*hour)+(-30*(minute/60))
    hourHand = hourLargeDegree + hourSmallDegree
    
#     #print "hourHand", hourHand
    minuteHand = -((360/60)*minute) + (float(second/60.0)*-6.0)
    secondHand = -((360/60)*second)

    jD = julianC[0],julianC[1],julianC[2],julianC[3],julianC[4],julianC[5],julianC[6],julianC[7]
    
#label info
    canvas.delete("label1")
    ttt = (previouS,dayS,nightS, jD)
#     ttt = str(previouS)
#     ttt.strip("{")
#     ttt.strip("}")
    canvas.create_text(250,400, tags ="label1",text=ttt)
    
# #planet label
#     canvas.create_text(900,200, text = (planetPos))

#outer clock rim
    canvas.create_circle(950, 500, 495, fill="white", outline="#000000", width=10)
    
#  minute tick  
    for m in range(0,360,6): 
        
        canvas.create_circle_arc(950, 500, 473, fill="#0000FF", outline="#000000", start=m-1, end=m)
#         m=m+6
#         #print (m)
 
#  hour tick  
    for m in range(0,360,30): 
        
        canvas.create_circle_arc(950, 500, 490, fill="#000000", outline="#000000", start=m-1, end=m)
#         m=m+6
#         #print (m)

#sub hour tick 
    for m in range(0,360,15): 
        
        canvas.create_circle_arc(950, 500,485, fill="#000000", outline="#000000", start=m, end=m)
#         m=m+6
#         #print (m)

#sub hour tick 
    for m in range(0,360,1): 
        
        canvas.create_circle_arc(950, 500,465, fill="#000000", outline="#000000", start=m, end=m)
#         m=m+6
#         #print (m)
#sub hour tick 

    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5, end=7.5)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+15, end=7.5+15)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+30, end=7.5+30)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+45, end=7.5+45)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+60, end=7.5+60)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+75, end=7.5+75)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+90, end=7.5+90)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+15+90, end=7.5+15+90)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+30+90, end=7.5+30+90)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+45+90, end=7.5+45+90)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+60+90, end=7.5+60+90)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+75+90, end=7.5+75+90)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+180, end=7.5+180)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+15+180, end=7.5+15+180)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+30+180, end=7.5+30+180)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+45+180, end=7.5+45+180)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+60+180, end=7.5+60+180)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+75+180, end=7.5+75+180)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+270, end=7.5+270)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+15+270, end=7.5+15+270)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+30+270, end=7.5+30+270)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+45+270, end=7.5+45+270)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+60+270, end=7.5+60+270)
    canvas.create_circle_arc(950, 500,475, fill="#000000", outline="#000000", start=7.5+75+270, end=7.5+75+270)

# #planetary clock hands bottom layer 
 
#     canvas.create_circle_arc(950, 500, 495, fill="#8b0000", outline="black", start=plPo-0+offSet, end=plPo+0+offSet)
#     canvas.create_circle_arc(950, 500, 495, fill="#006400", outline="black", start=urPo-0+offSet, end=urPo+0+offSet)
#     canvas.create_circle_arc(950, 500, 495, fill="blue", outline="black", start=nePo-0+offSet, end=nePo+0+offSet)
#     canvas.create_circle_arc(950, 500, 495, fill="#8A2BE2", outline="black", start=saPo-0+offSet, end=saPo+0+offSet)
#     canvas.create_circle_arc(950, 500, 495, fill="#EE82EE", outline="black", start=juPo-0+offSet, end=juPo+0+offSet)
#     canvas.create_circle_arc(950, 500, 495, fill="#FF0000", outline="black", start=maPo-0+offSet, end=maPo+0+offSet)
#     canvas.create_circle_arc(950, 500, 495, fill="#FFA500", outline="black", start=soPo-0+offSet, end=soPo+0+offSet)
#     canvas.create_circle_arc(950, 500, 495, fill="#008000", outline="black", start=vePo-0+offSet, end=vePo+0+offSet)
#     canvas.create_circle_arc(950, 500, 495, fill="#FFFF00", outline="black", start=mePo-0+offSet, end=mePo+0+offSet)     
#     canvas.create_circle_arc(950, 500, 495, fill="#c0c0c0", outline="black", start=moPo-0+offSet, end=moPo+0+offSet)

   
#processed lunar mansions ~CE2000
    canvas.create_circle_arc(950, 500, 460, fill="#696969", outline="#000000",width=5, start=0+33+offSet, end=12+33+offSet)
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
    canvas.create_circle_arc(950, 500, 460, fill="#696969", outline="#000000",width=5, start=180+33+offSet, end=192+33+offSet)
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
    canvas.create_circle_arc(950, 500, 430, fill="#696969", outline="#000000",width=5, start=0+offSet, end=12+offSet)
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
    canvas.create_circle_arc(950, 500, 430, fill="#696969", outline="#000000",width=5, start=180+offSet, end=192+offSet)
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
   
# #planetary clock hands bottom layer 
  
    canvas.create_circle_arc(950, 500, 495, fill="#8b0000", outline="black", start=plPo-0+offSet, end=plPo+0+offSet)
    canvas.create_circle_arc(950, 500, 495, fill="#006400", outline="black", start=urPo-0+offSet, end=urPo+0+offSet)
    canvas.create_circle_arc(950, 500, 495, fill="blue", outline="black", start=nePo-0+offSet, end=nePo+0+offSet)
    canvas.create_circle_arc(950, 500, 495, fill="#8A2BE2", outline="black", start=saPo-0+offSet, end=saPo+0+offSet)
    canvas.create_circle_arc(950, 500, 495, fill="#EE82EE", outline="black", start=juPo-0+offSet, end=juPo+0+offSet)
    canvas.create_circle_arc(950, 500, 495, fill="#FF0000", outline="black", start=maPo-0+offSet, end=maPo+0+offSet)
    canvas.create_circle_arc(950, 500, 495, fill="#FFA500", outline="black", start=soPo-0+offSet, end=soPo+0+offSet)
    canvas.create_circle_arc(950, 500, 495, fill="#008000", outline="black", start=vePo-0+offSet, end=vePo+0+offSet)
    canvas.create_circle_arc(950, 500, 495, fill="#FFFF00", outline="black", start=mePo-0+offSet, end=mePo+0+offSet)     
    canvas.create_circle_arc(950, 500, 495, fill="#c0c0c0", outline="black", start=moPo-0+offSet, end=moPo+0+offSet)
 
     
    
    
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
#     water blue, #191970
#     fire red , #FF0000
#     green earth, #808000
#     yellow air, #FFFF00
#      spring
    canvas.create_circle_arc(950, 500, 393, fill="#FFFF00", outline="#000000", start=0+offSet, end=90+offSet)
#     summer
    canvas.create_circle_arc(950, 500, 393, fill="#FF0000", outline="#000000", start=90+offSet, end=180+offSet)
#     autumn
    canvas.create_circle_arc(950, 500, 393, fill="#191970", outline="#000000", start=180+offSet, end=270+offSet)
#     winter
    canvas.create_circle_arc(950, 500, 393, fill="#808000", outline="#000000", start=270+offSet, end=360+offSet)
     
    #zodiac boundaries
     
    canvas.create_circle_arc(950, 500, 385, fill="#FF0000", outline="#000000", start=0+offSet, end=30+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#808000", outline="#000000", start=30+offSet, end=60+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#FFFF00", outline="#000000", start=60+offSet, end=90+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#191970", outline="#000000", start=90+offSet, end=120+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#FF0000", outline="#000000", start=120+offSet, end=150+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#808000", outline="#000000", start=150+offSet, end=180+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#FFFF00", outline="#000000", start=180+offSet, end=210+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#191970", outline="#000000", start=210+offSet, end=240+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#FF0000", outline="#000000", start=240+offSet, end=270+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#808000", outline="#000000", start=270+offSet, end=300+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#FFFF00", outline="#000000", start=300+offSet, end=330+offSet)
    canvas.create_circle_arc(950, 500, 385, fill="#191970", outline="#000000", start=330+offSet, end=360+offSet)

#  decan tick  
    for m in range(0,360,10): 
        
        canvas.create_circle_arc(950, 500, 380, fill="#000000", outline="darkgray", start=m, end=m)
#         m=m+6
#        #print (m)

#  decan small tick  
    for m in range(0,360,1): 
        
        canvas.create_circle_arc(950, 500, 350, fill="#000000", outline="darkgray", start=m, end=m)
#         m=m+6
#        #print (m)


#offsets

#     offsetB = sunUp -90
#     offsetB = -55.5  #thursday 03.21.2019 0715 sunrise
#     offsetB = -35.5  #friday
#     offsetB = -17.5  #saturday
#     offsetB = -4.5 #sunday
#     offsetB = 10.5  #monday
#     offsetB = 45 #tuesday
#     offsetB = 58 #wednesday  
    offsetB = -90 #-10, 69
    
#     offsetB = 90
    #print offsetB, "offsetB"
    
    offsetC = -90 #-6, 270
    
    offsetD = -90  #3, 180
    

#refresh hours if needed  
    canvas.delete("hours") 
#previous night hours

#     theSunWasUp = sunDegree(lastSunSet, lastPlanetaryHourNightLength)
    #print "lastSunSet"
    #print lastSunSet.hour, lastSunSet.minute
    lastSunHourLargeDegree = -((360/12)*lastSunSet.hour)
    #print lastSunHourLargeDegree, "lastSunHourLargeDegree"

    lastSunHourSmallDegree = float(lastSunSet.minute/60.0)*-30.0
    #print lastSunHourSmallDegree, "lastSunHourSmallDegree"
    lastSunHourHand = lastSunHourLargeDegree + lastSunHourSmallDegree
#     lastSunMinuteHand = -((360/60)*lastSunSet.minute) + (float(lastSunSet.second/60.0)*-6.0)
#     lastSunSecondHand = -((360/60)*lastSunSet.second)
#     
    theSunWasUp = lastSunHourHand - offsetC
    
    #print theSunWasUp ,"theSunWasUp"
    #print theSunWasUp + offsetC,"theSunWasUp + offsetC"
    #print abs(clockPositionNight(lastPlanetaryHourNightLength)),"abs(clockPositionNight(lastPlanetaryHourNightLength))"
    
#     
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pI[1]), 
                            outline="#000000", tags="hours",
                            start =(theSunWasUp),
                            end=(theSunWasUp+  (1*clockPositionNight(lastPlanetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pII[1]), 
                            outline="#000000", tags="hours",
                            start =(theSunWasUp+ (1*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end =(theSunWasUp+  (2    *clockPositionNight(lastPlanetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIII[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (2*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (3*clockPositionNight(lastPlanetaryHourNightLength))))
   
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIV[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (3*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (4*clockPositionNight(lastPlanetaryHourNightLength))))
      
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pV[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (4*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (5*clockPositionNight(lastPlanetaryHourNightLength))))
   
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVI[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (5*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (6*clockPositionNight(lastPlanetaryHourNightLength))))
  
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVII[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (6*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (7*clockPositionNight(lastPlanetaryHourNightLength))))
  
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVIII[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (7*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (8*clockPositionNight(lastPlanetaryHourNightLength))))
  
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIX[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (8*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (9*clockPositionNight(lastPlanetaryHourNightLength))))
  
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pX[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (9*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (10*clockPositionNight(lastPlanetaryHourNightLength))))
  
    canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pXI[1]), 
                             outline="#000000", tags="hours",
                              start= (theSunWasUp+  (10*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (11*clockPositionNight(lastPlanetaryHourNightLength))))
  
    canvas.create_circle_arc(950, 500, 335, fill=planetaryColor(pXII[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunWasUp+  (11*clockPositionNight(lastPlanetaryHourNightLength))), 
                             end=(theSunWasUp+  (12*clockPositionNight(lastPlanetaryHourNightLength))))

#     #print sunRise
#     #print clockPosition(planetaryHourDayLength), "clockPosition(sunRise)"

#day hours
  
#     theSunIsUp = sunDegree(sunRise, planetaryHourDayLength)
    #print "sunRise"
    #print sunRise.hour, sunRise.minute
    sunHourLargeDegree = -((360/12)*sunRise.hour)
    #print sunHourLargeDegree, "sunHourLargeDegree"

    sunHourSmallDegree = float(sunRise.minute/60.0)*-30.0
    #print sunHourSmallDegree, "sunHourSmallDegree"
    sunHourHand = sunHourLargeDegree + sunHourSmallDegree
#     sunMinuteHand = -((360/60)*sunRise.minute) + (float(sunRise.second/60.0)*-6.0)
#     sunSecondHand = -((360/60)*sunRise.second)
#     
    theSunIsUp = sunHourHand -offsetB
    
    
    #print theSunIsUp, "theSunIsUp"
    #print planetaryHourDayLength, "planetaryHourDayLength"
    #print abs(clockPosition(planetaryHourDayLength)), "abs(clockPosition(planetaryHourDayLength))"
    canvas.create_circle_arc(950, 500, 320, 
                             fill = planetaryColor(dI[0]), 
                             outline ="#000000", tags="hours",
                             start = (theSunIsUp),
                             end = (theSunIsUp -  (clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, 
                            fill=planetaryColor(dII[0]), 
                            outline="#000000", tags="hours",
                            start=(theSunIsUp -  (clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (2*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, 
                            fill=planetaryColor(dIII[0]), 
                            outline="#000000", tags="hours",
                            start=(theSunIsUp -  (2*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (3*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, 
                            fill=planetaryColor(dIV[0]), 
                            outline="#000000", tags="hours",
                            start=(theSunIsUp -  (3*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (4*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, 
                            fill=planetaryColor(dV[0]), 
                            outline="#000000", tags="hours",
                            start=(theSunIsUp -  (4*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (5*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dVI[0]), 
                             outline="#000000", tags="hours",
                            start=(theSunIsUp -  (5*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (6*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dVII[0]), 
                             outline="#000000", tags="hours",
                             start=(theSunIsUp -  (6*clockPosition(planetaryHourDayLength))),
                            end=(offsetB -theSunIsUp-  (7*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dVIII[0]), 
                             outline="#000000", tags="hours",
                             start=(theSunIsUp -  (7*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (8*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, 
                             fill=planetaryColor(dIX[0]), 
                             outline="#000000", tags="hours",
                             start=(theSunIsUp -  (8*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (9*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 320, fill=planetaryColor(dX[0]), 
                             outline="#000000", tags="hours",
                             start=(theSunIsUp -  (9*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (10*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 310, fill=planetaryColor(dXI[0]), 
                             outline="#000000", tags="hours",
                             start=(theSunIsUp -  (10*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (11*clockPosition(planetaryHourDayLength))))
    canvas.create_circle_arc(950, 500, 300, fill=planetaryColor(dXII[0]), 
                             outline="#000000", tags="hours",
                             start=(theSunIsUp -  (11*clockPosition(planetaryHourDayLength))),
                            end=(theSunIsUp -  (12*clockPosition(planetaryHourDayLength))))
# # #     #print "sunset", ((sunUp)-(12 * sunUpPlus))
#     
# #night hours
# # 
#     theSunIsDown = sunDegree(sunSet, planetaryHourNightLength)
#     theSunIsDown = (offsetB - offsetD - theSunIsUp - (12*clockPosition(planetaryHourDayLength))) 
    #print "sunSet"
    #print sunSet.hour, sunSet.minute
    sunSetHourLargeDegree = -((360/12)*sunSet.hour)
    #print lastSunHourLargeDegree, "sunHourLargeDegree"

    sunSetHourSmallDegree = float(sunSet.minute/60.0)*-30.0
    #print sunSetHourSmallDegree, "sunSetHourSmallDegree"
    sunSetHourHand = sunSetHourLargeDegree + sunSetHourSmallDegree
#     sunSetMinuteHand = -((360/60)*sunSet.minute) + (float(sunSet.second/60.0)*-6.0)
#     sunSetSecondHand = -((360/60)*sunSet.second)
    
    theSunIsDown =  sunSetHourHand - offsetD
     
    #print theSunIsDown, "theSunIsDown"
#     #print theSunIsDown , "theSunIsDown + 720"
    #print abs(clockPositionNight(planetaryHourNightLength)),"abs(clockPositionNight(planetaryHourNightLength))"
    
    canvas.create_circle_arc(950, 500, 290, 
                            fill=planetaryColor(I[1]), 
                            outline="#000000", tags="hours",
                            start = (theSunIsDown),
                            end = (theSunIsDown +  (1*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                            fill=planetaryColor(II[1]), 
                            outline="#000000", tags="hours",
                            start = (theSunIsDown+  (1*clockPositionNight(planetaryHourNightLength))), 
                            end = (theSunIsDown+  (2*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                            fill=planetaryColor(III[1]), 
                            outline="#000000", tags="hours",
                            start= (theSunIsDown+   (2*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+   (3*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                            fill=planetaryColor(IV[1]), 
                            outline="#000000", tags="hours",
                            start= (theSunIsDown+   (3*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+   (4*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                             fill=planetaryColor(V[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunIsDown+   (4*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+   (5*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                             fill=planetaryColor(VI[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunIsDown+   (5*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+   (6*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                             fill=planetaryColor(VII[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunIsDown+   (6*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+   (7*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                             fill=planetaryColor(VIII[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunIsDown+  (7*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+  (8*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                             fill=planetaryColor(IX[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunIsDown+  (8*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+  (9*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                             fill=planetaryColor(X[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunIsDown+   (9*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+   (10*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                             fill=planetaryColor(XI[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunIsDown+   (10*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+   (11*clockPositionNight(planetaryHourNightLength))))
    canvas.create_circle_arc(950, 500, 290, 
                             fill=planetaryColor(XII[1]), 
                             outline="#000000", tags="hours",
                             start= (theSunIsDown+   (11*clockPositionNight(planetaryHourNightLength))), 
                             end=(theSunIsDown+   (12*clockPositionNight(planetaryHourNightLength))))
# 





    
#inner circle    
    canvas.create_circle(950, 500, 270, fill="white", outline="white", width=10)

#sub hour tick 
    for m in range(0,360,15): 
         
        canvas.create_circle_arc(950, 500,275, fill="#000000", outline="#000000", start=m, end=m)
#         m=m+6
#         #print (m)
 
#sub hour tick 
#     for m in range(0,360,15): 
         
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5, end=7.5)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+15, end=7.5+15)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+30, end=7.5+30)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+45, end=7.5+45)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+60, end=7.5+60)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+75, end=7.5+75)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+90, end=7.5+90)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+15+90, end=7.5+15+90)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+30+90, end=7.5+30+90)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+45+90, end=7.5+45+90)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+60+90, end=7.5+60+90)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+75+90, end=7.5+75+90)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+180, end=7.5+180)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+15+180, end=7.5+15+180)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+30+180, end=7.5+30+180)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+45+180, end=7.5+45+180)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+60+180, end=7.5+60+180)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+75+180, end=7.5+75+180)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+270, end=7.5+270)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+15+270, end=7.5+15+9270)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+30+270, end=7.5+30+270)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+45+270, end=7.5+45+270)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+60+270, end=7.5+60+270)
    canvas.create_circle_arc(950, 500,270, fill="#000000", outline="#000000", start=7.5+75+270, end=7.5+75+270) 
 
#inner circle   2 
    canvas.create_circle(950, 500, 260, fill="black", outline="#000000", width=5)

        
#planetary planet hands top layer
    canvas.create_circle_arc(950, 500, 420, fill="#8b0000", outline="black", start=plPo-1+offSet, end=plPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#006400", outline="black", start=urPo-1+offSet, end=urPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="blue", outline="black", start=nePo-1+offSet, end=nePo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#8A2BE2", outline="black", start=saPo-1+offSet, end=saPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#EE82EE", outline="black", start=juPo-1+offSet, end=juPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#FF0000", outline="black", start=maPo-1+offSet, end=maPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#FFA500", outline="black", start=soPo-1+offSet, end=soPo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#008000", outline="black", start=vePo-1+offSet, end=vePo+offSet)
    canvas.create_circle_arc(950, 500, 420, fill="#FFFF00", outline="black", start=mePo-1+offSet, end=mePo+offSet)    
    canvas.create_circle_arc(950, 500, 420, fill="#c0c0c0", outline="black", start=moPo-1+offSet, end=moPo+offSet)

      
#clock
#     canvas.delete("clock1") 
    canvas.create_circle_arc(950, 500, 360, fill="black", outline="white", tags="clock",start=(hourHand -3+offSet), end=(hourHand+offSet))
    canvas.create_circle_arc(950, 500, 476, fill="black", outline="white", tags="clock",start=(minuteHand -2+offSet), end=(minuteHand+offSet))
    canvas.create_circle_arc(950, 500, 495, fill="black", outline="white", tags="clock1",start=(secondHand -1+offSet), end=(secondHand+offSet))

    
    
#planet label
    canvas.delete("label2") 
    canvas.create_text(1500,100, tags = "label2",text = (planetPos))
    canvas.create_text(1500,900, tags = "label2",text = (planetPosD))
    
    
    
    #root.update_idletasks()
    root.after(1000, App)
    return




#App() 

#root.update_idletasks()
#root.after(1000, App)
#root.mainloop()
App()

while True:
    root.update_idletasks()
    root.update() 


#  
# def main():
#     app = App()
#     app.mainloop()
# 
# if __name__ == "__main__":
#     main()
