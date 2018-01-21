#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#
# This program does:
# Unittest 
#
#Author: Rumbo181
#
#Date: '21/1/18'


import unittest
from datetime import datetime

from ..rule import PriceRule
from ..stock import Stock




class PriceRuleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        goog=Stock('GOOG')
        goog.update(datetime(2014,2,10),11)
        cls.exchange = {"GOOG": goog}

    def test_a_PriceRule_matches_when_it_meets_the_condition(self):
        rule = PriceRule('GOOG', lambda stock: stock.price > 10)
        self.assertTrue(rule.matches(self.exchange))

        "TODO: develop the remainder tests"



    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
