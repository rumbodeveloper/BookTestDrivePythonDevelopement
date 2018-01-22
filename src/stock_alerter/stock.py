#! /usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Date = '13/1/18'
'''


class DiccOrderedKeys(dict):
    '''Esta clase es una forma facil de obtener un diccionario y un argumento con sus claves ordenadas'''

    @property
    def ordered_keys(self):
        return sorted(list(self.keys()))


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = DiccOrderedKeys()

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        self.price_history[timestamp] = price

    @property
    def price(self):
        if len(self.price_history) == 0: return None  # el diccionario de precios no tiene ninguno
        return self.price_history[self.price_history.ordered_keys[-1]]

    def is_increasing_trend(self):
        return self.price_history[self.price_history.ordered_keys[-3]] \
               < self.price_history[self.price_history.ordered_keys[-2]] \
               < self.price_history[self.price_history.ordered_keys[-1]]
