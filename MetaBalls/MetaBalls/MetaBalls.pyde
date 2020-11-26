blobs = []


class Blob:
    def __init__(self,x,y):
        self.pos = PVector(x,y)
        self.r = float(10)
        self.vel = PVector.random2D()
        self.vel.mult(random(2,5))
        
    def update(self):
        self.pos.add(self.vel)
        
        if self.pos.x>width or self.pos.x <0:
            self.vel.x *= -1
     
        if self.pos.y >height or self.pos.y < 0:
            self.vel.y *= -1
            
        
    def show(self):
        
        ellipse(self.pos.x,self.pos.y,self.r*2,self.r*2)



def setup():
    global blobs
    
    size(360,150,P2D)
    frameRate(60)
    colorMode(HSB)
    noFill()
    stroke(0)
    strokeWeight(4)
    
    for i in range(2):
        blobs.append(Blob(random(width),random(height)))
    
def draw():
    background(0)

    loadPixels()
    for x in range(width):
        for y in range(height):
            index = x + (y*width)
            sum = 0
            for b in blobs:
                d = dist(x,y,b.pos.x,b.pos.y)
                if d > 0:
                    col = (100*b.r)/d
                else:
                    col = 0
                sum+= col
                
            pixels[index] = color(sum,255,255)
            
    updatePixels()
    
    for b in blobs:
        b.update()
        #b.show()
    
