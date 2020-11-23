int r = 2;

ArrayList<Walker> tree = new ArrayList<Walker>();
ArrayList<Walker> walkers = new ArrayList<Walker>();

class Walker{
   PVector pos;
   boolean stuck;
  
   Walker(boolean stuck,int x, int y){
    this.pos = new PVector(x,y);
    this.stuck = stuck;
   }
    
    
  void walk(){
    PVector vel = PVector.random2D();
    vel.mult(5);
    this.pos.add(vel);
    
    this.pos.x = constrain(this.pos.x,0,width);
    this.pos.y = constrain(this.pos.y,0,height);
    
  }
  
  boolean checkStuck(ArrayList<Walker> others){
    for (int i =0; i<others.size(); i++){
      float d = PVector.dist(this.pos, others.get(i).pos);
      if (d < (r*2)){
        this.stuck = true;
        break;
      }
    }
    return this.stuck;
  }
  
  void show(){
    if (this.stuck == true){
      stroke(255,0,0);
      fill(255,0,0);
    }else{
      fill(255);
      stroke(255);
    }
    ellipse(this.pos.x, this.pos.y, r * 2, r * 2); 
  }
}

int[] randomPoint(){
  int i = floor(random(4));
  int[] lst = new int[2];
 
  
  if (i==0){
    lst[0] = int(random(width));
    lst[1] = 0;
  }else if (i == 1){
    lst[0] = int(random(width));
    lst[1] = height;
  }else if (i == 2){
    lst[0] = 0;
    lst[1] = int(random(height));
  }else{
    lst[0] = width;
    lst[1] = int(random(height));
  }
  return lst;
}
  



void setup(){
  size(400,400,P2D);
  
  tree.add(new Walker(true,width/2,height/2));
  
  for(int i = 0; i <1000; i++){
    int[] pt = new int[2];
    pt = randomPoint();
    walkers.add(new Walker(false,pt[0],pt[1]));
  }
}



void draw(){
  background(0);
  
  for (Walker i: tree){
    i.show();
  }
  
  for (Walker i: walkers){
    i.show();
  }
  
  for(int i=0; i<200; i++){
    for (int a= walkers.size()-1; a>=0; a--){
      walkers.get(a).walk();
      if (walkers.get(a).checkStuck(tree) == true){
        tree.add(walkers.get(a));
        walkers.remove(a);
      }
    }
  }
}
