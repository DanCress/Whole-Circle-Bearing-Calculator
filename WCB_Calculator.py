##############################################################
# Simple calculator of whole circle bearings,                #
# based on two points A and B,                               #
# each with a respective Easting (m) and Northing (m) value  #
##############################################################

#WCB = Angle from North clockwise toward Line AB

import math

class PointA:
    E = 258.971 #USER INPUT POINT A Easting here
    N = 490.856 #USER INPUT Point A Northing here
    
class PointB:
    E = 276.722 #USER INPUT Point B Easting here
    N = 523.555 #USER INPUT Point B Northing here

#Calculate Deltas (Point B - Point A)

DE = PointB.E - PointA.E
DN = PointB.N - PointA.N

#Calculate Quadrant Bearing QAB

QBab = math.atan(abs(DE)/abs(DN))

if DE > 0 and DN > 0: # B - A, DE = 270 - 260, DN = 520 - 510
    WCBab = QBab
elif DE > 0 and DN < 0: # B - A, DE = 270 - 260, DN = 510 - 520
    WCBab = 3.14159 - QBab
elif DE < 0 and DN < 0: # B - A, DE = 260 - 270, DN = 520 - 510
    WCBab = 3.14159 + QBab 
elif DE < 0 and DN > 0: # B - A, DE = 260 - 270, DN = 520 - 510
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

distance = round(((PointB.E - PointA.E)**2 + (PointB.N - PointA.N)**2)**0.5, 3) #** to the power of

print("WCB AB is: ", ABdegrees, "°", ABminutes, "'", ABseconds, "\"")
print("WCB BA is: ", BAdegrees, "°", BAminutes, "'",  BAseconds, "\"")
print("The distance is: ", distance, "m")