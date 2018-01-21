#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#
# This program does:
# Whatever
#
#Author: Rumbo181
#
#Date: '21/1/18'


class PriceRule:

    def __init__(self,symbol, condition):
        self.symbol=symbol
        self.condition=condition

    def matches(self,exchange):
        try:
            stock=exchange[self.symbol]
        except:
            return False
        return self.condition(stock) if stock.price else False

    def depends_on(self):
        return {self.symbol}



def main():
    pass


if __name__ == "__main__":
    main()