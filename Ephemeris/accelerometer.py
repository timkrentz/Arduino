# Package for reading Acceleromter->Arduino setup
# Author: Tim Krentz
# Created Friday, June 16, 2015

import serial

class accelerometer:
	"""A class for the H48C accelerometer + Arduino"""

###############################################################################################

	#Accelerometer initialization function, creates and returns accelerometer object
	#Can accept port name and buadrate
	#Assumes 8 bits, no parity, 1 stop bit
	def __init__(self, port='/dev/ttyACM0', baudrate=115200):

		#Open serial port, assign to 'ser'
		self.ser = serial.Serial(port, baudrate)


###############################################################################################


	#Method to return an int-type vector of X, Y, and Z acceleration forces
	def getVector(self):
		
		#Create temporary variables
		self.stringIn = ''
		self.dataOut = []

		#Try 'timeOut' times to read from serial
		timeOut = 10
		while timeOut > 0:
			timeOut -= 1

			#Read string from Serial
			self.stringIn = self.ser.readline()
	
			#Split string by spaces into x, y, and z components
			self.dataOut = self.stringIn.split()

			#Ensure that the string was split into three parts
			if len(self.dataOut) != 3:
				print('ERROR: LENGTH')
				continue

			#Attempt to convert each of the three sub-strings into integers
			try:
				self.dataOut = map(int, self.dataOut)
				break
			except ValueError:
				print('ERROR: OBFUSCATION')
				continue

			#At this point, all criteria for good string are passed...
			#so break out of WHILE
			break

		#This bit prints to console if no good string was read
		if timeOut <= 0:
			print('ERROR: TIMEOUT')
			return [0,0,0]
		else:
			return self.dataOut
		
###############################################################################################


#Testbench code, runs if top-level
if __name__ == "__main__":
	
	#Create accelerometer object
	accel =	accelerometer()

	#Read bytes from serial stream
	print('Running...')
	ints = accel.getVector()
	print(ints)
	
