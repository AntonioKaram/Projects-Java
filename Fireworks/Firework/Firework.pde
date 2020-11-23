int numP = 100;
PVector Gsmall = new PVector(0, 0.08);
PVector Gbig = new PVector(0, 0.2);

int x = 0;

ArrayList<Fireworkk> fireworks = new ArrayList<Fireworkk>();


void setup(){
  size(1000,700,P2D);
  colorMode(HSB);
}



void draw(){
  noStroke();
  fill(0,0,0,75);
  rect(0, 0, width, height);
  
  if (random(1) <0.05){
    fireworks.add(new Fireworkk());
  }
  
  for (int i  = fireworks.size()-1; i>0; i--){
    fireworks.get(i).update();
    fireworks.get(i).show();
    
    if (fireworks.get(i).done() == true){
      fireworks.remove(i);
    }
  }
  
  x+=1;
}

class Particle{
  float hu;
  PVector pos;
  PVector vel;
  PVector acc;
  int lifespan;
  boolean firework;
  float lifespanDelta;
  
  
  
  Particle(float x, float y, float hu, boolean firework){
    this.pos = new PVector(x,y);
    this.firework = firework;
    this.hu = hu;
    
    this.lifespan = 255;
    this.lifespanDelta = random(4,6);
    
    if (this.firework == true){
      this.vel = new PVector(0,random(-15,-10));
    }else{
      this.vel =  PVector.random2D();
      this.vel.mult(random(1,4));
    }
    
    this.acc = new PVector(0,0);
    
  }
  
  void applyForce(PVector force){
    this.acc.add(force);
  }
  
  boolean done(){
    if (this.lifespan < 0){
      return true;
    
    }else{
      return false;
    
    }
  }
  
  void update(){
    if (this.firework != true){
      this.vel.mult(0.95);
      this.lifespan -= this.lifespanDelta;
    }
     this.vel.add(this.acc);
     this.pos.add(this.vel);
     this.acc.mult(0);
  }
  
  void show(){
   if (this.firework == true){
     stroke(this.hu,255,255);
     strokeWeight(6);
   }else{
     stroke(this.hu,255,255, this.lifespan);
     strokeWeight(4);
   }
   point(this.pos.x,this.pos.y);
  }
}

class Fireworkk{
  float hu;
  boolean exploded;
  Particle firework;
  ArrayList<Particle> particles;
  
  Fireworkk(){
    this.hu = random(255);
    this.firework = new Particle(random(width), height,this.hu, true);
    particles = new ArrayList<Particle>();
    this.exploded = false;
  }
  boolean done(){
    if (this.exploded == true && particles.size() == 0){
      return true;
    }else{
      return false;
    }
  }
  
  void update(){
    if (this.exploded != true){
      this.firework.applyForce(Gbig);
      this.firework.update();
      
      if (this.firework.vel.y >= 0){
        this.exploded = true;
        this.explode();
      }
    }
    
    for (int i = this.particles.size()-1; i >= 0 ; i--){
      this.particles.get(i).applyForce(Gsmall);
      this.particles.get(i).update();
      
      if (this.particles.get(i).done() == true){
        this.particles.remove(i);
      }
    }
  }

  void show(){
    if (this.exploded != true){
      this.firework.show();
    }
    for (int i = 0; i < this.particles.size(); i++){
      this.particles.get(i).show();
    }
  }
  
  void explode(){
    for (int i = 0; i<numP; i++){
      Particle p = new Particle(this.firework.pos.x, this.firework.pos.y,this.hu, false);
      this.particles.add(p);
    }
  }
}
