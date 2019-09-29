'''
Created on Nov 22, 2018 

@author: doktorbrown

Modified on Sep 28, 2019 

@author: doktorbrown

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
from Hours import *


# root = Tk() 
# 
# lab = Label(root)
# lab.pack()


 
# https://github.com/sffjunkie/astral   pip install astral
# import swisseph as swe

# from Planetaries import Hours

# log = logger.Logger()
# 
# log.logMsg("starting up...")
# 
# prev_entry = 0
# this_entry = 0
# 
# root = tk.Tk()
# canvas = tk.Canvas(root, width=1900, height=1000, borderwidth=0, highlightthickness=0, bg="#d3d3d3")
# canvas.grid()
# root.wm_title("astronomical lunar mansion clock")

#currently this needs to be added to the 


city_name = 'Spruce Creek'

# city_name = 'cabin'
# city_name = 'Chicago'
#148
# city_name = 'subbadubbawubbawoo'

# #print time.time()
# #print time.time()+3600
julianC = time.localtime(time.time()-(86400*13))
#print "julianC=",julianC
yester= time.localtime(time.time()-86400)
# #print time.localtime(time.time())
morrow= time.localtime(time.time()+86400)
# 
# def timeUpdate():
#     return time.asctime( time.localtime(time.time()) )

#         time = datetime.datetime.now().strftime("Time: %H:%M:%S")
#         print time, "this is the mofo"
#         hour = int(datetime.datetime.now().strftime("%H"))
#         minute = int(datetime.datetime.now().strftime("%M"))
#         second = int(datetime.datetime.now().strftime("%S"))
        

# def timeUpdate():
#     return datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y" )


global localtime
localtime = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y" )

#(year, month, day[, hour[, minute[, second
#Sat Sep 28 17:54:34 2019 localtime
print localtime, "localtime"

todayDate=datetime.date.today()
print todayDate, "tofaydate"


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
# a.geocoder.add_locations([("Cabin","USA",41.833333,-76.133333,"US/Eastern",467)])
# a.geocoder.add_locations([("subbadubbawubbawoo","USA",0,0,"Europe/London",0)])
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

