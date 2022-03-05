from ejercicio import divide
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = divide(8,2)
                self.assertTrue(resultado)


if __name__ == '__main__':
	unittest.main()