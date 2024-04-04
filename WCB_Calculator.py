# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:06:36 2024

@author: Dan
"""
#Known coordinates, known location

#Calc WCB/AB, WCB/BA. A/B is from Point A to B
#WCB = Angle from North clockwise toward Line AB

import math

class PointA:
    E = 258.971
    N = 490.856
    
class PointB:
    E = 276.722
    N = 523.555

#Calculate Deltas

DEab = PointB.E - PointA.E
DNab = PointB.N - PointA.N

#Calculate Quadrant Bearing QAB
QBab = math.atan(abs(DEab)/abs(DNab))

#print(degrees, minutes, seconds)

if DEab > 0 and DNab > 0:
    WCBab = QBab
elif DEab > 0 and DNab < 0:
    WCBab = 3.14159 - QBab
elif DEab < 0 and DNab < 0:
    WCBab = 3.14159 + QBab
elif DEab < 0 and DNab > 0:
    WCBab = 6.28319 - QBab

if WCBab < 3.14159 :
    WCBba = WCBab + 3.14159
else:
    WCBba = WCBab - 3.14159

ABdegrees = round(WCBab * 180/(math.pi), 3)
ABminutes = round((ABdegrees % 1) * 60, 3)
ABseconds = round((ABminutes % 1) * 60, 3)

BAdegrees = round(WCBba * 180/(math.pi), 3)
BAminutes = round((BAdegrees % 1) * 60, 3)
BAseconds = round((BAminutes % 1) * 60, 3)

print("WCB AB is: ", ABdegrees, "°", ABminutes, "'", ABseconds, "\"")
print("WCB BA is: ", BAdegrees, "°", BAminutes, "'",  BAseconds, "\"")