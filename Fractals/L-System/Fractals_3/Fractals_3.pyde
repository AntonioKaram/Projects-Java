#BASIC:
#Variables: A and B
#Axiom: A
#Rules: (A --> AB),(B --> A)

#FRACTAL 1:
#Variables: F and + and - and [ and ]
#Axium: F
#Rules: F --> FF+[+F-F-F]-[-F+F+F]

axiom = "F"
sentence = axiom
ln = 200
angle = 0


def turtle():
    background(0)
    resetMatrix()
    translate(width/2,height)
    stroke(255,100)
    for i in range(len(sentence)):
        now = sentence[i]
        if now == "F":
            line(0, 0, 0, -ln)
            translate(0, -ln)
        elif now == "+":
            rotate(angle)
        elif now == "-":
            rotate(-angle)
        elif now == "[":
            push()
        elif now == "]":
            pop()
            
def generate():
    global sentence
    global ln
    
    ln *=0.5 
    
    newSentence = ''
    for i in range(len(sentence)):
        current = sentence[i]
        if current == "F":
            current = "FF+[+F-F-F]-[-F+F+F]"
        else:
            current = current
        newSentence += current
    sentence = newSentence
    
    
    

        
def mousePressed():
    global sentence
    generate()
    print(sentence)
    
    

def setup():
    global angle
    size(800,800,P2D)
    angle = radians(25) 
    #turtle()

def draw():
   background(0)
   turtle()
    
    
    
    
    
    
