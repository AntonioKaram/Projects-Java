change = 0.67
angle = PI
tree = []
a = 6
counter = 0
leaves = []

class Branch():
    def __init__(self,begin,en):
        self.en = en
        self.begin = begin
        self.finished = False

        
    def jitter(self):
        self.en.x += random(-1,1)
        self.en.y += random(-1,1)

    def show(self):
        stroke(255)
        line(self.begin.x,self.begin.y,self.en.x,self.en.y)
        
    def branchA(self):
        
        dir = PVector.sub(self.en,self.begin)
        dir.rotate(angle/a)
        dir.mult(change)
        
        newEnd = PVector.add(self.en,dir)
        branch = Branch(self.en,newEnd)
        
        return branch
    
    def branchB(self):
        dir = PVector.sub(self.en,self.begin)
        dir.rotate(-(angle/a))
        dir.mult(change)

        newEnd = PVector.add(self.en,dir)
        branch = Branch(self.en,newEnd)
        
        return branch


def keyPressed():
    global a 
    if keyCode == UP:
            a -= 0.1
    if keyCode == DOWN:
            a += 0.1
            
def mousePressed():
    global tree 
    global counter
    global leaves
    
    for i in reversed(range(len(tree))):
        if tree[i].finished == False:
            tree.append(tree[i].branchA())
            tree.append(tree[i].branchB())
        tree[i].finished = True
    
    counter += 1
    leaf = 0
    if counter >= 2:
        for i in range(len(tree)):
            if tree[i].finished == False:
                leaf = tree[i].en.copy()
                leaves.append(leaf) 
            
    
def setup():
    global tree
    
    size(800,800,P2D)
    
    a = PVector(width/2,height)
    b = PVector(width/2,height-200)
    
    root = Branch(a,b)
    tree.append(root)

    
    
def draw():
    background(0)
    
    for i in range(len(tree)):
        #tree[i].jitter()
        tree[i].show()
        
    for i in range(len(leaves)):
        noStroke()
        fill(255,0,100,100)
        ellipse(leaves[i].x,leaves[i].y,8,10)
    
