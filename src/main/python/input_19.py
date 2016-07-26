import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(19,gpio.IN,pull_up_down=gpio.PUD_DOWN)
gpio.input(19)
