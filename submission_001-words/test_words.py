import unittest
import word_processor
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stderr, redirect_stdout


class TestWord(unittest.TestCase):
    def test_convert_to_list(self):
        result = word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertTrue(result , "['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement', 'times', 'what', 'say', 'you']")
    
    def test_words_longer_than(self):
        result= word_processor.words_longer_than(7 ,'These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertTrue(result, "['interesting', 'understatement']")

    def test_words_length_map(self):
        result=word_processor.words_lengths_map('')
        self.assertTrue('{5: 2, 3: 3, 6: 1, 11: 1, 2: 1, 7: 1, 14: 1, 4: 1}')
    
    def test_count_letters(self):
        result= word_processor.letters_count_map('')
        self.assertTrue(result ,"{'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 7, 'u': 3, 'v': 1, 'w': 0, 'x': 0, 'y': 2, 'z': 0}")
    
    def test_most_used_character(self):
        result = word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(result , 'e')