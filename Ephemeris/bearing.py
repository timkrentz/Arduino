# Package for getting the current location of the sun
# Requires PyEphem (ephem) and datetime (datetime) libraries
# Author: Tim Krentz
# June 22, 2015

import ephem
import datetime


####################################################################################################

# Method definition: GPS coord. defaults to lot outside PRL high bay
def getBearing(latitude=40.442947, longitude=-79.945108, elevation=269):
	"""getBearing returns a 2-element vector of (1) angle from North and (2) elevation from horizon"""

	# Create 'Observer' object in PyEphem call it 'curr'
	curr = ephem.Observer()

	# Assign observer's longitude, latitude, and elevation
	curr.lat = latitude
	curr.lon = longitude
	curr.elevation = elevation

	# Get datetime object in UTC time from datetime library, assign to observer object
	curr.date = datetime.datetime.utcnow()

	# Get angles from observer to the Sun
	b = ephem.Sun(curr)

	# Return the azimuth from North and the altitude above horizon to the Sun
	return [b.az, b.alt]


####################################################################################################


# Testbench code: runs if bearing.py is top-level
if __name__ == "__main__":
	
	# Get the current angles to sun from asphalt outside PRL highbay, and print them out
	temp = getBearing()
	print('The Sun is currently %s degrees from North and %s degrees above the horizon.' % (temp[0],temp[1]))
