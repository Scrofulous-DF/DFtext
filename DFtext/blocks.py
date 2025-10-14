from .items import *
from typing import Any, Type
from . import main as m
from .main import blockdatacreator

class Block:

    def __init_subclass__(cls : Any) -> None:
        super().__init_subclass__()
        m.LENGTH += 2

def no_bltag_blockdatacreator(type : str, action : str, items : tuple[Item, ...]):
    itemdata = []
    for index, item in enumerate(items):
        itemdata.append(item.get_item_text(index))
    
    blockdata = blockdatacreator(type, action, itemdata)

    m.DATA.append(blockdata)

class SetVar(Block):

    def __init__(self) -> None:
        self.type = "set_var"

    def set(self, var : Var, value : Item):
        """
        Sets a Var to a value

        var : variable to set
        value : any item 
        """
        no_bltag_blockdatacreator(self.type, "=", (var, value))

    def randomvalue(self, var : Var, *values : Item):
        """
        Sets a Var to random value from a set

        var : variable to set
        values : any items
        """
        no_bltag_blockdatacreator(self.type, "RandomValue", (var,)+ values)

    def add(self, var : Var, *numbers : Number | Var):
        """
        Sets a var to numbers (and/or vars) added

        var : var to set
        numbers : number (and/or vars that are number type) to add together
        """
        no_bltag_blockdatacreator(self.type, "+", (var,) + numbers)

    def subtract(self, var : Var, *numbers : Number | Var):
        """
        Sets a var to numbers (and/or vars) subtracted

        var : var to set
        numbers : number (and/or vars that are number type) to subtracted together
        """
        no_bltag_blockdatacreator(self.type, "-", (var,) + numbers)

    def multiple(self, var : Var, *numbers : Number | Var):
        """
        Sets a var to numbers (and/or vars) multipled

        var : var to set
        numbers : number (and/or vars that are number type) to multiple together
        """
        no_bltag_blockdatacreator(self.type, "x", (var,) + numbers)

    def increment(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "+=", items)

    def decrement(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "-=", items)

    def exponent(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "Exponent", items)

    def root(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "Root", items)

    def logarithm(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "Logarithm", items)

    def parsenumber(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "ParseNumber", items)
    
    def absolutevalue(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "AbsoluteValue", items)

    def clampnum(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "ClampNumber", items)

    def wrapnum(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "WrapNum", items)

    def bouncenum(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "BounceNum", items)

    def average(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "Average", items)

    def min(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "MinNumber", items)

    def max(self, *items : Item):
        no_bltag_blockdatacreator(self.type, "MaxNumber", items)