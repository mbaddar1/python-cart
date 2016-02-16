'''
Created on Feb 13, 2016

@author: baddar
'''
import csv
from decimal import Decimal
class IngredientsStore:
    '''
    classdocs
    '''
    "Store ingredients in store"
        
    def __init__(self,inputIngredients=list()):
        '''
        Create store instance with ingredients list with price
        '''
        if(not isinstance(inputIngredients, list)):
            raise ValueError("Input ingredients must be in list.")
        self.ingredients= dict()
        for item in inputIngredients:
            self.ingredients[item[0]] = Decimal(item[1])
    #static method to create ingredientStore instance from CSV        
    @staticmethod
    def init_from_filepath(csv_path):
        
        with open(csv_path,'rb') as csvfile:
            csvreader = csv.reader(csvfile,delimiter=',', quotechar='"')
            ingredientStoreInstance = IngredientsStore()
            ingredientStoreInstance.ingredients = dict()
            for row in csvreader:
                ingredientStoreInstance.ingredients[row[0]] = Decimal(row[1])
            return(ingredientStoreInstance)
    def get_ingredient_price(self,item):
        if self.ingredients.has_key(item):
            return self.ingredients[item]
        else:
            raise Exception('item '+item+' doesn\'t exist in the store')
        
    def hasIngredient(self,ingredientName):
        return self.ingredients.has_key(ingredientName)