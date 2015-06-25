# Package for reading Acceleromter->Arduino setup
# Author: Tim Krentz
# Created Friday, June 16, 2015

import serial
import math

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
		timeOut = 200
		while timeOut > 0:
			timeOut -= 1

			#Send request byte to Arduino
			self.ser.write(chr(0x5A))

			#Check if data is available on serial line, otherwise re-loop
			if self.ser.inWaiting() <= 0:
				continue

			#Read string from serial
			self.stringIn = self.ser.readline()
	
			#Split string by spaces into x, y, and z components
			self.dataOut = self.stringIn.split()

			#Ensure that the string was split into three parts
			if len(self.dataOut) != 3:
				print('ERROR: LENGTH')
				continue

			#Attempt to convert each of the three sub-strings into integers
			#Important because sometimes serial returns sub-strings like '-4-56'
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
			return [0,0,0]			#This could be improved with actual
							#error handeling
		else:
			phi = math.degrees(math.atan2(self.dataOut[2],math.hypot(self.dataOut[0],self.dataOut[1])))
			theta = math.degrees(math.atan2(self.dataOut[1],self.dataOut[0]))
			return [theta,phi]
			
 
		
###############################################################################################


#Testbench code, runs if top-level
if __name__ == "__main__":
	
	#Create accelerometer object
	accel =	accelerometer()

	#Read a force vector from accelerometer
	angs = accel.getVector()
	print('Current force vector: ',angs)

