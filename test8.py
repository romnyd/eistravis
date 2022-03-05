from ejercicio import max
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = max([1, 8, 3, 0, 12])
                self.assertEqual(resultado,12)


if __name__ == '__main__':
	unittest.main()