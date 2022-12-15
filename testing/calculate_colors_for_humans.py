import time
red_port = 7
green_port = 29
blue_port = 31
delay_speed = 10


red = 255
green = 0
blue = 0
ds = 0

color_output = []

while not (red == 255 and blue==1):
    #time.sleep(0.1)


    red_hex = hex(red)[2:]
    green_hex = hex(green)[2:]
    blue_hex = hex(blue)[2:]
    if len(red_hex) ==1:red_hex = "0" + red_hex
    if len(green_hex) ==1:green_hex = "0" + green_hex
    if len(blue_hex) ==1:blue_hex = "0" + blue_hex
    
    print("#" + red_hex + green_hex + blue_hex)
    #green coming up more slowly
    if(red==255 and green != 255 and blue == 0 and ds==0):
        green += 1
    #red coming out more slowly
    if(green == 255 and red != 0 and blue == 0 and ds==0):
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

    ds += 1
    
    if(ds == delay_speed):
        ds = 0
    
    




        
    port_list_in_progress = []
    brightness_list_in_progress = []
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
    #maybe should be indented
    port_list = port_list_in_progress
    brightness_list = brightness_list_in_progress

    color_output.append({"value_list": brightness_list, "port_list": port_list})
print(len(color_output))
file = open("color-output.txt", "w")
file.write("master_color = " + str(color_output))
file.close()
