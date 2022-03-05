from ejercicio import mult
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = mult(3)
                self.assertTrue(resultado)


if __name__ == '__main__':
	unittest.main()