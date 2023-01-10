from inventory import Inventory
class Player:
    def __init__(self, name, hp, dmg, arm): 
        # Här så får Player information om spelarens namn, health points, damage och armour.
        # hp (Health Points) berättar hur mycket liv en spelare har, om spelarens hp blir noll, så dör spelaren och då förlorar.
        # dmg (damage) är hur mycket bas skada spelaren gör.
        # arm (armour) är hur mycket skada spelaren kan absorbera innan hp:en sänks.
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.arm = arm

    def hit(self, dmg_recived):
        print("You got hit!")
        total_damage_recived  = dmg_recived - self.arm 
        if total_damage_recived < 0: 
            total_damage_recived = 0 
            # Här så räknas den totala skadan som spelaren tar ut.
            # Om totalen blir mindre än noll, alltså om self.arm är större än dmg_recived,
            # så blir totalen noll, annars så skulle spelaren helas av attacken.
        else:
            pass
        self.hp -= total_damage_recived
        print(f"You hp is now {self.hp}")
        # När den totala skadan har räknats ut så subtraheras den från spelarens hp.
        # Sen skriver koden ut hur mycket hp spelaren har kvar.