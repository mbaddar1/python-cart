'''
Created on Feb 13, 2016

@author: baddar
'''

from ingredients.IngredientsStore import IngredientsStore
from decimal import Decimal
import csv
from pickle import INST
from carts.Cart import Cart
from Discount.BulkDiscount import BulkDiscount
from Discount.NoDiscount import NoDiscount




ingredients = [
    ('tomatoes', Decimal('0.15')),
    ('chicken', Decimal('3.49')),
    ('onions', Decimal('2.00')),
    ('rice', Decimal('0.70')),
]

i = IngredientsStore(ingredients)
# v = i.ingredients['tomatoes']
# 
# i2 = IngredientsStore.init_from_filepath('../../data/ingredients.csv')
# print i2.ingredients['tomatoes']

# 
# try:
#     v2 = i.get_ingredient_price('tomatos')
#     print v2
# except Exception as inst:
#     print type(inst)
#     print inst.args

c = Cart(i)
q= c.getQty('tomatoes')
print q
c.add('tomatoes', 2)
q= c.getQty('tomatoes')
print q
c.add('tomatoes', 4)
q= c.getQty('tomatoes')
print q

d = BulkDiscount('tomatoes',2,1)
d1 = NoDiscount('tomatoes')
v = d.calc_line_total(c)
print v
v1 = d1.calc_line_total(c)
print v1

dic = dict()
dic = {"1":1,"2":2}
print dic
k = map(lambda (k,v) : v*v, dic.iteritems())
print k
c.add('onions',3)
#t = c.get_total()
#print t

t1 = c.get_total([d])
print t1
    
