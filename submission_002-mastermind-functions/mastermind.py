import random
''' Global variables that will be used in each function '''
#code = [0,0,0,0]
answer =  ''
correct = False
turns = 0
correct_digits_and_position =0
# TODO: Decompose into functions
#def run_game():
def get_random_numbers(): 
    ''' This function generates 4 random numbers and stores them in a list called code.Its parameters is code'''
    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def check_number(): 
    ''' This function prompts the user for input then checks if the input is exactly  4 numbers.Its parameters is code and answer'''
    global code
    global answer
    
   # turns = 0
    #while not correct and turns < 12:
    while True:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        else:
            break
    

def  check_correct():
    ''' This function checks if the user guessed the correct number in the code .
    It also checks if the guess is in the correct position. It also counts the number of turns.
    Its parameter are turns , correct_digits_and_position and answer'''
    global turns
    global correct_digits_and_position
    global answer
    
    check_number()
    
    correct_digits_and_position = 0 
    #while not correct and turns < 12:      
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
  #  break
    turns += 1
 

def win():
    ''' This function checks if the winner won by checking if the number of correct_digits_and position is 4. 
                If the condition is not true then it displays the correct answer.
                Its paramters are code , turns , correct_digits_and_postion and correct.'''
    global code
    global turns
    global correct_digit_and_position
    global correct
   # while not correct and turns < 12:    
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
        print('The code was: '+str(code))
    else:

        print('Turns left: '+str(12 - turns))
        #check_number()
        #print('The code was: '+str(code))
        if (turns-12)==0:
            print('The code was: '+str(code))   
    return correct
def run_game(): 
    '''This is the main function which calls the other functions in order for the game to work. 
                Its parameters are turns and  correct '''
    global turns 
    correct = False
    get_random_numbers()

    while not correct and turns < 12:    

       
        #check_number()
        check_correct()
        correct =win()
        
    #turns +=1

if __name__ == "__main__":
    run_game()
