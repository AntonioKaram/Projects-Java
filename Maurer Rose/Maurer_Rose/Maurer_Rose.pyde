x = 0
y = 0
r = 0
n = 0
d = 0
k = 0



def setup():
    size(1000,750,P2D)


def draw():
    global n
    global d
    background(0)
    translate(width/2,height/2)
    stroke(255)
    
    noFill()
    beginShape()
    strokeWeight(1) 
    for i in range(2 *361):
        k = radians(i * d)
        r = 350 * sin(n * k)
        x = r * cos(k)
        y = r * sin(k)
        vertex(x,y) 
    endShape()
    
    noFill()
    stroke(255,0,0)
    strokeWeight(4)
    beginShape()
    for i in range(2 *361):
        k = radians(i)
        r = 350 * sin(n * k)
        x = r * cos(k)
        y = r * sin(k)
        vertex(x,y) 
    endShape()
    
    n += 0.01
    d += 0.01
    
