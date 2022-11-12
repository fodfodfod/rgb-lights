# from threading import Thread
import RPi.GPIO as GPIO
import time
import asyncio

#GPIO.output(7, True)
#time.sleep()


red = 255

green = 0

blue = 0



brightness_list = []
port_list = []


red_port = 7
green_port = 29
blue_port = 31

flash_speed = 10000

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_port,GPIO.OUT)
GPIO.setup(green_port,GPIO.OUT)
GPIO.setup(blue_port,GPIO.OUT)

async def find_next_color():
    print("finding next color")
    global red
    global blue
    global green
    
    red_hex = hex(red)[2:]
    green_hex = hex(green)[2:]
    blue_hex = hex(blue)[2:]
    if len(red_hex) ==1:red_hex = "0" + red_hex
    if len(green_hex) ==1:green_hex = "0" + green_hex
    if len(blue_hex) ==1:blue_hex = "0" + blue_hex
    
    print("#" + red_hex + green_hex + blue_hex)
    
    

    #green coming up
    if(red==255 and green != 255 and blue == 0):
        green += 1
    #red coming out
    if(green == 255 and red != 0 and blue == 0):
        red -= 1
    
    #green == 255 and red == 0 blue != 255
    #blue coming in
    if(green == 255 and red == 0 and blue != 255):
        blue += 1
    #green going out
    if(blue == 255 and green != 0 and red == 0):
        green -= 1
    
    # red coming in
    if(blue == 255 and green == 0 and red != 255):
        red += 1
    #blue going out
    if(blue != 0 and red == 255 and green == 0):
        blue -= 1

async def update_display():
    
    port_list_in_progress = []
    brightness_list_in_progress = []
    global red
    global blue
    global green
    # print(f"updating display with {red}, {green}, {blue}")
    red_copy = red
    blue_copy = blue
    green_copy=green
    for i in range(1, 7):
        

        if(red_copy <= green_copy and red_copy<=blue_copy and red_copy < 300):
            
            port_list_in_progress.append(red_port)
            subtract_time = 0
            for i in range(0, len(brightness_list_in_progress)):
                subtract_time += brightness_list_in_progress[i]
            red_copy -= subtract_time
            brightness_list_in_progress.append(red_copy)
            red_copy = 300
        
        if(green_copy <= red_copy and green_copy<=blue_copy and green_copy < 300):
            
            port_list_in_progress.append(green_port)
            subtract_time = 0
            for i in range(0, len(brightness_list_in_progress)):
                subtract_time += brightness_list_in_progress[i]
            green_copy-= subtract_time
            brightness_list_in_progress.append(green_copy)
            green_copy = 300
        
        if(blue_copy <= green_copy and blue_copy<=red_copy and blue_copy < 300):

            port_list_in_progress.append(blue_port)
            subtract_time = 0
            for i in range(0, len(brightness_list_in_progress)):
                subtract_time += brightness_list_in_progress[i]
            blue_copy -= subtract_time
            brightness_list_in_progress.append(blue_copy)
            blue_copy = 300
        global port_list
        global brightness_list
        port_list = port_list_in_progress
        brightness_list = brightness_list_in_progress
async def run_display():
    print("display created")
    while True:
        GPIO.output(red_port, True)
        GPIO.output(green_port, True)
        GPIO.output(blue_port, True)

        
        global brightness_list
        print(str(brightness_list) + "hi")
        time.sleep(brightness_list[0]/flash_speed)
        GPIO.output(port_list[0], False)
        time.sleep(brightness_list[1]/flash_speed)
        GPIO.output(port_list[1], False)
        time.sleep(brightness_list[2]/flash_speed)
        GPIO.output(port_list[2], False)        

async def main():
    # background_tasks = set()
    run_display_task = asyncio.create_task(run_display())
    # background_tasks.add(run_display_task)

    # await run_display()
    
    # print("pre sleep")
    # await asyncio.sleep(1)
    print("start loop")
    while 1 == 1:
        
        find_next_color_task = asyncio.create_task(find_next_color())
        await find_next_color_task

        # asyncio.run(find_next_color())

        # await find_next_color()

        update_display_task = asyncio.create_task(update_display())
        await update_display_task

        # await update_display()
        time.sleep(0.005)
        
        # print("done display")
    await run_display_task

asyncio.run(update_display())

asyncio.run(main())

GPIO.cleanup()