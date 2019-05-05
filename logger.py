'''
Created on May 5, 2019

@author: zaremba
'''

import time

class Logger(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print "Logger.__init__"
        
    def logMsg(self, msg):
        
        now = time.clock()
        print repr(now) + " " + msg