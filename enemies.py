class Orc:
    def __init__(self, name, hp, dmg, arm): #Här så får orcen veta hur mycket liv den har, 
                                            #hur mycket skada den gör och hyr mycket skada den kan ta innan hp:en sänks.
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.arm = arm

    def attack(self):
        print(f"{self.name} attacks for {self.dmg} dmg")
        return self.dmg

    def hit(self, dmg_recived, attack_type):
        print("You hit the enemy.")
        
        if attack_type == "standard": #Om attacken är standard så måste den ta sig igenom armour.
            total_damage_recived = dmg_recived - self.arm
            if total_damage_recived < 0:
                total_damage_recived = 0
            else:
                pass
            self.hp -= total_damage_recived
            if self.hp < 0:
                self.hp == 0
            print(f"It took {total_damage_recived} dmg!\nIt has {self.hp} hp left")

        elif attack_type == "magic": #Om attacken är magisk så går den förbi armour.
            self.hp -= dmg_recived
        
        else:
            print("Error, attack type non existent")