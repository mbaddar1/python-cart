'''
Created on Feb 15, 2016

@author: baddar
'''
from ingredients.IngredientsStore import IngredientsStore
class Cart:
    '''
    Data structure to store shopping cart for a customer , each ingredient with its 
    quantity
    '''
    
    def __init__(self, ingredientsStoreInst):
        '''
        Create Cart instance with ingredientStore instance
        '''
        #chack parameters
        if(not isinstance(ingredientsStoreInst, IngredientsStore)):
            raise ValueError("Cart must take instance of type IngredientsStore")
        self.ingredientsStoreInst = ingredientsStoreInst
        self.cart_dict = dict()
    '''
    Add items to cart
    '''
    def add(self,ingredientName,qty = 1):
        if not isinstance(qty, (int,long)):
            raise ValueError("Qty must be integer or long")
        if(qty < 1):
            raise ValueError("Qty must be >=1")
        #merge added quantities to existing or add new ingredient line
        if not (self.ingredientsStoreInst.hasIngredient(ingredientName)):
            raise ValueError("Ingredient :"+ingredientName+" not in the associated ingredient store.")
        tmp = self.cart_dict.get(ingredientName,0)
        self.cart_dict[ingredientName] = tmp + qty
    def getQty(self,ingredientName):
        return (self.cart_dict.get(ingredientName,0))
    '''
    Get total price to pay after applying discounts
    '''
    def get_total(self,discounts=[]):
        tot_discount = 0
        tot_price_list = map(lambda (k,v): v*self.ingredientsStoreInst.get_ingredient_price(k),self.cart_dict.iteritems())
        tot_price = reduce(lambda x,y :x+y, tot_price_list)
        
        if len(discounts) == 0:
            tot_discount = 0
        else:
            discount_vals = map(lambda d: d.calc_line_total(self),discounts)
            tot_discount = reduce(lambda x,y:x+y, discount_vals)
        return tot_price-tot_discount
            
            
        
        