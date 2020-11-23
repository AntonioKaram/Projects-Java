Cell[][] grid;
Cell[][] prev;


float dA = 1.0;
float dB = 0.5;
float feed = 0.05;  
float k = 0.062;
float time_step = 1;

void setup(){
  size(500,500,P2D);
  grid = new Cell[width][height];
  prev = new Cell[width][height];
  
  for (int i =0; i<width;i++){
    for (int j =0; j<height; j++){
      float a = 1.0;
      float b = 0.0;
      
      grid[i][j] = new Cell(a,b);
      prev[i][j] = new Cell(a,b); 
    }
  }
  
  for (int n = 0; n<10; n++){
    int startx = int(random(20, width - 20));
    int starty = int(random(20, height - 20));
    
    for (int i = startx; i<startx+10; i++){
      for (int j = starty; j<starty +10; j++){
          float a = 1.0;
          float b = 1.0;
          
          grid[i][j] = new Cell(a, b);
          prev[i][j] = new Cell(a, b);  
      }
    }   
  }  
}


void draw(){
  for (int i = 0; i <=1; i++){
    update();
    swap();
  }
  
  loadPixels();
  for (int i = 0; i<width;i++){
    for (int j = 0; j<height; j++){
      Cell spot = grid[i][j];
      float a = spot.a;
      float b = spot.b;
      
      int pix = i + (j*width);
      pixels[pix] = color((a-b)*255);
    
    }
  }
  updatePixels();
}

class Cell{
  float a;
  float b;
  
  Cell(float a_,float b_){
    this.a = a_;
    this.b = b_;
  }
}
  
void update(){
    for (int i = 1; i < width-1; i++){
      for (int j=1; j< height-1; j++){
        Cell spot = prev[i][j];
        Cell newspot = grid[i][j];
        
        float a  = spot.a;
        float b = spot.b;
        
        float laplaceA = float(0);
        laplaceA += a * -1;
        laplaceA += prev[i + 1][j].a * 0.2;
        laplaceA += prev[i - 1][j].a * 0.2;
        laplaceA += prev[i][j + 1].a * 0.2;
        laplaceA += prev[i][j - 1].a * 0.2;
        laplaceA += prev[i - 1][j - 1].a * 0.05;
        laplaceA += prev[i + 1][j - 1].a * 0.05;
        laplaceA += prev[i - 1][j + 1].a * 0.05;
        laplaceA += prev[i + 1][j + 1].a * 0.05;

        float laplaceB = float(0);
        laplaceB += b * -1;
        laplaceB += prev[i + 1][j].b * 0.2;
        laplaceB += prev[i - 1][j].b * 0.2;
        laplaceB += prev[i][j + 1].b * 0.2;
        laplaceB += prev[i][j - 1].b * 0.2;
        laplaceB += prev[i - 1][j - 1].b * 0.05;
        laplaceB += prev[i + 1][j - 1].b * 0.05;
        laplaceB += prev[i - 1][j + 1].b * 0.05;
        laplaceB += prev[i + 1][j + 1].b * 0.05;
            
        newspot.a = a + (dA*laplaceA - a*b*b + feed*(1-a))*1;
        newspot.b = b + (dB*laplaceB + a*b*b - (k+feed)*b)*1;

        newspot.a = constrain(newspot.a, 0, 1);
        newspot.b = constrain(newspot.b, 0, 1);
      }
    }
  }


void swap(){
  Cell[][] temp = prev;
  prev = grid;
  grid = temp;
}
