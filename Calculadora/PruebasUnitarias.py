"""
Created on Sun Oct  4 10:48:21 2020

@author: Christian Caro - 20181020027
@author: Neider Puentes - 20172021307
@author: Santiago Rios - 2018020027

"""
from calculadora import calculadora
import unittest
c = calculadora()

class PruebasUnitarias(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(c.sumar(5, 7), 12)

    def test_resta(self):
        self.assertEqual(c.restar(5, 7), -2)

    def test_multiplicar(self):
        self.assertEqual(c.multilplicar(5, 7), 35)

    def test_dividir(self):
        self.assertEqual(c.dividir(2, 1), 2)

    def test_elevar(self):
        self.assertEqual(c.elevar(5, 2), 25)

    def test_raiz(self):
        self.assertEqual(c.raizCuadrada(9), 3)

if __name__ == "__main__":
    unittest.main()
