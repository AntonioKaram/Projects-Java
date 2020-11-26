cells = []


class Cell:
    def __init__(self,pos,r,c):
        self.r = r
        self.pos = pos
        self.c = c 
    
    def move(self):
        vel  = PVector.random2D()
        self.pos.add(vel)
    
    def show(self):
        fill(self.c,100)
        noStroke()
        ellipse(self.pos.x,self.pos.y,self.r,self.r)
        
    def clicked(self,x,y):
        d = dist(self.pos.x,self.pos.y,x,y)
        
        if d < self.r:
            return True
        else:
            return False
        
    def mitosis(self):
        offset = random(-20,20)
        newpos = PVector(self.pos.x+offset,self.pos.y+offset)
        cell = Cell(newpos,self.r*0.8,self.c)
        return cell


def setup():
    global cells
    size(700,700,P2D)
    cells.append(Cell(PVector(random(width-80),random(height-80)),80,color(random(100,255),0,random(100,255))))
    cells.append(Cell(PVector(random(width-80),random(height-80)),80,color(random(100,255),0,random(100,255))))
    
    
def draw():
    background(0)
    for i in range(len(cells)):
        cells[i].move()
        cells[i].show()

def mousePressed():
    global cells
    cellA = 0
    for i in reversed(range(len(cells))):
        if  cells[i].clicked(mouseX,mouseY):
            cellA = cells[i].mitosis() 
            cellB = cells[i].mitosis()
            cells.append(cellA)
            cells.append(cellB)
            cells.pop(i)
             
        
        
        
        
        
        
