import unittest

from database.StatisticsDAO import StatisticsDAO


class MyTestCase(unittest.TestCase):
    def test_year_loading(self):
        r = StatisticsDAO.load_years_list()
        self.assertEqual(len(r), 4)
        self.assertIn(2015, r)

if __name__ == '__main__':
    unittest.main()
