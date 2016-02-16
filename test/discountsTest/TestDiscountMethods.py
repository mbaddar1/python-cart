'''
Created on Feb 16, 2016

@author: baddar
'''
import unittest
from decimal import Decimal
from ingredients.IngredientsStore import IngredientsStore
from carts.Cart import Cart
from Discount.NoDiscount import NoDiscount
from Discount.BulkDiscount import BulkDiscount
class TestDiscountMethods(unittest.TestCase):


    def testNoDiscountCalcLine(self):
        ingredients = [
                ('tomatoes', Decimal('0.15')),
                ('chicken', Decimal('3.49')),
                ('onions', Decimal('2.00')),
                ('rice', Decimal('0.70')),
            ]
        ingrStoreInst = IngredientsStore(ingredients)
        cart = Cart(ingrStoreInst)
        no_discount = NoDiscount('tomatoes')
        dval = no_discount.calc_line_total(cart)
        self.assertEqual(dval, 0, "")
        
    def testBulkDiscount(self):
        ingredients = [
                ('tomatoes', Decimal('0.15')),
                ('chicken', Decimal('3.49')),
                ('onions', Decimal('2.00')),
                ('rice', Decimal('0.70')),
            ]
        ingrStoreInst = IngredientsStore(ingredients)
        cart = Cart(ingrStoreInst)
        d1 = BulkDiscount('tomatoes',2,1)
        d2 = BulkDiscount('onions',1,1)
        d3 = BulkDiscount('rice',1,1)
        cart.add('tomatoes', 6)
        cart.add('onions',8)
        cart.add('chicken',3)
        
        d1_val = d1.calc_line_total(cart)
        d2_val = d2.calc_line_total(cart)
        d3_val = d3.calc_line_total(cart)
        
        self.assertEquals(Decimal('0.30').compare(d1_val), 0, "")
        self.assertEquals(Decimal('8.00').compare(d2_val), 0, "")
        self.assertEqual(Decimal('0.00').compare(d3_val), 0, "")
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDiscountMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)