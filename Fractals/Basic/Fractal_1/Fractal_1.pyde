change = 0.67
angle = PI
a = 4
def branch(ln):
    line(0, 0, 0,  - ln)
    translate(0,-ln)
    if ln > 2:
        if a != 0:
            push()
            rotate(angle/a)
            branch(ln * change)
            pop()
            push()
            rotate(-(angle/a))
            branch(ln * change)
            pop()
    
    



def setup():
    size(800,800,P2D)
    
def draw():
    background(0)
    
    stroke(255)
    translate(width/2,height)
    
    branch(200)
    print a 

def keyPressed():
    global a 
    if keyCode == UP:
            a -= 0.1
    if keyCode == DOWN:
            a += 0.1
