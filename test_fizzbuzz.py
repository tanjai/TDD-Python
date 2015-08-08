import unittest
class FizzBuzz():
	def count(self, number):
		if number == 1:
			return '1'
		elif number == 3:
			return 'fizz'
		return '2'


class TestFizzBuzz(unittest.TestCase):
	def setUp(self):
		self.fizzbuzz = FizzBuzz()

	def test_it_should_return_1_when_number_is_1(self):
		self.assertEqual('1',self.fizzbuzz.count(1))

	def test_it_should_return_2_when_number_is_1(self):
		self.assertEqual('2',self.fizzbuzz.count(2))

	def test_it_should_return_fizz_when_number_is_3(self):
		self.assertEqual('fizz',self.fizzbuzz.count(3))
