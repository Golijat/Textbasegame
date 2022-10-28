from tokenize import Name


class Inventory:
    def __init__(self, start_weapons={}, start_items=[]):
        self.weapons = start_weapons
        self.items = start_items

    def add_item(self, Name, Value):
        self.weapons[Name] = Value
        
    def weapon(self, name):
        return self.weapons[name]
    
    def show_inv(self):
        x = 1
        for item in self.items: # Den här biten kod används för att skippa utprintningen av vilken typ av föremål det är i inventoryt
                                # och istället printar bara föremålet. Sen så printas det även ut lite extra information beroende på
                                # vilken type föremålet har.
                for a, b in item.items():
                    if a == "type":
                        type = item["type"]
                        continue
                    
                    if type == "health":
                        print(x, a, ": +", b,"hp")
                    elif type == "dmg_inc":
                        print(x, a, ": +", b,"dmg for two turns")
                    x += 1