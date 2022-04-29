import unittest
from city_country_function import get_city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        city_function = get_city_country('chile', 'santiago')
        self.assertEqual(city_function, 'Chile Santiago')

    def get_country_citi_population(self):
        city_function = get_city_country('chile', 'santiago', 'population')
        self.assertEqual(city_function, 'Chile Santiago Population-')
if __name__ == '__main__':
    unittest.main()