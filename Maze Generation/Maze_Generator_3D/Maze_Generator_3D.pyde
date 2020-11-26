add_library('peasycam')

cols = None
rows = None
w = 20
current = None


grid = []
stack = []

cam = 0

def index(i, j):
    if i < 0 or j < 0 or i > cols - 1 or j > rows - 1:
        return -1

    return (i + j * cols)

def removeWalls(a, b):
    x = a.i - b.i
    y = a.j - b.j
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    if x == -1:
        a.walls[1] = False
        b.walls[3] = False
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    if y == -1:
        a.walls[2] = False
        b.walls[0] = False


class Cell:

    def __init__(self, i, j):
        self.i = i
        self.j = j  # Top , Right, Bottom, Left
        self.walls = [True, True, True, True]
        self.visited = False

    def checkNeighbors(self):
        neighbors = []

        if index(self.i, self.j - 1) != -1:
            top = grid[index(self.i, self.j - 1)]
        else:
            top = None
        if index(self.i + 1, self.j) != -1:
            right = grid[index(self.i + 1, self.j)]
        else:
            right = None
        if index(self.i, self.j + 1) != -1:
            bottom = grid[index(self.i, self.j + 1)]
        else:
            bottom = None
        if index(self.i - 1, self.j) != -1:
            left = grid[index(self.i - 1, self.j)]
        else:
            left = None

        if top != None and top.visited != True:
            neighbors.append(top)
        if right != None and right.visited != True:
            neighbors.append(right)
        if bottom != None and bottom.visited != True:
            neighbors.append(bottom)
        if left != None and left.visited != True:
            neighbors.append(left)

        if len(neighbors) > 0:
            r = floor(random(0, len(neighbors)))
            return neighbors[r]
        else:
            return False

    def highlight(self):
        x = self.i * w
        y = self.j * w

        noStroke()
        fill(0, 0, 255)
        pushMatrix()
        translate(x + (w / 2), y + (w / 2), w / 2)
        box(w - 1, w - 1, w - 1)
        popMatrix()

    def show(self):
        x = self.i * w
        y = self.j * w

        walls(self, x, y, w)


def setup():
    global grid
    global cols
    global rows
    global current
    global cam

    size(600, 600, P3D)

    cols = floor(width / w)
    rows = floor(height / w)

    cell = None
    for j in range(rows):
        for i in range(cols):
            cell = Cell(i, j)
            grid.append(cell)

    current = grid[0]

    cam = PeasyCam(this, 1000)

def draw():
    global stack
    global current

    lights()
    translate(-width / 2, -height / 2)
    background(51)

    for i in range(len(grid)):
        grid[i].show()

    current.visited = True
    current.highlight()
    next = current.checkNeighbors()  # STEP 1

    if next != False:  # PART 1
        next.visited = True
        stack.append(current)  # 2
        removeWalls(current, next)  # STEP 3
        current = next  # STEP 4

    elif len(stack) > 0:  # PART2
        current = stack[-1]
        stack.pop(-1)


def walls(cell, x, y, w):
    fill(255)
    stroke(255)
    pushMatrix()
    translate(x, y, 0)

    if cell.walls[0] == True:
        # line(0,0,w,0)

        beginShape()
        vertex(0, 0, 0)
        vertex(w, 0, 0)  # Top-Front
        vertex(w, 0, w)
        vertex(0, 0, w)
        endShape(CLOSE)

    if cell.walls[1] == True:
        #line(w, 0, w, w)

        beginShape()
        vertex(w, 0, 0)
        vertex(w, w, 0)  # Right-Front
        vertex(w, w, w)
        vertex(w, 0, w)  # Right-Back
        endShape(CLOSE)

    if cell.walls[2] == True:
        #line(w, w, 0, w)

        beginShape()
        vertex(w, w, 0)
        vertex(0, w, 0)  # Bottom-Front
        vertex(0, w, w)
        vertex(w, w, w)  # Bottom-Back
        endShape(CLOSE)

    if cell.walls[3] == True:
        #line(0, w, 0, 0)

        beginShape()
        vertex(0, w, 0)
        vertex(0, 0, 0)  # Left-Front
        vertex(0, 0, w)
        vertex(0, w, w)  # Left-Back
        endShape(CLOSE)

    popMatrix()
