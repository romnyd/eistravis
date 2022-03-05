from funciones import sumar
import unittest

class TestSumar(unittest.TestCase):

	def test_1(self):
		resultado = sumar(3, 4, 1, 7)
		self.assertNotEqual(resultado, 13)


if __name__ == '__main__':
	unittest.main()
		