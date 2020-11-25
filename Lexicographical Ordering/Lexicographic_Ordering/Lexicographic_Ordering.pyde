vals = [0,1,2,3,4,5,6,7,8,9]

def setup():
    size(500,500)
    #noLoop()
    
    
def draw():
    global vals
    background(0)
    
    print(vals)
    
    textSize(64)
    s = ''
    for i in range(len(vals)):
        s += str(vals[i])
        
    fill(255)
    text(s,20,height/2)
    
    
    
    largestI = -1
    largestJ = -1
    
    for i in range(len(vals)-1):
        if vals[i] < vals[i+1]:
            largestI = i
            
    
    if largestI == -1:
        print('finished')
        noLoop()
        
        
    for j in range(len(vals)):
        if vals[largestI] < vals[j]:
             largestJ = j
             
    swap(vals,largestI,largestJ)    


    endArray = vals[largestI+1::]

    vals = vals[0:largestI+1]
    endArray = endArray[::-1]
    vals.extend(endArray)

        
    
    
        
    
    
    
def swap(a,i,j):
    temp = a[i]
    a[i]= a[j]
    a[j] = temp
