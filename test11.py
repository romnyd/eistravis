from ejercicio import is_even
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                
                
                try:
                    resultado = is_even(23)
                    self.assertIsInstance(resultado, bool)
                except ValueError:
                    self.fail()


if __name__ == '__main__':
	unittest.main()