import random

def random_fill_word(word):
    temp=''
    randletter_index= random.randint(0 , len(word)-1)
    letter= word[randletter_index]
    i=0
    while i<len(word)-1:
        if letter==word[i]:
            temp=temp +letter
        else:
            temp =temp +'_'
        
        i= i+1
    print(temp)    
    return temp
    
random_fill_word('morglin')