import unittest
from city_functions import cit_cou

class CitCouTestCase(unittest.TestCase):

       def test_city_country(self):
            formatted_citcou = cit_cou("Warsaw", "Poland")
            self.assertEqual(formatted_citcou, "Warsaw, Poland")

if __name__ == '__main__':
       unittest.main(exit=False)
