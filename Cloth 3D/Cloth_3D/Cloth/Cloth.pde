import toxi.geom.*;
import toxi.geom.mesh.*;
import toxi.geom.mesh.subdiv.*;
import toxi.geom.mesh2d.*;
import toxi.math.*;
import toxi.math.conversion.*;
import toxi.math.noise.*;
import toxi.math.waves.*;
import toxi.util.*;
import toxi.util.datatypes.*;
import toxi.util.events.*;

import toxi.physics.*;
import toxi.physics2d.*;
import toxi.physics2d.behaviors.*;
import toxi.physics2d.constraints.*;

class Particle extends VerletParticle2D {
  
  Particle(float x, float y){
    super(x,y);
  }
 
  void display(){
    fill(255);
    ellipse(x,y,10,10);
  }
}

class Spring extends VerletSpring2D{
  Spring(Particle a, Particle b){ 
    super(a,b,w,str);
  }
  
  void display(){
    stroke(255);
    strokeWeight(2);
    line(a.x,a.y,b.x,b.y);
  }
  
}

float str = 0.8;
float w = 10;
int cols = 40;
int rows  = 40;

ArrayList<Spring> springs;
Particle[][] particles = new Particle[cols][rows];
VerletPhysics2D physics;


void setup(){
  size(600,600);
  springs = new ArrayList<Spring>();
  
  physics = new VerletPhysics2D(); 
  
  Vec2D gravity = new Vec2D(0,1);
  GravityBehavior gb = new GravityBehavior(gravity);
  
  physics.addBehavior(gb);

  float x = 100;
  for (int i = 0; i < cols; i++){
    float y = 10;
    for (int j = 0; j < rows; j++){
       Particle p = new Particle(x,y); 
       particles[i][j] = p;
       physics.addParticle(p);
       y = y + w;
    }
       x = x + w;
  }
  
  for (int i = 0; i < cols-1; i++){
    for (int j = 0; j < rows-2; j++){
      Particle a = particles[i][j];
      Particle b1 = particles[i+1][j];
      Particle b2 = particles[i][j+1];
      
      Spring s1 = new Spring(a,b1);
      Spring s2 = new Spring(a,b2);
      
      springs.add(s1);
      springs.add(s2);
      
      physics.addSpring(s1);
      physics.addSpring(s2);
  
    }
  }
  
  particles[0][0].lock();
  particles[cols-1][0].lock();


  
}

void draw(){
  background(0);
  
  physics.update();
  
  for (int i = 0; i < cols; i++){
    for (int j = 0; j < rows; j++){
        //particles[i][j].display(); 
    }
  }
  
  for (Spring s: springs){
    s.display();
  }
}
