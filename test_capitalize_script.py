import unittest 
import capitalize_script


## create new class TestCapitalize that inherits the method TestCase() from unitttest library 
class TestCapitalize(unittest.TestCase):
    def test_one_word(self):
        text = 'python'

        ## set result to cap_text function imported from capitalize_script
        result = capitalize_script.cap_text(text)

        ##run test?
        self.assertEqual(result, 'Python')
    
    def test_multiple_words(self):
        text = 'monty python'
        result = capitalize_script.cap_text(text)
        self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
    unittest.main()