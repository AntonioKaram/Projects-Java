ArrayList<PVector> dots = new ArrayList<PVector>();



void setup(){
  size(1000,750,P2D);
  colorMode(HSB);
  
  for (int a = 0; a <360; a++){
   dots.add(PVector.fromAngle(a).mult(200));   
  }
}

void draw(){
  background(0);
  translate(width/2,height/2);
  
  stroke(255);
  noFill();
  
  for(PVector vec : dots){
    point(vec.x, vec.y);   
  }
  
  for (int i=0; i < dots.size(); i++){
    PVector me = dots.get(i);
    
    if (180 +i < 360){
      PVector pt = dots.get(180+i);
      stroke((i) % 255, 255, 255);
      line(me.x, me.y, pt.x, pt.y);
    
    }
    
  }




}
