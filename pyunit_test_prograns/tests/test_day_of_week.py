import unittest
from day_of_week import DayOfWeek

class TestDayOfWeek(unittest.TestCase):
    
    def setUp(self):
        self.day_of_week = DayOfWeek()
    
    def test_get_date(self):
        self.assertRaises(ValueError,self.day_of_week.get_date)
        


if __name__ == "__main__":
    unittest.main()