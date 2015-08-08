import unittest
class FizzBuzz():
	def count(self, number):
		if self.isModuloBy3(number):
			return 'fizz'
		if number ==5:
			return 'buzz'
		return str(number)

	def isModuloBy3(self, number):
		return number % 3 == 0


class TestFizzBuzz(unittest.TestCase):
	def setUp(self):
		self.fizzbuzz = FizzBuzz()

	def test_it_should_return_1_when_number_is_1(self):
		self.assertEqual('1',self.fizzbuzz.count(1))

	def test_it_should_return_2_when_number_is_1(self):
		self.assertEqual('2',self.fizzbuzz.count(2))

	def test_it_should_return_fizz_when_number_is_3(self):
		self.assertEqual('fizz',self.fizzbuzz.count(3))

	def test_it_should_return_buzz_when_number_is_5(self):
		self.assertEqual('buzz',self.fizzbuzz.count(5))

	def test_it_should_return_fizz_when_number_is_6(self):
		self.assertEqual('fizz',self.fizzbuzz.count(6))

