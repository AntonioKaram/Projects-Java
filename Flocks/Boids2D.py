import sys
import pygame
import random
import math as m
from OpenGL.GL import *
from OpenGL.GLU import *
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

#Initiation
pygame.init()
width = 1400
height = 800
window = pygame.display.set_mode((width,height),RESIZABLE)
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont('Helvetica',22)

#Scaling Variables
velocity = random.choice(range(-12,-10))

#Environmental Variables
flock = []
size = 8
numBoids = 100

#Background
Background = pygame.Surface((width,height))                 
Background.fill(black)           
window.blit(Background, (0,0))


class Boid:
    def __init__(self,x,y):
        self.pos = pygame.math.Vector2(random.choice(range(width)),random.choice(range(height)))
        self.vel = pygame.math.Vector2(random.uniform(-2,2),random.uniform(-2,2))
        self.vel *= random.choice(range(2,4))
        self.acc = pygame.math.Vector2(0,0)
        self.maxForceAlign = 1.5
        self.maxForceCohesion = 1.5
        self.maxForceSeperation = 3
        self.maxSpeed = 15;
        self.alignPerception = 50
        self.cohesionPerception = 200
        self.seperationPerception = 50
          
    def edges(self):
    	if (self.pos.x>width):
    		self.pos.x = 0
    	
    	elif (self.pos.x <0):
    		self.pos.x = width
    	
    	if (self.pos.y > height-50):
    		self.pos.y=0
    	
    	elif (self.pos.y < 0):
    		self.pos.y = height-50
          
    def align(self,boids):
    	perceptionRadius = self.alignPerception
    	steering =  pygame.math.Vector2()
    	total = 0
    	d= 0
    	
    	for i in range(len(boids)):
    		d = m.sqrt(((self.pos.x - boids[i].pos.x)**2) + ((self.pos.y - boids[i].pos.y)**2))
    		
    		if boids[i] != self and d < perceptionRadius:
    		 	steering += boids[i].vel
    		 	total += 1
    		 	
    	if total >0:
    		steering = steering / total
    		steering.scale_to_length(self.maxSpeed) 
    		steering -= self.vel
    		
    		if steering.length()<self.maxForceAlign:
    			steering = steering
    		elif steering.length()>=self.maxForceAlign:
    			steering.scale_to_length(self.maxForceAlign)
    		
    	return steering
    	
    
    def cohesion(self,boids):
    	perceptionRadius = self.cohesionPerception
    	steering =  pygame.math.Vector2()
    	total = 0
    	d= 0
    	
    	for i in range(len(boids)):
    		d = m.sqrt(((self.pos.x - boids[i].pos.x)**2) + ((self.pos.y - boids[i].pos.y)**2))
    		
    		if boids[i] != self and d < perceptionRadius:
    		 	steering += boids[i].pos
    		 	total += 1
    		 	
    	if total >0:
    		steering = steering / total
    		steering -= self.pos
    		steering.scale_to_length(self.maxSpeed) 
    		steering -= self.vel
    		
    		if steering.length()<self.maxForceCohesion:
    			steering = steering
    		elif steering.length()>=self.maxForceCohesion:
    			steering.scale_to_length(self.maxForceCohesion)
    		
    	return steering
    	 	
    def seperation(self,boids):
    	perceptionRadius = self.seperationPerception
    	steering =  pygame.math.Vector2()
    	total = 0
    	d= 0
    	
    	for i in range(len(boids)):
    		d = m.sqrt(((self.pos.x - boids[i].pos.x)**2) + ((self.pos.y - boids[i].pos.y)**2))
    		
    		if boids[i] != self and d < perceptionRadius:
    			diff = pygame.math.Vector2((self.pos.x-boids[i].pos.x),(self.pos.y-boids[i].pos.y))
    			diff = diff / d 
    			steering += diff
    			total += 1
    		 	
    	if total >0:
    		steering = steering / total
    		steering.scale_to_length(self.maxSpeed) 
    		steering -= self.vel
    		
    		if steering.length()<self.maxForceSeperation:
    			steering = steering
    		elif steering.length()>=self.maxForceSeperation:
    			steering.scale_to_length(self.maxForceSeperation)
    		
    	return steering
    	    	
    			
    def flocking(self,boids):
    	#alignment = self.align(boids)
    	cohesion = self.cohesion(boids)
    	#seperation = self.seperation(boids)
    	#self.acc += seperation
    	#self.acc += alignment
    	self.acc += cohesion

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0 
    
    def show(self):
            pygame.draw.circle(window,white,(int(self.pos.x),int(self.pos.y)),size)
            



def type(text,x,y,color):
	message = font.render(text,True,color)
	window.blit(message,(x,y))

for i in range(numBoids):
    flock.append(Boid(random.choice(range(width)),random.choice(range(height))))


while True:
    #allows user to exit the screen
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       if event.type == pygame.KEYDOWN:
       	   if event.key == pygame.K_UP:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].maxForceAlign +=0.25
       	   if event.key == pygame.K_DOWN:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].maxForceAlign -=0.25
       	   	   	   
       	   if event.key == pygame.K_RIGHT:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].maxForceCohesion +=0.25
       	   if event.key == pygame.K_LEFT:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].maxForceCohesion -=0.25
       	   	   	   
       	   if event.key == pygame.K_PERIOD:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].maxForceSeperation +=0.25
       	   if event.key == pygame.K_COMMA:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].maxForceSeperation -=0.25
       	   
       	   if event.key == pygame.K_EQUALS :
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].alignPerception +=5
       	   if event.key == pygame.K_MINUS:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].alignPerception -=5
       	   
       	   if event.key == pygame.K_0 :
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].cohesionPerception +=5
       	   if event.key == pygame.K_9:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].cohesionPerception -=5
       	   	   	   
       	   if event.key == pygame.K_RIGHTBRACKET :
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].seperationPerception +=5
       	   if event.key == pygame.K_LEFTBRACKET:
       	   	   for i in range(len(flock)):
       	   	   	   flock[i].seperationPerception -=5
	

    window.fill(black)  
    for i in range(len(flock)):
    	flock[i].edges()
    	flock[i].flocking(flock)
    	flock[i].update()
    	flock[i].show()  
    
    pygame.draw.rect(window,white, Rect((0,height-50),(width,50)))
    type("MFAlign: " + str(flock[1].maxForceAlign),10,height-35,black)
    type("MFCohesion: " + str(flock[1].maxForceCohesion),210,height-35,black) 
    type("MFSeperation: " + str(flock[1].maxForceSeperation),410,height-35,black)
    type("Align: " + str(flock[1].alignPerception),610,height-35,black)
    type("Cohesion: " + str(flock[1].cohesionPerception),810,height-35,black) 
    type("Seperation: " + str(flock[1].seperationPerception),1010,height-35,black)     

    
        
    pygame.display.update()
    clock.tick(FPS)

































