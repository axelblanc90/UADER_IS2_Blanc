import unittest
from new_primes4 import es_primo, imprimir_primos

class TestFuncionesPrimos(unittest.TestCase):

    def test_es_primo(self):
        self.assertFalse(es_primo(1))
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(13))
        self.assertFalse(es_primo(15))

    def test_imprimir_primos(self):
        self.assertEqual(imprimir_primos(1, 10), [2, 3, 5, 7])
        self.assertEqual(imprimir_primos(10, 20), [11, 13, 17, 19])
        self.assertEqual(imprimir_primos(22, 29), [23, 29])
        self.assertEqual(imprimir_primos(0, 1), [])

if __name__ == '__main__':
    unittest.main()
