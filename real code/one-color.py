import RPi.GPIO as GPIO
import time

#GPIO.output(7, True)
#time.sleep()


red = 0
green = 255
blue = 0

red_port = 7
green_port = 29
blue_port = 31

flash_speed = 10000

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_port,GPIO.OUT)
GPIO.setup(green_port,GPIO.OUT)
GPIO.setup(blue_port,GPIO.OUT)

port_list = []
brightness_list = []

red_copy = red
blue_copy = blue
green_copy=green
for i in range(1, 7):
    

    if(red_copy <= green_copy and red_copy<=blue_copy and red_copy < 300):
        
        port_list.append(red_port)
        subtract_time = 0
        for i in range(0, len(brightness_list)):
            subtract_time += brightness_list[i]
        red_copy -= subtract_time
        brightness_list.append(red_copy)
        red_copy = 300
    
    if(green_copy <= red_copy and green_copy<=blue_copy and green_copy < 300):
        
        port_list.append(green_port)
        subtract_time = 0
        for i in range(0, len(brightness_list)):
            subtract_time += brightness_list[i]
        green_copy-= subtract_time
        brightness_list.append(green_copy)
        green_copy = 300
    
    if(blue_copy <= green_copy and blue_copy<=red_copy and blue_copy < 300):
        print("blue add")
        port_list.append(blue_port)
        subtract_time = 0
        for i in range(0, len(brightness_list)):
            subtract_time += brightness_list[i]
        blue_copy -= subtract_time
        brightness_list.append(blue_copy)
        blue_copy = 300

while True:
    GPIO.output(red_port, True)
    GPIO.output(green_port, True)
    GPIO.output(blue_port, True)

    

    time.sleep(brightness_list[0]/flash_speed)
    GPIO.output(port_list[0], False)
    time.sleep(brightness_list[1]/flash_speed)
    GPIO.output(port_list[1], False)
    time.sleep(brightness_list[2]/flash_speed)
    GPIO.output(port_list[2], False)        


        


GPIO.cleanup()