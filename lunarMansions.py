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
#02/19/2019 modified with updated JPL keplerian elements from https://ssd.jpl.nasa.gov/txt/p_elem_t2.txt
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
print m
sunConstellation = (ephem.constellation(m))
sunLoc = m.ra, m.dec
print "sunLoc",sunLoc



a = Astral()
a.solar_depression = 'civil'

city = a[city_name]

print('Information for %s/%s' % (city_name, city.region))
# Information for London/England

timezone = city.timezone
print('Timezone: %s' % timezone)
# Timezone: Europe/London

print('Latitude: %.02f; Longitude: %.02f' % (city.latitude, city.longitude))
# Latitude: 51.60; Longitude: 0.08
print "Local current time :", localtime
now = localtime.split(" ")
print now
# print now[4], "now"
hms = now[3]
print hms

hour = int(hms.split(":")[0])
# print "hour",hour
minute = int(hms.split(":")[1])
# print "minute", minute
second = int(hms.split(":")[2])
# print second

print "Sun is in",sunConstellation[1]
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
print "Moon is in",moonConstellation[1]
print moonCheck(a, year, month, day)

# print datetime.datetime(),"datetime.datetime"


dtime = datetime.datetime(year, month, day, hour, minute, second, 0, pyastro.UTC())
# print year
# print month
# print day
# print hour 
# print minute
print dtime, "dtime now"
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


def zodiacDegree(planetPosition):

    planetPositionString = str(planetPosition)
#     print planetPositionString[0]
#     print planetPositionString[1]
#     print planetPositionString[2]
#     print planetPositionString[3]
#     print planetPositionString[4]
#     print planetPositionString[5]
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
    elif str(positionChrB) == "LB":
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
    return zodDegPos + zodMinPos + zodSignDegree
    
   
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

print hour, minute
hourLargeDegree = -((360/12)*hour)
print hourLargeDegree, "hourLargeDegree"
print minute

hourSmallDegree = float(minute/60.0)*-30.0
print hourSmallDegree, "hourSmallDegree"
#     hourHand = -((360/12)*hour)+(-30*(minute/60))
hourHand = hourLargeDegree + hourSmallDegree

print "hourHand", hourHand
minuteHand = -((360/60)*minute) + (float(second/60.0)*-6.0)
secondHand = -((360/60)*second)


def update(): 
    hour
    print hour
    minute
    print minute
    second
    print second
    print "Moon:    ",moonPosition , moPo
    print "Mercury: ",mercuryPosition, mePo
    print "Venus:   ",venusPosition, vePo
    print "Sun:     ",solPosition, soPo 
    print "Mars:    ",marsPosition, maPo
    print "Jupiter: ",jupiterPosition, juPo
    print "Saturn:  ",saturnPosition, saPo
    print "Neptune: ",neptunePosition, nePo
    print "Uranus:  ",uranusPosition, urPo 
    print "Pluto:   ",plutoPosition, plPo 
#     hourHand = -((360/12)*hour)+(30*(minute/60))
    print hourHand 
    print minuteHand
    print secondHand
    print localtime
   
    root.after(1000, update)  
    return

 


# print pyastro.positions(dtime)
# print ms

# from tkinter import *
# root = tk.Tk()
# canvas = tk.Canvas(root, width=1900, height=1000, borderwidth=0, highlightthickness=0, bg="#d3d3d3")
# canvas.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc


def App():
    hour
    minute
    second
 
#offset 90 moves Aries 0 to 12 o'clock  position
#     offSet = 0
    offSet = 90
#     offSet = -90
#     offSet = 180

#outer clock rim
    canvas.create_circle(950, 500, 495, fill="white", outline="#000000", width=5)
    
#  minute tick  
    for m in range(0,360,6): 
        
        canvas.create_circle_arc(950, 500, 473, fill="#0000FF", outline="#000000", start=m-1, end=m)
#         m=m+6
        print (m)
 
#  hour tick  
    for m in range(0,360,30): 
        
        canvas.create_circle_arc(950, 500, 490, fill="#000000", outline="#000000", start=m-1, end=m)
#         m=m+6
        print (m)
   
#processed lunar mansions
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
    
    
#traditional lunar mansions
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
        print (m)


#inner circle    
    canvas.create_circle(950, 500, 340, fill="white", outline="white", width=10)
        
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
#     #invert for clockwise rotation
# 
#     print hour, minute
#     hourLargeDegree = -((360/12)*hour)
#     print hourLargeDegree, "hourLargeDegree"
#     print minute
#     
#     hourSmallDegree = float(minute/60.0)*-30.0
#     print hourSmallDegree, "hourSmallDegree"
# #     hourHand = -((360/12)*hour)+(-30*(minute/60))
#     hourHand = hourLargeDegree + hourSmallDegree
# 
#     print "hourHand", hourHand
#     minuteHand = -((360/60)*minute)
#     secondHand = -((360/60)*second)
    canvas.create_circle_arc(950, 500, 390, fill="black", outline="", start=(hourHand -5+offSet), end=(hourHand+offSet))
    canvas.create_circle_arc(950, 500, 450, fill="black", outline="", start=(minuteHand -2+offSet), end=(minuteHand+offSet))
    canvas.create_circle_arc(950, 500, 495, fill="black", outline="", start=(secondHand -1+offSet), end=(secondHand+offSet))
    
    
#     canvas.create_circle_arc(500, 400, 100, style="arc", outline="white", width=6, start=270-25, end=270+25)
#     canvas.create_circle(500, 400, 20, fill="#BBB", outline="")
    localtime
    time
#     root.after(1000, update)
    root.wm_title("astronomical lunar mansion clock")
    doog = (App)
    root.after(1000, doog)
    return



def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms

# run first time
# clock()    

App() 
root.after(1000, update)
root.mainloop()


# 
# def main():
#     app = App()
#     app.mainloop()
# 
# if __name__ == "__main__":
#     main()
