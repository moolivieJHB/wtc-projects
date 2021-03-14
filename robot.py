def robot_start():
    """This is the entry function, do not change"""
    # global name
    # """This is the entry function, do not change"""
    # name= input("What do you want to name your robot?")
    # name= name.upper()
    # print (name)
    # print('Hello kiddo!')
    # return name
    command=['OFF', 'HELP' ,'FORWARD','BACK' , 'RIGHT', 'LEFT', 'SPRINT']
    steps=''
    name=''
    ycoordinate = 0
    xcoordinate = 0
    name = get_robot_name()
    off = ""
    key= 0
    while True:

        ycoordinate , xcoordinate , off  , key = get_command_input(name , command , ycoordinate , xcoordinate , off , key)
        if off=="anything":

            break

def get_robot_name():
    # global name

    name = input("What do you want to name your robot? ")
    name = name.upper()
    print("{}: Hello kiddo!".format(name))   
    return name
    
def get_command_input(name , command , ycoordinate , xcoordinate , off , key ):

    plus=0
    action2 = input("{}: What must I do next? ".format(name))
    
    action= action2.upper()
    
    action=action.split()
    
    if action[0] in command:
        if action[0]=='OFF':
            print("{}: Shutting down..".format(name))
            off="anything"
           
        elif action[0]=='HELP':
            help()
        
        elif action[0] =='RIGHT':
            key+=1
            if key==4:
                key =0
            turn_right(name , ycoordinate , xcoordinate)
        elif action[0]=='LEFT':
            key-=1
            if key<0:
                key = 3
            turn_left(name , ycoordinate , xcoordinate)   
        # elif action[0]== 'SPRINT':
        #     for i in action[1]:
        #         forward(name , ycoordinate , xcoordinate , action[1])
        #         action[1]-=1
             
        elif len(action)==2 and action[1].isdigit():
            if action[0] =='FORWARD' or action[0]== 'SPRINT':
                if action[0]== 'SPRINT' :
                 
                    plus=add(int(action[1]))
                    
                if key == 0:
                    if( int(action[1]) + plus)+ ycoordinate>200:
                        out_of_bounds(name , ycoordinate, xcoordinate)
                    else:

                        ycoordinate= ycoordinate + (int(action[1]) + plus)
                        if action[0]!= 'SPRINT' :
                            forward(name ,ycoordinate , xcoordinate ,action[1])
                        else:
                            sprint(name , int(action[1]))
                            position_forward(name , ycoordinate, xcoordinate)
                elif key == 1:
                    if (int(action[1]) + plus) + xcoordinate>100:
                        out_of_bounds(name , ycoordinate, xcoordinate)
                    else:
                        xcoordinate =xcoordinate + (int(action[1]) + plus)
                        if action[0]!= 'SPRINT' :
                            forward(name ,ycoordinate , xcoordinate ,action[1])
                        else:
                            sprint(name , int(action[1]))
                            position_forward(name , ycoordinate, xcoordinate)
                elif key ==2:

                    if  ycoordinate - (int(action[1]) + plus) <-200:
                        out_of_bounds(name , ycoordinate, xcoordinate)
                    else:
                        ycoordinate= ycoordinate - (int(action[1]) + plus)
                        if action[0]!= 'SPRINT' :
                            forward(name ,ycoordinate , xcoordinate ,action[1])
                        else:
                            sprint(name , int(action[1]))
                            position_forward(name , ycoordinate, xcoordinate)
                elif key == 3:
                  
                    if  xcoordinate - (int(action[1]) + plus) <-100:
                        out_of_bounds(name , ycoordinate, xcoordinate)
                    else:   
                        

                        xcoordinate = xcoordinate - (int(action[1]) + plus)
                        if action[0]!= 'SPRINT' :
                            forward(name ,ycoordinate , xcoordinate ,action[1])
                        else:
                            sprint(name , int(action[1]))
                            position_forward(name , ycoordinate, xcoordinate)
                
                
            elif action[0] =='BACK':
              
                if key == 0:
                    if ycoordinate - int(action[1])  <-200:
                         out_of_bounds(name , ycoordinate, xcoordinate)
                    else:

                        ycoordinate= ycoordinate -int(action[1])
                        back(name , ycoordinate , xcoordinate , action[1])  
                  
                elif key == 1:
                    if  xcoordinate -int(action[1]) <-100:
                        out_of_bounds(name , ycoordinate, xcoordinate)
                    else:
                        xcoordinate =xcoordinate - int(action[1])
                        back(name , ycoordinate , xcoordinate , action[1]) 
                        
                elif key ==2:
                    if int(action[1]) + ycoordinate>200:
                        out_of_bounds(name , ycoordinate, xcoordinate)
                    else:
                        ycoordinate= ycoordinate + int(action[1])
                        back(name , ycoordinate , xcoordinate , action[1])
                elif key == 3:
                    if int(action[1]) + xcoordinate>100:
                        out_of_bounds(name , ycoordinate, xcoordinate)

                    else:
                        xcoordinate = xcoordinate +int(action[1])
                        back(name , ycoordinate , xcoordinate , action[1])

        
               
        else:
            print(name +': Sorry, I did not understand ' +"'" +action2 +"'.")      
    
    else:
        print(name +': Sorry, I did not understand ' +"'" +action2 +"'.")

    return ycoordinate , xcoordinate , off , key 
    
def help():
    print('''I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward
BACK - move backwards
RIGHT - move right
LEFT - move left
SPRINT - burst of speed''')

def forward(name , ycoordinate , xcoordinate , steps):

    print(' > {} moved forward by {} steps.'.format(name,steps))
    position_forward(name , ycoordinate, xcoordinate)

def back(name , ycoordinate ,xcoordinate , steps):
   
    print(' > {} moved back by {} steps.'.format(name,steps))
    position_forward(name , ycoordinate , xcoordinate)
    
  
def position_forward(name , ycoordinate , xcoordinate):

    print(" > {} now at position ({},{}).".format(name,xcoordinate,ycoordinate))
        
def turn_right(name , ycoordinate , xcoordinate):
  
    print(" > {} turned right.".format(name))
    position_forward(name , ycoordinate , xcoordinate)

def turn_left(name , ycoordinate, xcoordinate):

    print(" > {} turned left.".format(name))
    position_forward(name , ycoordinate , xcoordinate)
def out_of_bounds(name , ycoordinate , xcoordinate):
    print("{}: Sorry, I cannot go outside my safe zone.".format(name))
    position_forward(name , ycoordinate ,xcoordinate )
def sprint(name , steps):
    if steps==0:
        return 
    print(" > {} moved forward by {} steps.".format(name,steps))
    sprint(name ,steps-1)
def add(steps):
    plus =0
    for i in range(steps):
        plus += i
    return plus
if __name__ == "__main__":  
    robot_start()

   
    