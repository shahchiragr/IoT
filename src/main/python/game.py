#import necessary libraries
import RPi.GPIO as gp,random, time

#set variable for easy pin reference
switchR = 19	#red switch
switchB = 26	#blue switch
ledR = 13
ledG = 6
ledB = 5

#initialize GPIO pins
gp.setmode(gp.BCM)
gp.setup(switchR, gp.IN, pull_up_down=gp.PUD_DOWN)
gp.setup(switchB, gp.IN, pull_up_down=gp.PUD_DOWN)
gp.setup([ledR,ledG,ledB],gp.OUT)

#define a function to monitor switches
def monitorSwitches(seconds):
	#loop for specified time; checking for switch press
	timeEnd = time.time() + seconds
	while time.time() < timeEnd:
		if gp.input(switchR) == True:
			return announceWinner(switchR)
		if gp.input(switchB) == True:
			return announceWinner(switchB)
	return False

# define a function to announce the Winner
def announceWinner(switch):
	#define witch button was press first
	firstBtn = ledR if switch == switchR else ledB
	lastBtn = ledB if switch == switchR else ledR

	#determin witch player won
	winner = firstBtn if ledColor == ledG else lastBtn
	
	#turn off active color and falsh winnin color
	gp.output(ledColor, False)
	
	for i in range(0,10):
		gp.output(winner,True)
		time.sleep(0.5)
		gp.output(winner,False)
		time.sleep(0.5)

#play the game, loop until a switch pressed
winner = False
while winner == False:
	#select random Led color
	ledColor = random.choice([ledR,ledG,ledB])

	#play through one color style

	gp.output(ledColor, True) # turn on LED
	winner = monitorSwitches(5) #monitor switches
	gp.output(ledColor, False) # turn off LED

gp.cleanup()



