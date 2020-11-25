add_library('peasycam')
x = float(0.01)
y = float(0)
z = float(0)

a = float(10)
b = float(28)
c = float(8.0/3.0)

#a = float(28)
#b = float(46.92)
#c = float(4)

points = []

cam = None

def setup():
    global cam
    size(800,600,P3D)
    colorMode(HSB)
    cam = PeasyCam(this,1000)
    
    
def draw():
    global x
    global y
    global z
    
    background(0)
    
    dt = float(0.01)
    
    dx = float( (a * (y - x))     * dt)
    dy = float( (x * (b - z) - y) * dt)
    dz = float( (x * y - c * z)   * dt)
    
    x = x + dx
    y = y + dy
    z = z + dz
    
    points.append(PVector(x,y,z))
    
    
    translate(0,0,-80)
    strokeWeight(0.2)
    scale(5)
    stroke(255)
    noFill()
    beginShape()
    
    hu =0
    
    for v in points:
        stroke(hu,255,255)
        vertex(v.x,v.y,v.z)
        

        hu += 0.1
        if hu > 255:
            hu = 0
        
    endShape()
    
    
     
