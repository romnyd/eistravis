from ejercicio import odd_numbers
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = odd_numbers([1, 8, 3, 6, 12, 5])
                self.assertEqual(resultado,[1, 3, 5])


if __name__ == '__main__':
	unittest.main()