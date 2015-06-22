#Experimental Code for learning to use the PyEphem library
#PyEphem is used for ephemeris calculations
#The goal is to use this in designing the Sun Sensor
# Tim Krentz
# June 21, 2015


import ephem
import datetime

t = datetime.datetime.utcnow()


cmu = ephem.Observer()
cmu.lat = 40.442947
cmu.lon = -79.945108
cmu.elevation = 269
cmu.date = t 


S = ephem.Sun(cmu)
print('%s %s' % (S.az, S.alt))







