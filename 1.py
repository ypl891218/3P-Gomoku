import pygame
from pygame.locals import *


displayHeight = 1024
displayWidth = 1530
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
backgroundPosX = 0
backgroundPosY = 0
 
gameExit = False
##while not gameExit:
       
backgroundImage1 = pygame.image.load('Blank_Go_board.png').convert_alpha()
backgroundImage2 = pygame.image.load('frame.png').convert_alpha()
backgroundImage1 = pygame.transform.scale(backgroundImage1, (590, 590))
backgroundImage2 = pygame.transform.scale(backgroundImage2, (300, 300))
for i in range(10):
	gameDisplay.blit(backgroundImage1, [backgroundPosX, backgroundPosY])
	gameDisplay.blit(backgroundImage2, [backgroundPosX+i*10, backgroundPosY])
	pygame.time.delay(100)
	pygame.display.update()

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == MOUSEBUTTONDOWN:
			gameExit = True