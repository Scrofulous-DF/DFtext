from .main import blockdatacreator, dataparser
from . import main as m
from typing import Literal, Any

class PlayerEvent:

    def __init__(self, eventtype : Literal["RightClick","LeftClick","SwapHands"]):
        self.eventtype = eventtype

    def __enter__(self):
        m.LENGTH += 2
        m.DATA.append(blockdatacreator("event", self.eventtype))
        

    def __exit__(self, exc_type : Any, exc_value  : Any, traceback : Any):
        dataparser(m.DATA)


class EntityEvent:

    def __init__(self):
        pass
