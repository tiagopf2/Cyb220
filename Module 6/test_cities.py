# Written by Tiago Perez

import unittest
from city_functions import format_city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city_country = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()

# 11.2 Population

import unittest
from city_functions import format_city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city_country = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - population 5000000' work?"""
        formatted_city_country = format_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_country, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
