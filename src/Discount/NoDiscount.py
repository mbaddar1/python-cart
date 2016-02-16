'''
Created on Feb 15, 2016

@author: baddar
'''
from Discount.AbstractDiscount import AbstractDiscount

class NoDiscount(AbstractDiscount):
   
    def __init__(self,ingredientName):
        self.ingredientName = ingredientName
    def calc_line_total(self, cart):
        return 0
    