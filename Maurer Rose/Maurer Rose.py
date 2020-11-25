import sys
import pygame
import random
import math as m
from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier
from pygame.locals import *

#Colors
white = [255,255,255]
black = [0,0,0]
red = [206, 32, 41]
green = [0,155,0]
yellow = [255, 225, 124]
orange = [255, 102, 75]
brick = [144, 56, 67]
skin = [255, 252, 175]
lime = [0,255,0]
blue = [0,0,204]
pink = [255,0,127]

colors = [red,green,yellow,orange,brick,skin,lime,blue,pink]

# this code only needs to be ran once
pygame.init()
width = int(1400/2)
height = int(800/2)
window = pygame.display.set_mode((int(width*2),int(height*2)),RESIZABLE)
clock = pygame.time.Clock()
FPS = 240

#Assigning Variables
x = 0
y = 0
r = 0
n = 6
d = 71


while True:
    #allows user to exit the screen
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
           
    window.fill(black)  
    
    for i in range (50*361):
    	k = i * d
    	r = 500 * m.sin(n * k)
    	x = r * m.cos(k)
    	y = r * m.sin(k)
    	#pygame.draw.circle(window,white,(int(x+width),int(y+height)),2)
    	pygame.draw.line(window,white,(int(width),int(height)),(int(x+width),int(y+height)))
           
    #Background.set_alpha(25)
    #Background.fill(black)           
    #window.blit(Background, (0,0))
	
	


        
    pygame.display.update()
    clock.tick(FPS)

































