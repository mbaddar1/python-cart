'''
Created on Feb 16, 2016

@author: baddar
'''
import unittest
from decimal import Decimal
from carts.Cart import Cart
from ingredients.IngredientsStore import IngredientsStore
from Discount.BulkDiscount import BulkDiscount
from Discount.NoDiscount import NoDiscount
class TestCartsMethods(unittest.TestCase):


    def testCartAddInValidIngrOrQty(self):
        ingredients_list = [
            ('tomatoes', Decimal('0.15')),
            ('chicken', Decimal('3.49')),
            ('onions', Decimal('2.00')),
            ('rice', Decimal('0.70')),
        ]
        ingrStoreInst = IngredientsStore(ingredients_list)
        cart = Cart(ingrStoreInst)
        self.assertRaises(ValueError, Cart,ingredients_list)
        self.assertRaises(ValueError, cart.add,'tomatoes', '1')
        self.assertRaises(ValueError, cart.add,'tomatoes', 0)
        self.assertRaises(ValueError, cart.add,'tomatoes', -1)
        self.assertRaises(ValueError, cart.add,'tomatoess', 4)
    def testCartAddQty(self):
        ingredients_list = [
            ('tomatoes', Decimal('0.15')),
            ('chicken', Decimal('3.49')),
            ('onions', Decimal('2.00')),
            ('rice', Decimal('0.70')),
        ]
        ingrStoreInst = IngredientsStore(ingredients_list)
        cart = Cart(ingrStoreInst)
        cart.add('tomatoes', 2)
        cart.add('tomatoes', 5)
        self.assertEqual(cart.getQty('tomatoes'), 7, "")
    def testGetTotalNoDiscount(self):
        ingredients_list = [
            ('tomatoes', Decimal('0.15')),
            ('chicken', Decimal('3.49')),
            ('onions', Decimal('2.00')),
            ('rice', Decimal('0.70')),
        ]
        ingrStoreInst = IngredientsStore(ingredients_list)
        cart = Cart(ingrStoreInst)
        cart.add('tomatoes', 2)
        cart.add('onions', 4)
        cart.add('chicken',2)
        cart.add('rice',3)
        self.assertEqual(Decimal('17.38').compare(cart.get_total()), 0, "")
    def testGetTotalWithDiscounts(self):
        ingredients_list = [
            ('tomatoes', Decimal('0.15')),
            ('chicken', Decimal('3.49')),
            ('onions', Decimal('2.00')),
            ('rice', Decimal('0.70')),
        ]
        ingrStoreInst = IngredientsStore(ingredients_list)
        
        cart = Cart(ingrStoreInst)
        cart.add('tomatoes', 7)
        cart.add('onions', 4)
        cart.add('chicken',2)
        cart.add('rice',3)
        
        d1 = BulkDiscount('tomatoes',2,1)
        d2 = BulkDiscount ('onions',1,1)
        d3 = NoDiscount('rice')
        
        self.assertEqual(Decimal('13.83').compare(cart.get_total([d1,d2])),0,"")
        
if __name__ == "__main__":
   suite = unittest.TestLoader().loadTestsFromTestCase(TestCartsMethods)
   unittest.TextTestRunner(verbosity=2).run(suite)