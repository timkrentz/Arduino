# Example use of the time library in getting the current UTC
# Relies on the host operating system to have the correct time
# Author: Tim Krentz
# June 22, 2015

import time

current = time.time()
print('Number of seconds since epoch: %d' % current)

utcTime = time.gmtime(current)
print(utcTime)
