#NEEDS ANOTHER FILE TO RUN run_display()

def run_display():

    # from threading import Thread
    import RPi.GPIO as GPIO
    import time
    import asyncio
    import master_color

    #GPIO.output(7, True)
    #time.sleep()


    master_colors = master_color.master_color

    red = 255

    green = 0

    blue = 0

    red_port = 7
    green_port = 29
    blue_port = 31



    brightness_list = []
    port_list = []



    flash_speed = 100000

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(red_port,GPIO.OUT)
    GPIO.setup(green_port,GPIO.OUT)
    GPIO.setup(blue_port,GPIO.OUT)

    i = 0
    brightness_mult = 0.0
    
    print("display created")
    while True:
        color_id = int(time.time()*50)%len(master_colors)
        brightness_list = list(map(lambda x: x * brightness_mult, master_colors[color_id]["value_list"]))
        port_list = master_colors[color_id]["port_list"]


        for color in range(0, 3):
            if master_colors[color_id]["value_list"][color] != 0:
                GPIO.output(master_colors[color_id]["port_list"][color], True)

        #print(str(brightness_list) + "hi")
        time.sleep(brightness_list[0]/flash_speed)
        GPIO.output(port_list[0], False)
        time.sleep(brightness_list[1]/flash_speed)
        GPIO.output(port_list[1], False)
        time.sleep(brightness_list[2]/flash_speed)
        GPIO.output(port_list[2], False)
        time.sleep((256 - brightness_list[0] - brightness_list[1] - brightness_list[2])/flash_speed)
        i= i + 1
        if(brightness_mult < 256.0):
            brightness_mult = brightness_mult + 1.0
        else:
            print("done getting brighter")

# run_display()
# GPIO.cleanup()
