cols = None
rows = None
w = 10
current = None


grid = []
stack = []


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
        fill(0, 0, 255, 100)
        rect(x, y, w, w)

    def show(self):
        x = self.i * w
        y = self.j * w

        stroke(255)

        if self.walls[0] == True:
            line(x, y, x + w, y)  # Top
        if self.walls[1] == True:
            line(x + w, y, x + w, y + w)  # Right
        if self.walls[2] == True:
            line(x + w, y + w, x, y + w)  # Bottom
        if self.walls[3] == True:
            line(x, y + w, x, y)  # Left

        if self.visited:
            noStroke()
            fill(255, 0, 255, 100)
            rect(x, y, w, w)


def setup():
    global grid
    global cols
    global rows
    global current

    size(400, 400,P2D)
    #frameRate(5)

    cols = floor(width / w)
    rows = floor(height / w)

    cell = None
    for j in range(rows):
        for i in range(cols):
            cell = Cell(i, j)
            grid.append(cell)

    current = grid[0]

def draw():
    global stack
    global current

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
