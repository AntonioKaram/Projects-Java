minVal = -2.5
maxVal = 2.5


def setup():
    size(800, 800,P2D)
    colorMode(RGB, 1)
    pixelDensity(1)


def draw():
    
    background(255)
    
    w = float(5)
    h = float((w*height) / width)
    
    xmin = float(-w/2)
    ymin = float(-h/2)
    
    loadPixels()
    maxiter = 100
    
    xmax = float(xmin + w)
    ymax = float(ymin + h)
    
    dx = float((xmax - xmin) / (width))
    dy = float((ymax - ymin) / (height))
    
    y = float(ymin)
    for j in range(height):
        x = float(xmin)
        for i in range(width):
            a = float(x)
            b = float(y)
            
            n = 0
            
            while n < maxiter:
                aa = float(a * a)
                bb = float(b * b)
                twoab = float(2.0 * a * b)
                a = float(aa - bb + x)
                b = float(twoab + y)
                
                if ((a*a + b*b) > 16.0):
                    break
                n+=1
        
            if (n == maxiter):
                pixels[i+j*width] = color(0)
            else:
                pixels[i+j*width] = color(sqrt(float(n) / maxiter))
        
            x += dx
        y += dy
    
            
    
    updatePixels()

  
        
#Wrap    
#bright = 0
#if n <= int(maxIterations/2):
    #bright = map(n,0,maxIterations/2,0,1)
    #bright = map(sqrt(bright),0,1,0,255)
                
#if n == maxIterations:
    #bright = 200
