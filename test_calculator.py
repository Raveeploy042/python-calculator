import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) #actual output vs expected output

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3) 
    
    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1) 

    def test_add_positive_and_negative (self) :
        self.assertEqual(self.calc.add(10, -7), 3)

    def test_add_negative_zero (self) :
        self.assertEqual(self.calc.add(0, -7), -7)

    #test_subtract
    def test_subtract(self) :
        self.assertEqual (self.calc.subtract(5, 3), -2)

    def test_subtract_Second_greater_First(self) :
        self.assertEqual (self.calc.subtract(9, 23), 14)
    
    def test_subtract_zero(self) :
        self.assertEqual (self.calc.subtract(23, 0), -23)
    
    #test_multiply

    def test_multiply(self):
        self.assertEqual (self.calc.multiply(9,3),27)

    def test_multiply_zero (self) :
        self.assertEqual (self.calc.multiply(10, 0), 0)

    def test_multiply_negative (self) :
        self.assertEqual (self.calc.multiply(-8, 7), -56)

    #test_divide

    def test_divide (self) :
        self.assertEqual (self.calc.divide (24, 6) , 4)
    
    def test_divide_zero (self) :
        self.assertEqual (self.calc.divide (0, 10) , 0)

    def test_divide_negative (self) :
        self.assertEqual (self.calc.divide (-10, -10) , 1)
        
    #test_modulo

    def test_modulo (self) :
        self.assertEqual (self.calc.modulo (4 , 2), 0)
    
    def test_modulo_zero (self) :
        self.assertEqual (self.calc.modulo (0, 60), 0)

    def test_modulo_first_greaterthan_second (self) :
        self.assertEqual (self.calc.modulo (90, 80), 10)

    
if __name__ == '__main__':
    unittest.main()