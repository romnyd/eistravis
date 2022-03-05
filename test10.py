from ejercicio import even_numbers
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = even_numbers([1, 8, 3, 6, 12, 5])
                self.assertEqual(resultado,[8, 6, 12])


if __name__ == '__main__':
	unittest.main()