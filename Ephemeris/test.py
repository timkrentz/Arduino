#Experimental Code for learning to use the PyEphem library
#PyEphem is used for ephemeris calculations
#The goal is to use this in designing the Sun Sensor

import ephem

#U = ephem.Uranus()
#print('%s' % (U.name))

cmu = ephem.Observer()
cmu.lat = 40.2634501
cmu.lon = -79.5642191
cmu.elevation = 289
cmu.date = '2015/6/19 18:51:00'

S = ephem.Sun(cmu)
print('%s %s' % (S.az, S.alt))







