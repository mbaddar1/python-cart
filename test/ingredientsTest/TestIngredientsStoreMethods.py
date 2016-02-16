'''
Created on Feb 14, 2016

@author: baddar
'''
import unittest
from decimal import Decimal
from ingredients.IngredientsStore import IngredientsStore
import ingredients
class TestIngredientsStoreMethods(unittest.TestCase):


    def assertIngredients(self,ingredientsStoreInst):

        self.assertEqual(Decimal('0.15').compare(ingredientsStoreInst.ingredients['tomatoes']), 0, "")
        self.assertEqual(Decimal('3.49').compare(ingredientsStoreInst.ingredients['chicken']), 0, "")
        self.assertEqual(Decimal('2.00').compare(ingredientsStoreInst.ingredients['onions']), 0, "")
        self.assertEqual(Decimal('0.70').compare(ingredientsStoreInst.ingredients['rice']), 0, "")
        
    def testInitFromList(self):
        ingredients_list = [
            ('tomatoes', Decimal('0.15')),
            ('chicken', Decimal('3.49')),
            ('onions', Decimal('2.00')),
            ('rice', Decimal('0.70')),
        ]
        ingrStorInstance = IngredientsStore(ingredients_list)
        self.assertIngredients(ingrStorInstance)
    def testInitFromCSV(self):
        ingrStorInstance = IngredientsStore.init_from_filepath('../../data/ingredients.csv')
        self.assertIngredients(ingrStorInstance)
    def testGetIngredientPrice(self):
        ingredients_list = [
            ('tomatoes', Decimal('0.15')),
            ('chicken', Decimal('3.49')),
            ('onions', Decimal('2.00')),
            ('rice', Decimal('0.70')),
        ]
        ingrStorInstance = IngredientsStore(ingredients_list)
        self.assertEqual(Decimal('0.15').compare(ingrStorInstance.get_ingredient_price('tomatoes')), 0, "")
        self.assertRaises(Exception, ingrStorInstance.get_ingredient_price,'tomatoess')

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIngredientsStoreMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
    