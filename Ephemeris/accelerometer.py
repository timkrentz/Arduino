# Package for reading Acceleromter->Arduino setup
# Author: Tim Krentz
# Created Friday, June 16, 2015

import serial


	#Accelerometer creation function, creates and returns serial object
	#Required: port name and buadrate
	#Assumes 8 bits, no parity, 1 stop bit
	def create(port='/dev/ttyACM0', baudrate=115200):
		return serial.Serial(port, baudrate)


	#Read 'num' bytes from accelerometer object, defaults to 1 if not specified
	#self.readline should read until \n character, but it only reads one byte
	#fix this...
	def getVector():
		data = []			#Blank array
		while True:
			temp_char = self.read()
			if (temp_char == '\n'):
				print('Breaking...')
				break
			data.append(temp_char)
		return data








#Testbench code, runs if top-level
if __name__ == "__main__":
	
	#Create accelerometer object
	accel =	create('/dev/ttyACM0', 115200)

	#Read 50 bytes from serial stream
	print('Running...')
	print('%s' % accel.getVector())

