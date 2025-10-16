from gzip import compress
from base64 import b64encode
from typing import Any
from .nbt import external_saving_system

DATA = []
LENGTH = 0

# saving_system = external_saving_system(r"C:\Users\Kyleb\AppData\Roaming\.minecraft\hotbar.nbt", 8, 8)

def INIT(hotbarpath, bar, slot):
    global saving_system

    saving_system = external_saving_system(hotbarpath, bar, slot)

def blockdatacreator(type : str, action : str, items : list[str] = []) -> dict[str, Any]:
    return {"id":"block", "block":type, "args":{"items":items}, "action":action}

class Block:

    def __init_subclass__(cls : Any) -> None:
        super().__init_subclass__()
        m.LENGTH += 2

def no_bltag_blockdatacreator(type : str, action : str, items : tuple[Item, ...]):
    itemdata = []
    for index, item in enumerate(items):
        itemdata.append(item.get_item_text(index))
    
    blockdata = blockdatacreator(type, action, itemdata)

    DATA.append(blockdata)

def packer(data : list[str]) -> str:
    return str({"blocks" : data})

def compresser(data : str) -> str:
    return b64encode(compress(data.encode("utf-8"))).decode("utf-8")

def dataparser(data):
    global DATA
    global LENGTH

    packed = packer(data).replace("'", '"')

    print(packed)

    compressed = compresser(packed)

    saving_system.add_enderchest(compressed, LENGTH)

    DATA = []
    LENGTH = 0

def QUIT():

    saving_system.save()
