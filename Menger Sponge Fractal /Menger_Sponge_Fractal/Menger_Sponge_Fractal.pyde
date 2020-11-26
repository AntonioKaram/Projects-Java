a = 0

sponge = []





class Box:
    def __init__(self,x,y,z,biggness):
        self.pos = PVector(x,y,z)
        self. r = biggness
        
    def show(self):
        pushMatrix()
        translate(self.pos.x,self.pos.y,self.pos.z) 
        noStroke()
        fill(255)
        box(self.r) 
        popMatrix()
        
    def generate(self):
        boxes = []
        newR = self.r /3
        b= 0
        sum = 0
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):    
                    sum = abs(x) + abs(y) +abs(z)
                    if sum > 1: #if <=1 it gives an inverted fractal  
                        b = Box(self.pos.x + x*newR, self.pos.y+ y*newR, self.pos.z +z*newR,newR)
                        boxes.append(b)
        
        return boxes
            

def setup():
    global sponge 

    size(400,400,P3D)
    b = Box(0,0,0,200)
    sponge.append(b)
    
def mousePressed():
    global sponge
    next = []
    newBoxes = []
    for b in sponge:
        newBoxes = b.generate()
        next.extend(newBoxes)
    
        
    sponge = next

def draw():
    global a
    
    background(0)
    stroke(255)
    noFill()
    lights()
    
    translate(width/2,height/2)
    rotateX(a)
    rotateY(a*0.4)
    rotateZ(a*0.1)
    for b in sponge:    
        b.show()
    
    a += 0.01
