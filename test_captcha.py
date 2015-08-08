import unittest
from app import app

#class TestCaptcha(unittest.TestCase):
#	def test_fail(self):
#		self.assertEqual(True,False)

class TestFirstPatternLeftOperand(unittest.TestCase):
	def test_1_should_be_1(self):
		captcha = Captcha(1,1,1,1)
		self.assertEqual(captcha.left_operand, '1')


class Captcha:
	def __init__(self,pattern,left,operand,right):
		self.left_operand = str(left)