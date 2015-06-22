# Tim Krentz

import bearing

angles = bearing.getBearing()

print('Sun is currently %s degrees from North and %s degrees above horizon.' % (angles[0],angles[1]))

