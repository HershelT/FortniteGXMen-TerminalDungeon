blockedItems = ["🪵", '\033[31m▓\033[39m', "\033[32m※\033[0m","\033[38;2;218;165;32mⅡ\033[0m","\033[37m¤\033[0m", "🪨", "|", "🪦","💎", "※", "Ω","\033[90mΩ\033[0m", "₡", "Ⅲ", "Ⅷ", "Ⅱ"]





#"Item" : [["Items"][int(item amount)],"Name", Type of material needed to destroy"]
itemDrops = {
    "\033[32m※\033[0m" : [["Wood Plank", "Stick"],[3, 2],"Tree","Nothing"],
    "🪨" : [["Stone"],[2], "Boulder","Wood"],
    "\033[37m¤\033[0m" : [["Stone"],[2], "Boulder","Wood"],
    "\033[38;2;218;165;32m" + "Ⅱ" + "\033[0m" : [["Wood Wall"],[1], "Wood Wall", "Nothing"],
    "🪦" : [["Stone", "Flint"],[1,1], "Grave Yard", "Stone"],
    "🪵" : [["Crafting Table"],[1],"Crafting Table", "Nothing"],
    "\033[38;2;218;165;32mⅡ\033[0m" : [["Wood Wall"],[1],"Wood Wall", "Nothing"],
    "∏" : [["Wood Door"],[1], "Wood Door", "Nothing"],
    "\033[90mΩ\033[0m" : [["Iron Ore"],[1], "Iron Ore Deposit", "Stone"] #Can pass through if not on blocked items
}
def getItemList(item : str):
    itemsList = itemDrops[item]
    return itemsList



