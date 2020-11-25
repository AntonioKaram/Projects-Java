#SIN WAVEEE!!!

#angle = 0 then increase angle
#sin(angle)

def setup():
    size(1000, 800,P2D)
    colorMode(HSB, 1)
    pixelDensity(1)


def draw():

    ca = 0    #Real component of c                      try c = -0.8; c =0.8i; c = -0.8i; c = 1-goldenr; c = 0.285;
    cb = 0.8 #Imaginary component of c                       c = 0.285+0.01i; c = 0.45+0.1428i; c = −0.70176−0.3842i;
#                                                              c = −0.835−0.2321i; c = −0.8+0.156i; c = −0.7269+0.1889i

    
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
                
                if (aa + bb > 4.0):
                    break
                
                twoab = float(2.0 * a * b)
                a = float(aa - bb +ca)
                b = float(twoab +cb)
                
                
                n+=1
        
            if (n == maxiter):
                pixels[i+j*width] = color(0)
            else:
                h = sqrt(float(n) / maxiter)
                pixels[i+j*width] = color(h,255,255)
        
            x += dx
        y += dy
    
            
    
    updatePixels()
