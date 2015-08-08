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
    dummy_right = 1

    def test_1_should_be_one(self):
        captcha = Captcha(self.dummy_pattern,1,self.dummy_operand,self.dummy_right)
        self.assertEqual(captcha.left_operand(), 'one')
    def test_2_should_be_two(self):
        captcha = Captcha(self.dummy_pattern,2,self.dummy_operand,self.dummy_right)
        self.assertEqual(captcha.left_operand(),'two')

class TestFirstPatternRightOperand(unittest.TestCase):
    dummy_pattern = 1
    dummy_left = 1
    dummy_operand = 1

    def test_1_should_be_one(self):
        captcha = Captcha(self.dummy_pattern,self.dummy_left,self.dummy_operand,1)
        self.assertEqual(captcha.right_operand(),"one")

    def test_2_should_be_two(self):
        captcha = Captcha(self.dummy_pattern,self.dummy_left,self.dummy_operand,2)
        self.assertEqual(captcha.right_operand(),"two")

class TestSecondPatternRightOperand(unittest.TestCase):
    dummy_pattern = 2
    dummy_left = 1
    dummy_operand = 1

    def test_1_should_be_1(self):
        captcha = Captcha(self.dummy_pattern,self.dummy_left,self.dummy_operand,1)
        self.assertEqual(captcha.right_operand(),"1")
    def test_2_should_be_2(self):
        captcha = Captcha(self.dummy_pattern,self.dummy_left,self.dummy_operand,2)
        self.assertEqual(captcha.right_operand(),"2")

class TestOperand(unittest.TestCase):
    def test_1_sould_be_1(self):
        operand = Operand(1,1)
        self.assertEqual(operand.tostring(),'1')
    def test_2_should_be_2(self):
        operand =  Operand(1,2)
        self.assertEqual(operand.tostring(),'2')

class TestStringOperand(unittest.TestCase):
    def test_1_should_be_one(self):
        stringoperand = StringOperand(1)
        self.assertEqual(stringoperand.tostring(),'one')
    def test_2_should_be_two(self):
        stringoperand = StringOperand(2)
        self.assertEqual(stringoperand.tostring(),'two')

class TestintegerOperand(unittest.TestCase):
    def test_1_should_be_1(self):
        integeroperand = IntegerOperand(1)
        self.assertEqual(integeroperand.tostring(),'1')

class Captcha:
    def __init__(self,pattern,left,operator,right):
        # self.pattern = pattern
        if pattern == 1:
            self.left = integerOperand(left)
            self.right = stringoperand(right)
        elif pattern == 2:
            self.left = stringoperand
            self.right = integeroperand
        
  
        self.operator = Operand(operator)

    def left_operand(self):
        self.left.tostring

    def right_operand(self):
        words = ['one','two']
        if self.pattern == 2:
            return str(self.right)
        else :
            return words[self.right-1] 

    def operator(self):
        if self.operator == 1:
            return str(self.operator)

class Operand:
    def __init__(self ,operand):
        self.operand = operand
    def tostring(self):
        return str(self.operand)

class StringOperand(Operand):
    def __init__(self,operand):
        words = ['one', 'two']
        self.operand = words[operand-1]
class IntegerOperand(Operand):
    def __init__(self,operand):
        self.operand = operand






