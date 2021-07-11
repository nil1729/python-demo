import unittest
import cap

class TestCap(unittest.TestCase):

    def test_single_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEquals(result, 'Python')
    
    def test_multiple_word(self):
        text = 'python django'
        result = cap.cap_text(text)
        self.assertEquals(result, 'Python Django')

if __name__ == '__main__':
    unittest.main()