#! /usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Date = '13/1/18'
'''


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = {}
        self.ordered_timestamps = []

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        self.price_history[timestamp] = price
        self.ordered_timestamps = sorted(list(self.price_history.keys()))

    @property
    def price(self):
        if len(self.price_history) == 0: return None  # el diccionario de precios no tiene ninguno
        return self.price_history[self.ordered_timestamps[-1]]

    def is_increasing_trend(self):
        return self.price_history[self.ordered_timestamps[-3]] \
               < self.price_history[self.ordered_timestamps[-2]] \
               < self.price_history[self.ordered_timestamps[-1]]
