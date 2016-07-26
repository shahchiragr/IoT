#import necessary libraries

import RPi.GPIO as gp,time

#set variables for easy reference
photoPin = 21
ledPin = 22
threshold = 0.01 # measured in seconds

#initialize GPIO pins
gp.setmode(gp.BCM)
gp.setup(ledPin, gp.OUT)

#define a function measure fill time

def measureFillTime(pin):
	#discharge the capacitor (empty the bucket)
	gp.setup(pin, gp.OUT)
	gp.output(pin,False)
	time.sleep(0.1)

	#fill capacitor and measure time
	timeStart = time.time()
	gp.setup(pin,gp.IN)
	while (gp.input(pin) == False):
		pass
	return time.time() - timeStart

#run for one minute, then cleanup
timeEnd = time.time() + 60
while time.time() < timeEnd:
	fillTime = measureFillTime(photoPin)
	
	#turn on LED if fillTime  greater than threshold
	if fillTime > threshold:
		print "dark, fillTime:",fillTime
	else:
		print "light fillTime:",fillTime
		gp.output(ledPin,False)

gp.cleanup()
	