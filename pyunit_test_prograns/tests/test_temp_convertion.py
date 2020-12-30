import unittest
from temp_conversion import TemperatureConvert 

class TestTempratureConvertion(unittest.TestCase):

    def setUp(self):
        self.temp=TemperatureConvert()

    def test_celsius_to_fahrenheit(self):
        # self.assertAlmostEqual(self.temp.celsius_to_fahrenheit(20),68)
        self.assertRaises(TypeError,self.temp.celsius_to_fahrenheit('twenty'),68)

    # def test_get_temperature(self):      
    #     self.assertRaises(TypeError,self.temp.get_temperature())
    #     self.assertRaises(ValueError,self.temp.get_temperature())

if __name__ == "__main__":
        unittest.main()

