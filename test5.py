from ejercicio import length
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = length([2, 3, 5, 2])
                self.assertEquals(resultado, "Less than 5")


if __name__ == '__main__':
	unittest.main()