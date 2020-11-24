int numParticles = 100000;
int cols,rows,zoff;
int scl = 15; //increasing => more blocky, decreasing => more vectors
float inc = 0.1;  
boolean show = false;

ArrayList<PVector> flowfield = new ArrayList<PVector>();
ArrayList<Particle> particles = new ArrayList<Particle>();






class Particle{
  PVector pos,vel,acc,prev;
  int maxSpeed;
  
  Particle(){
    this.pos = new PVector(random(width),random(height));
    this.vel = new PVector(0,0);
    this.acc = new PVector(0,0);
    this.maxSpeed = 2;
    this.prev = this.pos.copy();
  }

  void update(){
    this.vel.add(this.acc);
    this.vel.limit(this.maxSpeed);
    this.pos.add(this.vel);
    this.acc.mult(0);
  }

  void applyForce(PVector force){
    this.acc.add(force);
  }
  
  void show(){
    stroke(0,5);
    strokeWeight(1);
    //point(this.pos.x,this.pos.y);
    line(this.pos.x,this.pos.y,this.prev.x,this.prev.y);
    this.updatePrev();
  }
  
  
  void edges(){
    if (this.pos.x > width){
      this.pos.x = 0; 
      this.updatePrev();
    }
    if (this.pos.x < 0){
      this.pos.x = width;
      this.updatePrev();
    }
    if (this.pos.y > height){
      this.pos.y = 0;
      this.updatePrev();
    }
    if (this.pos.y < 0){
      this.pos.y = height;
      this.updatePrev();
    }
  }
  
  void updatePrev(){
    this.prev.x = this.pos.x;
    this.prev.y = this.pos.y;
  }
  
  void follow(ArrayList<PVector> vectors){
    int x = floor(this.pos.x / scl);
    int y = floor(this.pos.y / scl);
    
    int index = constrain(x +(y*(cols)),0,vectors.size()-1);
    PVector force = vectors.get(index);
    
    this.applyForce(force);
  }
}



void setup(){
  size(800,800,P2D);
  
  cols = floor(width/scl);
  rows = floor(height/scl);
  
  for (int i =0; i< cols*rows; i++){
    flowfield.add(new PVector(0,0));
  }
  
  for (int i = 0; i<numParticles; i++){
     particles.add(new Particle());
  }
   
   background(255);
 
}



void draw(){
  float yoff = 0;
  
  
  
  
  for (int y=0; y<rows; y++){
    float xoff = 0;
    
    for (int x=0; x<cols;x++){
      int index = x + (y * cols);
      float angle = noise(xoff,yoff,zoff) * TWO_PI * 4;
      PVector v = PVector.fromAngle(angle);
      v.setMag(1);
      
      flowfield.set(index,v);
      
      if (show == true){
        stroke(0,50);
        strokeWeight(1);
        pushMatrix();
        translate(x * scl, y * scl);
        rotate(v.heading());
        line(0, 0, scl, 0);
        popMatrix();
      }
      
      xoff += inc;
    }
    yoff +=inc;
  }
  zoff+=0.005;
  
  for (int i = 0; i < particles.size(); i++){
    particles.get(i).follow(flowfield);
    particles.get(i).update();
    particles.get(i).show();
    particles.get(i).edges();
  }
}

void mousePressed(){
  if (show == true){
    show = false;
  }else{
    show = true;
  }
}
