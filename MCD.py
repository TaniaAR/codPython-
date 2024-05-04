import unittest
import math 

def maximoComunDivisor (nro1,nro2):
    return math.gcd(nro1,nro2)

class TestOperacion(unittest.TestCase):
    def test_maximoComunDivisor(self):
        esperado = 20
        actual = maximoComunDivisor(300,33800)
        self.assertEqual(actual, esperado)

        def tearDown(self):
            pass

    if __name__=='__main__':
        unittest.main()    
