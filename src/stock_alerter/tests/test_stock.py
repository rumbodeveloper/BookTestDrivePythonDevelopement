#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#
# This program does:
# Unittest 
#
# Author: Rumbo181
#
# Date: '13/1/18'


import unittest
from datetime import datetime

from ..stock import Stock


class StockTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock('GOOG')

    def test_price_of_a_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        with self.assertRaises(ValueError):
            self.goog.update(datetime(2014, 2, 13), -1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2014, 2, 13), price=10)
        self.goog.update(datetime(2014, 2, 14), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)

    def tearDown(self):
        pass


class StockTrendTestOrdered(unittest.TestCase):

    def setUp(self):
        self.goog = Stock('GOOG')

    def given_a_series_of_prices(self, prices):
        timestamps = [datetime(2014, 2, 11), datetime(2014, 2, 12), datetime(2014, 2, 13)]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        self.given_a_series_of_prices([8, 10, 12])
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_decreases(self):
        self.given_a_series_of_prices((12, 8, 6))
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal(self):
        self.given_a_series_of_prices((8, 8, 8))
        self.assertFalse(self.goog.is_increasing_trend())

    def tearDown(self):
        pass



class StockNotOrderedUpdates(unittest.TestCase):
    def setUp(self):
        self.goog=Stock('GOOG')

    def test_Stock_price_returns_latest_update(self):
        self.goog.update(datetime(2014,2,14),10)
        self.goog.update(datetime(2014, 2, 11), 8)
        self.goog.update(datetime(2014, 2, 10), 7)
        self.assertEqual(10,self.goog.price,msg="Stock doesn't returns latest price")

class StockTrendTestNotOrdered(unittest.TestCase):

    def setUp(self):
        self.goog = Stock('GOOG')

    def given_a_series_of_prices(self, prices):
        timestamps = [datetime(2014, 2, 13), datetime(2014, 2, 11), datetime(2014, 2, 12)]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        self.given_a_series_of_prices([10, 8, 9])
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_decreases(self):
        self.given_a_series_of_prices((6, 8, 7))
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal(self):
        self.given_a_series_of_prices((8, 8, 8))
        self.assertFalse(self.goog.is_increasing_trend())

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
