from ejercicio import addit
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = addit(3)
                self.assertEqual(resultado, 8)


if __name__ == '__main__':
	unittest.main()