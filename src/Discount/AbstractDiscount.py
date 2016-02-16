from abc import ABCMeta,abstractmethod
from _pyio import __metaclass__
class AbstractDiscount:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def calc_line_total(self,cart): pass