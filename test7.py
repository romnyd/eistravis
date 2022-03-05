from ejercicio import remove_letter
import unittest

class TestAddit(unittest.TestCase):

	def test_success(self):
                resultado = remove_letter("a","Hola esto es una prueba")
                self.assertEqual(resultado,"Hol esto es un prueb")


if __name__ == '__main__':
	unittest.main()