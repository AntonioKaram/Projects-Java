inc = 0.01


def setup():
    size(400,400,P2D)

    
def draw():
    yoff = 0
    
    loadPixels()
    for y in range(width):
        xoff = 0
        for x in range(height):
            index = x+(y*width)
            r = noise(xoff,yoff)*255
            pixels[index] = color(r,255)
            xoff += inc
        yoff+=inc
        
    updatePixels()

'''
For Blocky Perlin Noise
inc = 0.1
scl = 10
col = 0
rows = 0

def setup():
    global cols
    global rows
    
    size(400,400,P2D)
    
    cols = floor(width/scl)
    rows = floor(height/scl)
    

def draw():
    yoff = 0
    

    for y in range(rows):
        xoff = 0
        for x in range(cols):
            index = x+(y*width)
            r = noise(xoff,yoff)*255
            xoff += inc
            
            fill(r)
            rect(x *scl,y*scl,scl,scl)
        yoff+=inc
'''
