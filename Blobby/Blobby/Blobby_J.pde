void setup(){
  size(400,400,P2D);
}




void draw(){
  background(0);
  fill(255);

  translate(width/2,height/2);
  stroke(255);
  
  beginShape();
  int r = 100;
  float xoff = 0;
  float yoff = 0.01;
  
  for (float a = 0; a < TWO_PI; a+=0.05){
   float offset = map(noise(xoff+yoff),0,1,-15,15);
   float c = r + offset;
   
   float x = c * cos(a);
   float y = c * sin(a);
   
   vertex(x,y);
   xoff+= 0.05; 
  }
  yoff+= 0.05;
  
  
  
  endShape();
  
  


}
