velocity = random(-12, -10)

flock = []
sze = 10
numBoids = 100

class Boid:

    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(random(-1, 1), random(-1, 1))
        self.vel.setMag(2)
        self.vel.mult(random(2, 3))  # try 2,4
        self.acc = PVector(0, 0)

        self.maxSpeed = 10
        self.maxForceAlign = 2
        self.maxForceCohesion = 2
        self.maxForceSeperation = 3

        self.alignPerception = 100  # 100
        self.cohesionPerception = 50  # 50
        self.seperationPerception = 100  # 200

    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)

    def show(self):
        fill(255)
        noStroke()
        ellipse(self.pos.x, self.pos.y, sze, sze)

    def edges(self):
        if self.pos.x > width:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = width

        if self.pos.y > height:
            self.pos.y = 0
        elif self.pos.y < 0:
            self.pos.y = height

    def align(self, boids):
        perceptionRadius = self.alignPerception
        steering = PVector(0, 0)
        total = 0
        d = 0

        for i in range(len(boids)):
            d = dist(self.pos.x, boids[i].pos.x, self.pos.y, boids[i].pos.y)

            if boids[i] != self and d < perceptionRadius:
                steering.add(boids[i].vel)
                total += 1

        if total > 0:
            steering = steering / total
            steering.setMag(self.maxSpeed)
            steering.sub(self.vel)
            steering.limit(self.maxForceAlign)

        return steering

    def cohesion(self, boids):
        perceptionRadius = self.cohesionPerception
        steering = PVector(0, 0)
        total = 0
        d = 0

        for i in range(len(boids)):
            d = dist(self.pos.x, boids[i].pos.x, self.pos.y, boids[i].pos.y)

            if boids[i] != self and d < perceptionRadius:
                steering.add(boids[i].pos)
                total += 1

        if total > 0:
            steering = steering / total
            steering.sub(self.pos)
            steering.setMag(self.maxSpeed)
            steering.sub(self.vel)
            steering.limit(self.maxForceCohesion)

        return steering

    def seperation(self, boids):
        perceptionRadius = self.seperationPerception
        steering = PVector(0, 0)
        total = 0
        d = 0

        for i in range(len(boids)):
            d = dist(self.pos.x, boids[i].pos.x, self.pos.y, boids[i].pos.y)

            if boids[i] != self and d < perceptionRadius:
                diff = PVector(
                    (self.pos.x - boids[i].pos.x), (self.pos.y - boids[i].pos.y))
                diff = diff / d
                steering.add(diff)
                total += 1

        if total > 0:
            steering = steering / total
            steering.setMag(self.maxSpeed)
            steering.sub(self.vel)
            steering.limit(self.maxForceSeperation)

        return steering

    def flocking(self, boids):
        sep = self.seperation(boids)
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)

        self.acc.add(sep)
        self.acc.add(alignment)
        self.acc.add(cohesion)
    

def setup():
    global flock

    size(1000, 750, P2D)

    for i in range(numBoids):
        flock.append(Boid(random(width), random(height)))

def draw():
    background(0)

    for boid in flock:
        boid.edges()
        boid.flocking(flock)
        boid.update()
        boid.show()

        # print(boid.vel.x,boid.vel.y)
