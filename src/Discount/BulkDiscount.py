'''
Created on Feb 15, 2016

@author: baddar
'''
from Discount.AbstractDiscount import AbstractDiscount
class BulkDiscount(AbstractDiscount):
    
    def __init__(self,ingredientName,paidQty,freeQty):
        self.ingredientName = ingredientName
        self.paidQty = paidQty
        self.freeQty = freeQty
    
    def calc_line_total(self,cart):
        cart_qty = cart.getQty(self.ingredientName)
        bulks = cart_qty//(self.paidQty+self.freeQty)
        unitPrice = cart.ingredientsStoreInst.get_ingredient_price(self.ingredientName)
        tot_discount = bulks*self.freeQty*unitPrice
        return tot_discount