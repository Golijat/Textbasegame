from inventory import Inventory
class Player:
    def __init__(self, name, hp, dmg, arm): #Här så får Player information om spelarens namn, health points, damage och armour.
        #hp är hur mycket liv Player har, dmg är hur mycket skada den gör och arm är hur mycket skada spelaren kan absorbera innan hp:en sänks.
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.arm = arm
        #self.inventory = Inventory({"Sword", 5})
        #self.firstdmg = self.inventory.items["Sword"]

    def attack(self):
        print(f"You attack for {self.dmg} damage!")
        return self.dmg

    def hit(self, dmg_recived):
        print("You got hit!")
        total_damage_recived  = dmg_recived - self.arm 
        if total_damage_recived < 0: #Här så räknas den totala skadan som spelaren tar ut.
            total_damage_recived = 0 # Om totalen blir mindre än noll, alltså om self.arm är större är dmg_recived,
                                    # så blir totalen noll, annars så skulle spelaren helas av attacked.
        else:
            pass
        self.hp -= total_damage_recived
        print(f"You hp is now {self.hp}")