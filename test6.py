from ejercicio import reverse
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = reverse("casa")
                self.assertEqual(resultado,"asac")


if __name__ == '__main__':
	unittest.main()