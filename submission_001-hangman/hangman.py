#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
   # import short_words
    word= open (file_name , "r")
    item= word.readlines()
    # print(item)
    return item


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    # ranword = random.choice(words)
    
    ranword= random.randint(0 , len(words)-1)
    y = words[ranword]
    item = random.randint(0 ,len(y)-1)
    a= y[:item] + '_' + y[item +1:]

    print('Guess the word: ' + a )  
    return y

def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    n = input('Guess the missing letter: ')
    return n


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: ' + word)



if __name__ == "__main__":
    run_game('short_words.txt')

