import sys

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    while True:
        shape = input ('Shape?: ').lower()
        if shape=='triangle' or shape=='sqaure' or shape=='pyramid' or shape == 'rhombus' or shape=='trapezium':
            return shape
        


# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        height= input('Height?: ')
        if height.isdigit():
            return int(height)



# TODO: Step 2
def draw_pyramid(height, outline):
    if outline==False:
        x=1
        space=height -1
        for i in range(height):
            print(' '* (space) + '*'* x)        
            x=x+2
            space = space -1
    elif outline==True:
        firstline =height-1
        print(' '*firstline+ '*')
        for m in range(2 , height):
            outspace=height-m
            inspace=2*m-3
            print(' '*outspace +'*'+' '*inspace + '*')
        lastline= 2*m
        print('*' +'*' *lastline)

# TODO: Step 3
def draw_square(height, outline):
    if outline== False:
        for i in range(height):
         print('*'*height)

    elif outline== True:
        line1=height-1
        print('*'*line1)
        for m in range(2,height):
            inspace=height-3
            print('*' + ' '*inspace + '*')
        last=line1
        print('*'*last)

    pass
    



# TODO: Step 4
def draw_triangle(height, outline):
    if outline==False:
        x=1
        for i in range(height):
            print('*'* x)        
            x=x+1
    elif outline== True:
        for m in range(height):
            for n in range(m + 1):
                if n==0 or m==(height-1) or (m)==n:
                    print('*' , end='')
                else:
                    print(end=' ') 
            print()        
       
    

def draw_rhombus(height, outline):
    space= height+1
    if outline==False:
        space= height + 2
        for m in range (height):
            print(' '*space + '*'*height)
            space=space -1
    elif outline==True:
        
        out= height+2
        print(' '*out +'*'*height)
        for m in range(height-2):
            outer=height-1
            inspace=height-2
            print(' '*space + '*' +' '*inspace + '*')
            outer=outer -1
            space= space -1
        lastline= height-1
        print(' '*lastline +'*'*height)
    pass
def draw_trapezium(height , outline):
    space= height + 2
    if outline==False:
        for m in range (height):
            print(' '*space + '*'*height)
            space=space -1
            height= height+2
    elif outline==True:
        frst= height+3
        print(' '*frst +'*'*height)
        for m in range(1,height-1):
            hght=height+2
            inspace=height
            print(' '*space + '*' + ' '*inspace + '*')
            space=space -1
            height= height+2
        last=height+2
        print(' '*space+'*'*last)    
       
    pass


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height , outline)
    elif shape =="sqaure":
        draw_square(height , outline)
    elif shape =="triangle":
        draw_triangle(height , outline)
    elif shape=='rhombus':
        draw_rhombus(height , outline)
    elif shape=='trapezium':
        draw_trapezium(height , outline)   
            

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
   # while True:
    question =input('Outline only?').lower() 
    if question =='y':
            return True
    elif question=='n':
            return False
    else:
        pass




if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

