import random, pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1025, 770))
mapImg=pygame.image.load('cover.PNG')
mapImg=pygame.transform.scale(mapImg, (1025, 770))
DISPLAYSURF.blit(mapImg, (0, 0))
pygame.display.set_caption('Scotland Yard')


while True: # main game loop

 for event in pygame.event.get():
  if event.type == QUIT:
   pygame.quit()
   sys.exit()
  elif event.type == MOUSEBUTTONDOWN:
    #if self.Button1.pressed(pygame.mouse.get_pos()):
         print pygame.mouse.get_pos()
 pygame.display.update()
