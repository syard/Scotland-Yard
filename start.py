# -*- coding: cp1252 -*-
#/usr/bin/env python
#Simon H. Larsen
#Buttons.py - example
#Project startet: d. 28. august 2012
#Import pygame modules and Buttons.py(it must be in same dir)
print("HI")
import pygame, Buttons
from pygame.locals import *

#Initialize pygame
pygame.init()
print("HI2")
class Button_Example:
    def __init__(self):
        self.main()
    print("HI3")
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((1025,770),0,32)
        #Displaysurf = self.screen.convert_alpha()
        pygame.display.set_caption("Start Game")
        #DISPLAYSURF = pygame.display.set_mode((1025, 770))
        mapImg=pygame.image.load('cover.PNG')
        mapImg=pygame.transform.scale(mapImg, (1025, 770))
        self.screen.blit(mapImg, (0, 0))
        #self.screen.blit(Displaysurf,(0,0))
    print("HI4")
    #Update the display and show the button
    def update_display(self):
        #self.screen.fill((30,144,255))
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen.convert_alpha(), (1,142,35), 523, 397, 105,    48,    40,        "hi", (255,255,255))
        self.Button2.create_button(self.screen.convert_alpha(), (1,142,35), 534, 612, 146,    37,    40,        "hi", (255,255,255))
        self.Button3.create_button(self.screen.convert_alpha(), (1,142,35), 387, 609, 109,    41,    40,        "hi", (255,255,255))
        self.Button4.create_button(self.screen.convert_alpha(), (1,142,35), 342, 533, 151,    50,    40,        "hi", (255,255,255))
        self.Button5.create_button(self.screen.convert_alpha(), (1,142,35), 533, 539, 234,    43,    40,        "hi", (255,255,255)) 
        self.Button6.create_button(self.screen.convert_alpha(), (1,142,35), 536, 465, 169,    48,    40,        "hi", (255,255,255))
        self.Button7.create_button(self.screen.convert_alpha(), (1,142,35), 235, 466, 255,    47,    40,        "hi", (255,255,255)) 
        pygame.display.flip()

    print("HI5")
    #Run the loop
    def main(self):
        print("HI6")
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
        self.Button3 = Buttons.Button()
        self.Button4 = Buttons.Button()
        self.Button5 = Buttons.Button()
        self.Button6 = Buttons.Button()
        self.Button7 = Buttons.Button()
        self.display()
        print("HI")

        while True:
            self.update_display()
            #mapImg=pygame.image.load('cover.PNG')
            #mapImg=pygame.transform.scale(mapImg, (1025, 770))
            #self.screen.blit(mapImg, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        print "START"
                        import testmap.py
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        print "TUTORIAL"
                        
                    if self.Button3.pressed(pygame.mouse.get_pos()):
                        print "RULES"
                        
                    if self.Button4.pressed(pygame.mouse.get_pos()):
                        print "OPTIONS"
                    if self.Button5.pressed(pygame.mouse.get_pos()):
                        print "MORE GAMES"
                    if self.Button6.pressed(pygame.mouse.get_pos()):
                        print "STATISTICS"
                    if self.Button7.pressed(pygame.mouse.get_pos()):
                        print "ACHIEVEMENTS"
if True:
 #if __name__ == '__main__':
    obj = Button_Example()
