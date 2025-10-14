from typing import Literal, Any

class Item:
    def get_item_text(self, slot : int) -> dict[str, Any]:
        raise NotImplementedError("subclass did not implement \"get_item_text\" function")




class Var(Item):
    def __init__(self, name : str, scope : Literal["game", "save", "local", "line"]):
        scopedict = {"game" : "unsaved", "save": "saved", "local":"local", "line":"line"}

        self.scope = scopedict[scope]
        self.name = name

    def get_item_text(self, slot : int) -> dict[str, Any]:
        return {"item":{"id":"var","data":{"name":self.name, "scope":self.scope}},"slot":slot}
    
    def __str__(self):
        return f"var=({self.name},{self.scope})"
    
    def __repr__(self):
        return f"var=({self.name},{self.scope})"


class Number(Item):
    def __init__(self, number : str | float | int):
        self.number = number

    def get_item_text(self, slot : int) -> dict[str, Any]:
        return {"item": {"id": "num","data": {"name": str(self.number)}},"slot": slot}

    def __str__(self):
        return f"number=({self.number})"
    
    def __repr__(self):
        return f"number=({self.number})"

typedict = {"stxt":"comp", "sound":"snd", "particle":"part", "potion":"pot"}

class Param(Item):

    def __init__(self, name : str, type : Literal["any", "txt", "stxt", "num", "loc", "vec", "sound", "particle", "potion", "item", "var", "list", "dict"], plural = False, optional = False, defaultvalue : Item | None = None) -> None:
        self.name = name
        self.type = type
        self.plural = plural
        self.optional = optional
        self.defaultvalue = defaultvalue

        if not optional and not (defaultvalue == None):
                raise TypeError("If not optional there cannot be a default value")

    def get_item_text(self, slot: int) -> dict[str, Any]:
        self.defaultvalue.get_item_text(0)

        return {"item" : {"id" : "pn_el", "data" : {"name" : self.name, "type" : self.type, "plural" : self.plural, "optional" : self.optional}}}

Param("a", "particle")