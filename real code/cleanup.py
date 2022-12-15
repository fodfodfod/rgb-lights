import RPi.GPIO as GPIO
import os



red_port = 7
green_port = 29
blue_port = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_port,GPIO.OUT)
GPIO.setup(green_port,GPIO.OUT)
GPIO.setup(blue_port,GPIO.OUT)

GPIO.cleanup()
os.system("pkill -9 python3")

