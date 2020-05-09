import pygame, sys, os
from pygame.locals import *

catx = 10
caty = 10
screen = 0

def myQuit():
	pygame.quit()
	sys.exit(0)

def check_inputs(events):
	global catx,caty,screen

	for event in events:
		if event.type == QUIT:
			quit()
		else:
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					myQuit()
				elif event.key == K_LEFT or event.key == K_a:
					catx -= 5
					print("maove Rectangle Left")
				elif event.key == K_RIGHT or event.key == K_d:
					catx += 5
					print("Move Rectangle Right")
				elif event.key == K_UP or event.key == K_w:
					caty -= 5
					print("Move Rectangle UP")
				elif event.key == K_DOWN or event.key == K_s:
					caty += 5
					print("Move Rectangle Down")
				else:
					print(event.key)
	screen.fill((0,0,0))
	pygame.draw.rect(screen,(255,255,255),(catx,caty,50,100))
	pygame.display.update()



def main():
	global screen
	pygame.init()
	window = pygame.display.set_mode((600,600))
	pygame.display.set_caption('KeyBoard Move')
	screen  = pygame.display.get_surface()
	pygame.display.update()
	
	while True:
		check_inputs(pygame.event.get())


main()
