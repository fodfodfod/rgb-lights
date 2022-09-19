from threading import Thread
import RPi.GPIO as GPIO
import time

#GPIO.output(7, True)
#time.sleep()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

brightness = 0

def brightness_controller_function():
    
    while True:
        print(brightness)
        GPIO.output(7, True)
        time.sleep(brightness/10000)

        GPIO.output(7, False)
        time.sleep((100 - brightness)/10000)
        
    
# GPIO.output(7, True)
# time.sleep(2)

brightness_controller_thread = Thread(target=brightness_controller_function)

brightness_controller_thread.run()

for i in range(0, 101):
    
    brightness += 1
    time.sleep(0.1)
    


GPIO.cleanup()