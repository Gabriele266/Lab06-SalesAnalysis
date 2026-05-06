import unittest

from database.StatisticsDAO import StatisticsDAO


class MyTestCase(unittest.TestCase):
    def test_year_loading(self):
        r = StatisticsDAO.load_years_list()
        self.assertEqual(len(r), 4)
        self.assertIn(2015, r)

    def test_brand_loading(self):
        r = StatisticsDAO.load_brand_list()
        self.assertTrue(len(r) > 0)


    def test_retailer_loading(self):
        r = StatisticsDAO.load_retailer_list()
        self.assertTrue(len(r) > 0)

    def test_search_sales(self):
        result = StatisticsDAO.get_best_sales_filter(2017)
        self.assertEqual(len(result), 5)

if __name__ == '__main__':
    unittest.main()
