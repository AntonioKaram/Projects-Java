Bird bird;
ArrayList<Pipe> pipes = new ArrayList<Pipe>();
int score;



void setup(){
  size(800,700,P2D);
  
  bird = new Bird();

}

void draw(){
  background(0);
  
  
  if (frameCount % 60 == 0){
    pipes.add(new Pipe());
    System.out.println(pipes.size());
  }

  
  for (int i = 0; i < pipes.size(); i++){
    pipes.get(i).update();
    pipes.get(i).show();
    
    
    if (pipes.get(i).offscreen()){
      pipes.remove(i);
    }
    
    
    if (pipes.get(i).hits(bird)){
      pipes = new ArrayList<Pipe>();
      score = 0;
      bird.y = height/2;
      bird.x = 164;
      break;
    }
     
  }

  if (frameCount % 60 == 0){
    if (bird.x > pipes.get(0).x){
      score ++;
    }
  }
 
  
   bird.update();
   bird.show();
    
   textSize(24);
   text(("Score: "+str(score)), 10, 30);
   
   




}

class Bird{
  float x,y,r,gravity,vel,lift;
  
  Bird(){
    this.y = height/2;
    this.x = 164;
    this.r = 14;
    this.gravity = 1;
    this.vel = 0;
    this.lift = -20;
  }
  
  void show(){
    fill(255);
    ellipse(this.x,this.y,this.r,this.r); 
  }
  
  void update(){
    this.vel += this.gravity;
    this.vel *= 0.85;
    this.y += this.vel;
    
    if (this.y >= height-this.r){
      this.y = height;
      this.vel = 0;
    }
     if (this.y <= this.r){
       this.y = 0;
       this.vel = 0;
     }
  }
  
  void up(){
    this.vel += this.lift;
  }
}


class Pipe{
  float x,w,speed,space,top,bottom;
  boolean highlight;
  
  Pipe(){
    this.x = width;
    this.w = 20;
    this.speed = 3;
    this.highlight = false;
    this.space = random(42,height/2-50);
  
    if (random(1)>0.5){
      this.top = height/2 - this.space;
      this.bottom = height/2 ;
    }else{
      this.bottom = height/2 - this.space;
      this.top = height/2 ;
  
      }
  }
  
  void show(){
    fill(255,0,0);
    
    rect(this.x,0,this.w,this.top);
    rect(this.x,height-this.bottom,this.w,this.bottom);
  }
  
  void update(){
    this.x -= this.speed;
  }
  
  boolean offscreen(){
  if (this.x < -this.w){
    return true;
  }else{
  return false;
   }
  }
  
   boolean hits (Bird bird){
    if ((bird.y < this.top) || (bird.y  > (height-this.bottom))){
      if ((bird.x > this.x)&& (bird.x < (this.x +this.w) )){
        this.highlight = true;        
        return true;
      }else{
        return false;
      }
      
    }else{
        return false;
      }
      
    
  
  }    
}



void keyPressed(){
  if (key == ' '){
    bird.up();
  }
  
}
