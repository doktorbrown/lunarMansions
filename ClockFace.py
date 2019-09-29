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



class ClockFace():
        
    def __init__(self):
        self.ClockFace = []
        
    def display(self,canvas):
    #    canvas.delete("all")#deletes left side info
        
            #offset 90 moves Aries 0 to 12 o'clock  position
    #     offSet = 0
    #     offSet = 90
        offSet = -90 
           
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
    # planet positions would be needed here if it 
    # is to continue to be part of clockface for stacking 
      
#         canvas.create_circle_arc(950, 500, 495, fill="#8b0000", outline="black", start=plPo-0+offSet, end=plPo+0+offSet)
#         canvas.create_circle_arc(950, 500, 495, fill="#006400", outline="black", start=urPo-0+offSet, end=urPo+0+offSet)
#         canvas.create_circle_arc(950, 500, 495, fill="blue", outline="black", start=nePo-0+offSet, end=nePo+0+offSet)
#         canvas.create_circle_arc(950, 500, 495, fill="#8A2BE2", outline="black", start=saPo-0+offSet, end=saPo+0+offSet)
#         canvas.create_circle_arc(950, 500, 495, fill="#EE82EE", outline="black", start=juPo-0+offSet, end=juPo+0+offSet)
#         canvas.create_circle_arc(950, 500, 495, fill="#FF0000", outline="black", start=maPo-0+offSet, end=maPo+0+offSet)
#         canvas.create_circle_arc(950, 500, 495, fill="#FFA500", outline="black", start=soPo-0+offSet, end=soPo+0+offSet)
#         canvas.create_circle_arc(950, 500, 495, fill="#008000", outline="black", start=vePo-0+offSet, end=vePo+0+offSet)
#         canvas.create_circle_arc(950, 500, 495, fill="#FFFF00", outline="black", start=mePo-0+offSet, end=mePo+0+offSet)     
#         canvas.create_circle_arc(950, 500, 495, fill="#c0c0c0", outline="black", start=moPo-0+offSet, end=moPo+0+offSet)
#      
         
     # planet positions would be needed here if it 
    # is to continue to be part of clockface for stacking        
        
        #backround cover
#         canvas.create_circle(950, 500, 275, fill="white", outline="white", width=10)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=moPo-5+offSet, end=moPo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=mePo-5+offSet, end=mePo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=vePo-5+offSet, end=vePo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=soPo-5+offSet, end=soPo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=maPo-5+offSet, end=maPo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=juPo-5+offSet, end=juPo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=saPo-5+offSet, end=saPo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=nePo-5+offSet, end=nePo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=urPo-5+offSet, end=urPo+offSet)
#         canvas.create_circle_arc(950, 500, 380, fill="white", outline="white", start=plPo-5+offSet, end=plPo+offSet)
#     
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
