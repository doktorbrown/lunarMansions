'''
Created on Nov 22, 2018 

@author: doktorbrown

Modified on Sep 28, 2019 

@author: doktorbrown

'''


import datetime
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
from SunCalc import *
from PlanetaryHourDisplay import *
from ClockFace import *

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

def App():
    #this prevents the display from stacking upon itself and slowing
    canvas.delete("all")
    global localtime
#     localtime = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y" )
    print localtime, "loacaltime inside App"
#     time = datetime.datetime.now().strftime("Time: %H:%M:%S")
#     print time, "this is the mofo"
    global prev_entry
    global this_entry


#     
#     prev_entry = this_entry
#     this_entry = chron.clock()
#     interval = this_entry - prev_entry
#     
#     log.logMsg("Top of app(): " + repr(interval))
    h = Hours() 
    
    #offset 90 moves Aries 0 to 12 o'clock  position
#     offSet = 0
#     offSet = 90
    offSet = 90
    
#     offSet = 180
#     correctionFactorA = 1.3

#     yesterHours(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
#     todayHours(sunRise, planetaryHourDayLength, todaysDay, localtime)
#     toniteHours(sunSet, planetaryHourNightLength, todaysDay, localtime)
#
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
#          
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
    
    print  planetaryHourDayLength
    print (sunRise)
    print sunSet
    print sunDegree(sunRise, planetaryHourDayLength), "sunDegree"
    sunUp = (offSet+75) - 360-sunDegree(sunRise, planetaryHourDayLength)
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
#     print time, "this is the mofo"
    hour = int(datetime.datetime.now().strftime("%H"))
    minute = int(datetime.datetime.now().strftime("%M"))
    second = int(datetime.datetime.now().strftime("%S"))
    #positions

    dtime = datetime.datetime(year, month, day, hour, minute, second, 0, pyastro.UTC())
    
    try:
        
        dtimeYesterday = datetime.datetime(year, month, day-1, hour, minute, second, 0, pyastro.UTC())
    except:
        dtimeYesterday = datetime.datetime(year, month-1, 30, hour, minute, second, 0, pyastro.UTC())
        
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
    
# # #planetary correction offsets 03.19.19
#     moonOffset = 0.23 #vernal equinox full moon calibration 0.23  03.20.19
#     mercuryOffset = 0.47
#     venusOffset = -2.04
#     solOffset = 0.28
#     marsOffset =  3.03
#     jupiterOffset = 0.85
#     saturnOffset = -1.3
#     neptuneOffset = -0.6
#     uranusOffset = 1.25
#     plutoOffset = -1.62

# planetary correction offsets zero
    moonOffset = 0 #used to check with no offset
    mercuryOffset = 0
    venusOffset = 0
    solOffset = 0
    marsOffset =  0
    jupiterOffset = 0
    saturnOffset = 0
    neptuneOffset = 0
    uranusOffset = 0
    plutoOffset = 0

# # #planetary correction offsets from 0 offset 06.21.19
#     moonOffset = -1.8417 #solstice calculation against morinus 06.21.19 0729
#     mercuryOffset = -1.6356
#     venusOffset = 1.7028
#     solOffset = 0.4761
#     marsOffset =  -1.6486
#     jupiterOffset = 1.2978
#     saturnOffset = -1.2942
#     neptuneOffset = -0.3925
#     uranusOffset = 1.4167
#     plutoOffset = -1.5967

    
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
    
#planet label
#     canvas.create_text(900,200, text = (planetPos))

#

#clockface is created
    cf = ClockFace()
    cb=cf.display(canvas)
    

#planetary hours time arcs are called here
    phd = PlanetaryHourDisplay()
    pb=phd.display(canvas)
#     print pb
    
    
#     print"phd"
 




    
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

    # #planetary clock hands bottom layer
    # planet positions would be needed here if it 
    # is to continue to be part of clockface for stacking 
      
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

         
     # planet positions would be needed here if it 
    # is to continue to be part of clockface for stacking        
     
#     backround cover.  not used. would allow text flag to planet positions
#     canvas.create_circle(950, 500, 275, fill="white", outline="white", width=10)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=moPo-5+offSet, end=moPo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=mePo-5+offSet, end=mePo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=vePo-5+offSet, end=vePo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=soPo-5+offSet, end=soPo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=maPo-5+offSet, end=maPo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=juPo-5+offSet, end=juPo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=saPo-5+offSet, end=saPo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=nePo-5+offSet, end=nePo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=urPo-5+offSet, end=urPo+offSet)
#     canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=plPo-5+offSet, end=plPo+offSet)
#  
#inner circle   2 
    canvas.create_circle(950, 500, 260, fill="white", outline="#000000", width=5)
#planetary clock hands bottom layer 
  
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
    root.after(500, App)
    return




#App() 

#root.update_idletasks()
#root.after(1000, App)
#root.mainloop()
App()

while True:
    root.update_idletasks()
    global localtime
    localtime = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y" )
    print localtime, "this tha other mofo"
    root.update() 


#  
# def main():
#     app = App()
#     app.mainloop()
# 
# if __name__ == "__main__":
#     main()
