import random
import sys


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    temp=''
    randletter_index= random.randint(0 , len(word)-1)
    letter= word[randletter_index]
    i=0
    while i<len(word):
        if randletter_index==i:
            temp=temp +letter
        else:
            temp =temp +'_' 
        
        i= i+1
    print(temp)    
    return temp
    


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    for n in range (0, len(original_word)):
        if char==original_word[n] and char!=answer_word[n]:
            return True
    else:
        return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    for i in range(0 , len(original_word)):
        if original_word[i]==char:
            answer_word= answer_word[:i] + char + answer_word[i+1:]
  
    return answer_word

def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses==4:
        print('/----')
        print('|')
        print('|')
        print('|')
        print('|')
        print('_______')
    elif number_guesses==3:
        print('/----')
        print('|   '+'0')
        print('|')
        print('|')
        print('|')
        print('_______')
    elif number_guesses==2:
        print('/----')
        print('|   '+'0')
        print('|  '+'/|\\')
        print('|')
        print('|')
        print('_______')  
    elif number_guesses==1:
        print('/----')
        print('|   '+'0')
        print('|  '+'/|\\')
        print('|   '+'|')
        print('|')
        print('________')  
    elif number_guesses==0:
        print('/----')
        print('|   '+'0')
        print('|  '+'/|\\')
        print('|   '+'|')
        print('|  '+'/ \\')
        print('_______')  

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    number_guesses=5
    print("Guess the word: "+answer)
    while word!=answer:
        guess = get_user_input()
        if guess=='exit' or guess=='quit':
            print('Bye!')
            break

        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            number_guesses -= 1
            do_wrong_answer(answer, number_guesses)
           # print("Guess the word: "+answer)
        if number_guesses==0:
            print('Sorry, you are out of guesses. The word was: ' + word)
            break
        


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file='a'
    if len(sys.argv) == 2:
        words_file=sys.argv[1]
    else: 
        words_file = ask_file_name()
    
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)
    

