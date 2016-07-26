import RPi.GPIO as gp,random, time
gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup([5,6,13],gp.OUT)
gp.output(13,False)
gp.output(5,False)
gp.output(6,False)
gp.cleanup()
exit()
