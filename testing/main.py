import pygame

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
fps = 200

red = 255
green = 0
blue = 0


run = True
while run:
    clock.tick(fps)
    red_hex = hex(red)[2:]
    green_hex = hex(green)[2:]
    blue_hex = hex(blue)[2:]
    if len(red_hex) ==1:red_hex = "0" + red_hex
    if len(green_hex) ==1:green_hex = "0" + green_hex
    if len(blue_hex) ==1:blue_hex = "0" + blue_hex
    
    # print("#" + red_hex + green_hex + blue_hex)
    screen.fill("#" + red_hex + green_hex + blue_hex)
    pygame.display.update()
    
    # #red going to green
    # if(red == 255 or (red > 0 and green > 0)):
    #     red-=1
    #     green += 1
    
    # #green going to blue
    # elif(green == 255 or (green > 0 and blue > 0)):
    #     green-=1
    #     blue += 1
    
    # #blue going to red
    # elif(blue == 255 or (blue > 0 and red > 0)):
    #     blue-=1
    #     red += 1

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
        