#add_library('peasycam')
#add_library("toxiclibscore")
#add_library('verletphysics')



#class Particle(verletParticle2D):
#    def __init__(self,x,y):
 #       super().__init__(x,y)
        



particles = []
springs = []


def setup():
    size(600,400)
    global particles
    global springs
    
    
def draw():
    background(0)
