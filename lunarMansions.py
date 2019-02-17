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
#pip install pyastro
import time 
import datetime
import ephem
# https://rhodesmill.org/pyephem/  pip install ephem
from astral import Astral
import Tkinter as tk 
 
# https://github.com/sffjunkie/astral   pip install astral
# import swisseph as swe
# from Planetaries import Hours


city_name = 'Spruce Creek'
# city_name = 'Chicago'

# print time.time()
# print time.time()+3600
yester= time.localtime(time.time()-86400)
# print time.localtime(time.time())
morrow= time.localtime(time.time()+86400)

localtime = time.asctime( time.localtime(time.time()) )
# print localtime

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

 


# print pyastro.positions(dtime)
# print ms

# from tkinter import *
root = tk.Tk()
canvas = tk.Canvas(root, width=1900, height=1000, borderwidth=0, highlightthickness=0, bg="#d3d3d3")
canvas.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc

canvas.create_circle(950, 500, 450, fill="white", outline="#000000", width=20)

#processed lunar mansions
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=0+33, end=12+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=12+33, end=25+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=25+33, end=38.5+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=38.5+33, end=52+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=52+33, end=64+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=64+33, end=77.5+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=77.5+33, end=90+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=90+33, end=102+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=102+33, end=115+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=115+33, end=128.5+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=128.5+33, end=142+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=142+33, end=154+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=154+33, end=167.5+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=167.5+33, end=180+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=180+33, end=192+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=192+33, end=205+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=205+33, end=218.5+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=218.5+33, end=232+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=232+33, end=244+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=244+33, end=257.5+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=257.5+33, end=270+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=270+33, end=282+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=282+33, end=295+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=295+33, end=308.5+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=308.5+33, end=322+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=322+33, end=334+33)
canvas.create_circle_arc(950, 500, 433, fill="#fffff0", outline="#dcdcdc", start=334+33, end=347.5+33)
canvas.create_circle_arc(950, 500, 433, fill="white", outline="#dcdcdc", start=347.5+33, end=360+33)


#lunar mansions
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=0, end=12)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=12, end=25)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=25, end=38.5)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=38.5, end=52)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=52, end=64)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=64, end=77.5)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=77.5, end=90)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=90, end=102)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=102, end=115)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=115, end=128.5)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=128.5, end=142)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=142, end=154)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=154, end=167.5)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=167.5, end=180)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=180, end=192)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=192, end=205)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=205, end=218.5)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=218.5, end=232)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=232, end=244)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=244, end=257.5)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=257.5, end=270)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=270, end=282)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=282, end=295)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=295, end=308.5)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=308.5, end=322)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=322, end=334)
canvas.create_circle_arc(950, 500, 420, fill="#fffff0", outline="#dcdcdc", start=334, end=347.5)
canvas.create_circle_arc(950, 500, 420, fill="white", outline="#dcdcdc", start=347.5, end=360)


#dali?

canvas.create_circle_arc(950, 500, 420, fill="#c0c0c0", outline="", start=moPo-2, end=moPo)
canvas.create_circle_arc(950, 500, 420, fill="#FFFF00", outline="", start=mePo-2, end=mePo)
canvas.create_circle_arc(950, 500, 420, fill="#008000", outline="", start=vePo-2, end=vePo)
canvas.create_circle_arc(950, 500, 420, fill="#FFA500", outline="", start=soPo-2, end=soPo)
canvas.create_circle_arc(950, 500, 420, fill="#FF0000", outline="", start=maPo-2, end=maPo)
canvas.create_circle_arc(950, 500, 420, fill="#EE82EE", outline="", start=juPo-2, end=juPo)
canvas.create_circle_arc(950, 500, 420, fill="#8A2BE2", outline="", start=saPo-2, end=saPo)
canvas.create_circle_arc(950, 500, 420, fill="blue", outline="", start=nePo-2, end=nePo)
canvas.create_circle_arc(950, 500, 420, fill="#006400", outline="", start=urPo-2, end=urPo)
canvas.create_circle_arc(950, 500, 420, fill="red", outline="", start=plPo-2, end=plPo)



#backround cover
canvas.create_circle(950, 500, 150, fill="white", outline="white", width=10)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=moPo-5, end=moPo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=mePo-5, end=mePo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=vePo-5, end=vePo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=soPo-5, end=soPo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=maPo-5, end=maPo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=juPo-5, end=juPo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=saPo-5, end=saPo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=nePo-5, end=nePo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=urPo-5, end=urPo)
canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=plPo-5, end=plPo)

#zodiac boundaries

canvas.create_circle_arc(950, 500, 380, fill="#FF0000", outline="#dcdcdc", start=0, end=30)
canvas.create_circle_arc(950, 500, 380, fill="#808000", outline="#dcdcdc", start=30, end=60)
canvas.create_circle_arc(950, 500, 380, fill="#FFFF00", outline="#dcdcdc", start=60, end=90)
canvas.create_circle_arc(950, 500, 380, fill="#191970", outline="#dcdcdc", start=90, end=120)
canvas.create_circle_arc(950, 500, 380, fill="#FF0000", outline="#dcdcdc", start=120, end=150)
canvas.create_circle_arc(950, 500, 380, fill="#808000", outline="#dcdcdc", start=150, end=180)
canvas.create_circle_arc(950, 500, 380, fill="#FFFF00", outline="#dcdcdc", start=180, end=210)
canvas.create_circle_arc(950, 500, 380, fill="#191970", outline="#dcdcdc", start=210, end=240)
canvas.create_circle_arc(950, 500, 380, fill="#FF0000", outline="#dcdcdc", start=240, end=270)
canvas.create_circle_arc(950, 500, 380, fill="#808000", outline="#dcdcdc", start=270, end=300)
canvas.create_circle_arc(950, 500, 380, fill="#FFFF00", outline="#dcdcdc", start=300, end=330)
canvas.create_circle_arc(950, 500, 380, fill="#191970", outline="#dcdcdc", start=330, end=360)

canvas.create_circle(950, 500, 325, fill="white", outline="white", width=10)


#dali?

canvas.create_circle_arc(950, 500, 420, fill="#c0c0c0", outline="", start=moPo-2, end=moPo)
canvas.create_circle_arc(950, 500, 420, fill="#FFFF00", outline="", start=mePo-2, end=mePo)
canvas.create_circle_arc(950, 500, 420, fill="#008000", outline="", start=vePo-2, end=vePo)
canvas.create_circle_arc(950, 500, 420, fill="#FFA500", outline="", start=soPo-2, end=soPo)
canvas.create_circle_arc(950, 500, 420, fill="#FF0000", outline="", start=maPo-2, end=maPo)
canvas.create_circle_arc(950, 500, 420, fill="#EE82EE", outline="", start=juPo-2, end=juPo)
canvas.create_circle_arc(950, 500, 420, fill="#8A2BE2", outline="", start=saPo-2, end=saPo)
canvas.create_circle_arc(950, 500, 420, fill="blue", outline="", start=nePo-2, end=nePo)
canvas.create_circle_arc(950, 500, 420, fill="#006400", outline="", start=urPo-2, end=urPo)
canvas.create_circle_arc(950, 500, 420, fill="red", outline="", start=plPo-2, end=plPo)


# canvas.create_circle_arc(500, 400, 100, style="arc", outline="white", width=6, start=270-25, end=270+25)
# canvas.create_circle(500, 400, 20, fill="#BBB", outline="")

root.wm_title("Circles and Arcs")
root.mainloop()

