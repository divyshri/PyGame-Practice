import pygame,sys

from pygame.locals import *

pygame.init()

DisplaySurface = pygame.display.set_mode((500,500),0,32)

#Colors
Black = [0,0,0]
White = [255,255,255]
Red = [255,0,0]
Green = [0,255,0]
Blue = [0,0,255]

DisplaySurface.fill(White)

pygame.draw.polygon(DisplaySurface,Red,((146,0),(291,106),(205,60),(65,251)),5)
pygame.draw.line(DisplaySurface,Green,(100,200),(300,400),10)
pygame.draw.circle(DisplaySurface,Blue,(250,250),50,5)
pygame.draw.rect(DisplaySurface,Green,(200,150,50,100))
'''
pixObj = pygame.PixelArray(DisplaySurface)
pixObj[380][280] = Black
pixObj[382][282] = Black
pixObj[384][284] = Black
pixObj[386][286] = Black
pixObj[388][288] = Black
del pixObj
'''
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

