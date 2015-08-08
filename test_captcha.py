import unittest
from app import app

#class TestCaptcha(unittest.TestCase):
#   def test_fail(self):
#       self.assertEqual(True,False)

class TestFirstPatternLeftOperand(unittest.TestCase):
    dummy_operand = 1
    dummy_right = 1
    dummy_pattern = 1 

    def test_1_should_be_1(self):
        captcha = Captcha(self.dummy_pattern,1,self.dummy_operand,self.dummy_right)
        self.assertEqual(captcha.left_operand(), '1')
    def test_2_should_be_2(self):
        captcha = Captcha(self.dummy_pattern,2,self.dummy_operand,self.dummy_right)
        self.assertEqual(captcha.left_operand(), '2')

class TestSecondPatternLeftOperand(unittest.TestCase):
    dummy_pattern = 2
    dummy_operand = 1

    def test_1_should_be_one(self):
        captcha = Captcha(self.dummy_pattern,1,self.dummy_operand,1)
        self.assertEqual(captcha.left_operand(), 'one')
    def test_2_should_be_two(self):
        captcha = Captcha(self.dummy_pattern,2,self.dummy_operand,1)
        self.assertEqual(captcha.left_operand(),'two')


class Captcha:
    def __init__(self,pattern,left,operand,right):
        self.left = left 
        self.pattern = pattern

    def left_operand(self):
        words = ['one', 'two']
        if self.pattern == 1:
            return str(self.left) 
        elif self.pattern == 2:
            return words[self.left-1]



