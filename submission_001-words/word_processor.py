
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    
    return list(filter(None,(split(('.!?, ') , (text.lower())))))

def words_longer_than(length, text):

    words= convert_to_word_list(text)
    return list(map(lambda word:word , filter(lambda word: len(word)>length , words)))

def words_lengths_map(text):
    words=convert_to_word_list(text)
    length= list(sorted((map(lambda word:len(word), words))))
    length_dict= {key :length.count(key) for key in (length)}
    return length_dict

def get_alphabet_characters():
     alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     return alphabet
     
def letters_count_map(text):

    splitText= list(sorted(filter(None,(split((''),(text.lower().strip('?')))))))

    char_count=get_alphabet_characters()
    alphabet_dict= {key: splitText.count(key) for key in (char_count)}
    return alphabet_dict
    


def most_used_character(text):

    character= letters_count_map(text) 
    if len(text)== 0:
        return  None
    if len(character)==1:
        return character
    else:

        maxlength= max(character , key=character.get)
        return maxlength

if __name__ == "__main__":  
    print (convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?'))
    print(words_longer_than( 7 , 'These are indeed interesting, an obvious understatement, times. What say you?'))
    print(words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?'))
    print(letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?'))
    print(most_used_character('These are indeed interesting, an obvious understatement, times. What say you?'))