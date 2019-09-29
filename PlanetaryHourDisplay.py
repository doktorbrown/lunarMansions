'''
Created on Nov 22, 2018 

@author: doktorbrown

Modified on Sep 28, 2019 

@author: doktorbrown

'''
# import datetime
# import pyastro
#02/22/2019 modified with updated JPL keplerian elements from https://ssd.jpl.nasa.gov/txt/p_elem_t2.txt
#pip install pyastro
import time 
import datetime
# import ephem
# https://rhodesmill.org/pyephem/  pip install ephem
from astral import Astral
import Tkinter as tk 
from Tkinter import *
# import time as chron
# import logger
from Hours import *
from SunCalc import *


class PlanetaryHourDisplay():
        
    def __init__(self):
        self.PlanetaryHourDisplay = []
        
    def display(self,canvas):
#         time = datetime.datetime.now().strftime("Time: %H:%M:%S")
# #         print time, "this is the mofo"
#         hour = int(datetime.datetime.now().strftime("%H"))
#         minute = int(datetime.datetime.now().strftime("%M"))
#         second = int(datetime.datetime.now().strftime("%S"))
#         
        #Sat Sep 28 17:54:34 2019 localtime
        try:
#             canvas.delete("all")#display  goes minimal when on
            global localtime
            localtime = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y" )
            print localtime, "this fucker's in phd"
            
            h = Hours()
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
        
         
                   
            offsetB = -90
            #print offsetB, "offsetB"
            
            offsetC = -90 #-6, 270
            
            offsetD = -90  #3, 180
            
        
        #refresh hours if needed  
            canvas.delete("hours") 
            print "canv"
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
            
    ##         to do: if statement to check if daytime is longer than night
    ##         for negative (clockPosition(planetaryHourDayLength) so display continues clockwise
         
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pI[1]), 
                                    outline="#000000", tags="hours",
                                    start =180+(theSunWasUp),
                                    end=(theSunWasUp -  (1*clockPositionNight(lastPlanetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pII[1]), 
                                    outline="#000000", tags="hours",
                                    start =(theSunWasUp - (1*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end =(theSunWasUp -  (2    *clockPositionNight(lastPlanetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIII[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (2*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (3*clockPositionNight(lastPlanetaryHourNightLength))))
            
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIV[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (3*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (4*clockPositionNight(lastPlanetaryHourNightLength))))
               
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pV[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (4*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (5*clockPositionNight(lastPlanetaryHourNightLength))))
            
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVI[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (5*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (6*clockPositionNight(lastPlanetaryHourNightLength))))
           
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVII[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (6*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (7*clockPositionNight(lastPlanetaryHourNightLength))))
           
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pVIII[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (7*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (8*clockPositionNight(lastPlanetaryHourNightLength))))
           
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pIX[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (8*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (9*clockPositionNight(lastPlanetaryHourNightLength))))
           
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pX[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (9*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (10*clockPositionNight(lastPlanetaryHourNightLength))))
           
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pXI[1]), 
                                     outline="#000000", tags="hours",
                                      start= (theSunWasUp -  (10*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (11*clockPositionNight(lastPlanetaryHourNightLength))))
           
            canvas.create_circle_arc(950, 500, 340, fill=planetaryColor(pXII[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunWasUp -  (11*clockPositionNight(lastPlanetaryHourNightLength))), 
                                     end=(theSunWasUp -  (12*clockPositionNight(lastPlanetaryHourNightLength))))
         
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
            
    ##         to do: if statement to check if daytime is longer than night
    ##         for negative (clockPosition(planetaryHourDayLength) so display continues clockwise
      
            canvas.create_circle_arc(950, 500, 320, 
                                     fill = planetaryColor(dI[0]), 
                                     outline ="#000000", tags="hours",
                                     start = (theSunIsUp),
                                     end = (theSunIsUp +  (clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 320, 
                                    fill=planetaryColor(dII[0]), 
                                    outline="#000000", tags="hours",
                                    start=(theSunIsUp +  (clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (2*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 320, 
                                    fill=planetaryColor(dIII[0]), 
                                    outline="#000000", tags="hours",
                                    start=(theSunIsUp +  (2*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (3*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 320, 
                                    fill=planetaryColor(dIV[0]), 
                                    outline="#000000", tags="hours",
                                    start=(theSunIsUp +  (3*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (4*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 320, 
                                    fill=planetaryColor(dV[0]), 
                                    outline="#000000", tags="hours",
                                    start=(theSunIsUp +  (4*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (5*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 320, 
                                     fill=planetaryColor(dVI[0]), 
                                     outline="#000000", tags="hours",
                                    start=(theSunIsUp +  (5*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (6*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 320, 
                                     fill=planetaryColor(dVII[0]), 
                                     outline="#000000", tags="hours",
                                     start=(theSunIsUp +  (6*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (7*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 320, 
                                     fill=planetaryColor(dVIII[0]), 
                                     outline="#000000", tags="hours",
                                     start=(theSunIsUp +  (7*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (8*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 320, 
                                     fill=planetaryColor(dIX[0]), 
                                     outline="#000000", tags="hours",
                                     start=(theSunIsUp +  (8*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (9*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 310, fill=planetaryColor(dX[0]), 
                                     outline="#000000", tags="hours",
                                     start=(theSunIsUp +  (9*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (10*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 310, fill=planetaryColor(dXI[0]), 
                                     outline="#000000", tags="hours",
                                     start=(theSunIsUp +  (10*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (11*clockPosition(planetaryHourDayLength))))
            canvas.create_circle_arc(950, 500, 300, fill=planetaryColor(dXII[0]), 
                                     outline="#000000", tags="hours",
                                     start=(theSunIsUp +  (11*clockPosition(planetaryHourDayLength))),
                                    end=(theSunIsUp +  (12*clockPosition(planetaryHourDayLength))))
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
    
    ##         to do: if statement to check if daytime is longer than night
    ##         for negative (clockPosition(planetaryHourDayLength) so display continues clockwise
             
            canvas.create_circle_arc(950, 500, 290, 
                                    fill=planetaryColor(I[1]), 
                                    outline="#000000", tags="hours",
                                    start = (theSunIsDown),
                                    end = (theSunIsDown -  (1*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                    fill=planetaryColor(II[1]), 
                                    outline="#000000", tags="hours",
                                    start = (theSunIsDown -  (1*clockPositionNight(planetaryHourNightLength))), 
                                    end = (theSunIsDown -  (2*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                    fill=planetaryColor(III[1]), 
                                    outline="#000000", tags="hours",
                                    start= (theSunIsDown -   (2*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -   (3*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                    fill=planetaryColor(IV[1]), 
                                    outline="#000000", tags="hours",
                                    start= (theSunIsDown -   (3*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -   (4*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                     fill=planetaryColor(V[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunIsDown -   (4*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -   (5*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                     fill=planetaryColor(VI[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunIsDown -   (5*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -   (6*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                     fill=planetaryColor(VII[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunIsDown -   (6*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -   (7*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                     fill=planetaryColor(VIII[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunIsDown -  (7*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -  (8*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                     fill=planetaryColor(IX[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunIsDown -  (8*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -  (9*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                     fill=planetaryColor(X[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunIsDown -   (9*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -   (10*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 290, 
                                     fill=planetaryColor(XI[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunIsDown -   (10*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -   (11*clockPositionNight(planetaryHourNightLength))))
            canvas.create_circle_arc(950, 500, 287, 
                                     fill=planetaryColor(XII[1]), 
                                     outline="#000000", tags="hours",
                                     start= (theSunIsDown -   (11*clockPositionNight(planetaryHourNightLength))), 
                                     end=(theSunIsDown -   (12*clockPositionNight(planetaryHourNightLength))))
    
        except:
            print "fookin' broke mate!"
