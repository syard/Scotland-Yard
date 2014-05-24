# -*- coding: cp1252 -*-
#/usr/bin/env python
#Simon H. Larsen
#Buttons.py - example
#Project startet: d. 28. august 2012
#Import pygame modules and Buttons.py(it must be in same dir)
import pygame, Buttons
from pygame.locals import *

#Initialize pygame
pygame.init()

class Button_Example:
    def __init__(self):
        self.main()
    
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((1800,770))
        #Displaysurf = self.screen.convert_alpha()
        pygame.display.set_caption("Scotland Yard!")
        #DISPLAYSURF = pygame.display.set_mode((1025, 770))
        mapImg=pygame.image.load('map.jpg')
        mapImg=pygame.transform.scale(mapImg, (1018, 750))
        self.screen.blit(mapImg, (0, 0))
        #self.screen.blit(Displaysurf,(0,0))

    #Update the display and show the button
    def update_display(self):
        #self.screen.fill((30,144,255))
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, (255,0,0), 1023, 680, 200,    100,    0,        "BACK", (255,255,255))
        pygame.display.flip()


    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        #print "Give me a command!"
                        import start
if True:                            
#if __name__ == '__main__':
    obj = Button_Example()
