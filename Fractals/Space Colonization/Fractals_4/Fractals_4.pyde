numLeaves = 1500
max_dist = 100
min_dist = 10
tree = None

class Leaf:
    def __init__(self):
        self.pos  = PVector(random(width),random(height-200))
        self.reached = False
    
    def show(self):
        noStroke()
        fill(255)
        ellipse(self.pos.x,self.pos.y,4,7)
        
class Branch():
    def __init__(self, parent, pos, dir):
        self.pos = pos
        self.parent = parent 
        self.dir = dir
        self.origDir = self.dir.copy()
        self.count = 0
        self.lengt = 2.5
        
    def reset(self):
        self.dir = self.origDir.copy()
        self.count = 0
        
    def next(self):
        newDir = PVector.mult(self.dir.copy(), self.lengt)
        newPos = PVector.add(self.pos,newDir)
        newBranch = Branch(self,newPos,newDir)
     
        
        return newBranch
    
    def show(self):
        stroke(255)
        
        if self.parent == None:
            line(self.pos.x, self.pos.y, width/2,height)
        else:
            line(self.pos.x, self.pos.y , self.parent.pos.x, self.parent.pos.y)

class Tree:
    def __init__(self):        
         self.leaves = []
         self.branches = []
         
         rootPos = PVector(width/2,height)
         dir = PVector(0,-1)
         root = Branch(None,rootPos,dir)
         self.branches.append(root)
         for i in range(numLeaves):
             self.leaves.append(Leaf())
         current = root
         found = False
         while found !=True:
            for i in range(len(self.leaves)):
                d = PVector.dist(current.pos,self.leaves[i].pos)
                if d < max_dist: #and d > min_dist:
                    found = True
            if found != True:
                branch = current.next()
                current = branch
                self.branches.append(current) 
                
    
    def grow(self):
        for i in range(len(self.leaves)):
            leaf = self.leaves[i]
            
            closestBranch = None
            record = 100000
            
            for j in range(len(self.branches)):
                branch = self.branches[j]
                
                d = PVector.dist(leaf.pos,branch.pos)
                
                if d < min_dist:
                    leaf.reached = True
                    closestBranch = None
                    break
                elif d > max_dist:
                    pass
                
                elif closestBranch == None or d < record:
                    closestBranch = branch
                    record = d
                    
            if closestBranch != None:
                newDir = PVector.sub(leaf.pos,closestBranch.pos)
                newDir.normalize()
                closestBranch.dir.add(newDir)
                closestBranch.count += 1
        
        for i in reversed(range(len(self.leaves))):
            leaf = self.leaves[i]
            if leaf.reached == True:
                print(leaf)
                self.leaves.remove(leaf)
                
        for i in reversed(range(len(self.branches))):
            branch = self.branches[i]
            if branch.count > 0:
                #branch.dir.normalize()
                branch.dir.div(branch.count+1)
                newDir = PVector.mult(branch.dir,2.5)
                newPos = PVector.add(branch.pos,newDir)
                newBranch = Branch(branch,newPos,newDir)
                self.branches.append(newBranch)
                
            branch.reset()
            
 
    def show(self):
        for i in range(len(self.leaves)):
            self.leaves[i].show()
            
        for i in range(len(self.branches)):
            self.branches[i].show()
        
            




def setup():
    global tree
    
    size(800,800,P2D)
    
    tree = Tree()
    
    
def draw():
    background(0)
    
    tree.show()
    tree.grow()
    
    
