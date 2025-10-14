import nbtlib
from nbtlib.tag import Compound, Int, String, List, Byte

"""
Editing players saved hotbars.

puts a chest with code templates into one of the players slots
"""

booldict = {True:1, False:0}

def textnbt(text : str, color : str, bold : bool, italic : bool):
    textnbt = Compound({
        "text" : String(text),
        "color" : String(color),
        "bold" : Byte(booldict[bold]),
        "italic" : Byte(booldict[italic])
    })

    return textnbt

def nbtenderchest(data : str, length : int):

    text1 = textnbt("F ", "gold", True, False)
    text2 = textnbt("Custom code template", "dark_purple", False, False)

    custom_name = textnbt("D", "aqua", True, False)
    custom_name["extra"] = List[Compound]([text1, text2])

    text3 = textnbt("Length: ", "gray", False, False)
    text4 = textnbt("Author: ", "gray", False, False)

    text3["extra"] = List[Compound]([textnbt(f"{length} blocks", "#d4d4d4", False, False)])
    text4["extra"] = List[Compound]([textnbt("DFtext", "#d4d4d4", False, False)])

    minecraftlore = List[Compound]([text3, text4])

    item = Compound({
        "components" : Compound({
            "minecraft:custom_data" : Compound({
                "PublicBukkitValues" : Compound({
                    "hypercube:codetemplatedata" : String("{{\"author\":\"Text Editor\",\"name\":\"DF custom template\", \"version\":1, \"code\":\"{}\"}}".format(data))
                })
            }),
            "minecraft:custom_name" : custom_name,
            "minecraft:lore" : minecraftlore
        }),
        "count": Int(1),
        "id" : String("minecraft:ender_chest")
    })

    return item

class external_saving_system:

    def __init__(self, hotbarpath : str, bar : int, slot : int) -> None:
        self.path = hotbarpath
        self.bar = bar
        self.slot = slot
        self.items = []
        self.chestslot = 0
        self.chest = Compound({
            "components" : Compound({
                "minecraft:container" : String("NONE")
            }),
            "count" : Int(1),
            "id" : String("minecraft:chest")
        })

    def add_enderchest(self, data : str, length : int):

        item = nbtenderchest(data, length)

        if self.chestslot == 27:
            raise MemoryError("more than 27 initiations are not yet able")

        self.items.append(Compound({
            "item" : item,
            "slot" : Int(self.chestslot)
        }))

        self.chestslot += 1

    def save(self):

        self.chest["components"]["minecraft:container"] = List[Compound](self.items)

        with nbtlib.File.load(self.path, gzipped=False, byteorder="big") as file:
            file[str(self.bar)][self.slot] = self.chest

