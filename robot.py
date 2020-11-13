

# TODO: Decompose into functions

    
def move_square(s ,d):
    ''' this is the functon used to move the robot in the shape ofa a sqaure
        for the degree (d) and size (s) specified in the move() function'''

    print("Moving in a square of size "+str(s))
    for i in range(4):
            
        print("* Move Forward "+str(s))
        print("* Turn Right "+str(d)+" degrees")

def move_rectangle(lenn , wid , deg):
    ''' this function moves the robot in a rectangle and takes arguments for the length (lenn),
          width(wid) and degrees(deg) ; for which it should move in a rectangle      '''
    print("Moving in a rectangle of "+str(lenn)+" by "+str(wid))
    for i in range(2):
        
        print("* Move Forward "+str(lenn))
        print("* Turn Right "+str(deg)+" degrees")
        print("* Move Forward "+str(wid))
        print("* Turn Right "+str(deg)+" degrees")
def move_circle(deg , lenn):
    '''this function moves the robot in a circle . It has 2 arguements , lenn and degree
       which is used to move the toy in a circle.'''

    print("Moving in a circle")

    for i in range(360):
            
        print("* Move Forward "+str(lenn))
        print("* Turn Right "+str(deg)+" degrees")

def square_dancing(lenn ,s , deg):
    ''' this function takes length(lenn) , size (s) and degree (deg) as arguements.
     It makes the robot dance(move) according to was in the main function (move()) as parameters'''
    print(f"Square dancing - 3 squares of size {s}")
    for i in range(3):
        # length = 20
        print("* Move Forward "+str(lenn))
        print(f"Moving in a square of size {s}")
        for j in range(4):
            print("* Move Forward " + str(s))
            print("* Turn Right " + str(deg) + " degrees")
                #degrees = 90
def crop_circles(size, lenn , deg):
    ''' this function which takes length(lenn) and degrees(deg) as arguements; is used to
        move the robot in  a crop circle'''
    print("Crop circles - 4 circles")
    for i in range(4):
        print(f"* Move Forward {size}")
        print("Moving in a circle")
        for k in range(360):
            print("* Move Forward " + str(lenn))
            print("* Turn Right " + str(deg) + " degrees")
    
def move():
    ''' instead of move() i would name the function move_toy_robot . I 
    choose this name because it is very descriptive; it tells you exactly what will be moved.'''
    ''' this function provides paramenters for each of the above functions'''
    move_square(10,90) 
    move_rectangle(20 ,10,90)
    move_circle(1,1)
    square_dancing(20 ,20,90)
    crop_circles(20,1,1)
 
def robot_start():
    '''this function calls the move function'''
    move()
   
    


if __name__ == "__main__":
    robot_start()
