from ast import Num
import random
from shutil import which
import sys
import time
from unittest import skip
from player import Player
from enemies import Orc
from inventory import Inventory
import json


#All nödvändig information importeras.

weapon = {"Sword": 5}
inv = [{"type": "health", "Health Potion": 10}, {"type": "dmg_inc", "Damage Potion": 5}]
level = 1

#Information från save filen sparas i variabler.
f = open('./save.txt', 'r', encoding='utf-8')
i = f.readline()
try:
    weapon = json.loads(i)
except:
    pass
i = f.readline()
try:
    inv = json.loads(i)
except:
    pass
i = f.readline()
try:
    level = json.loads(i)
except:
    pass
f.close

player = Player("Niklas", 20*level, 1*level, 0) #Lägger in information till Player klassen och på så sätt skapar player.
#inventory = {"Sword": 5, "Shield": -5}#Ger info till inventory klassen.
inventory = Inventory(weapon, [{"type": "health", "Health Potion": 10}, {"type": "dmg_inc","Damage Potion": 5}])#Ger info till inventory klassen.
enemy = Orc("Big Dude", random.randint(10,20)*level, random.randint(5,10)*(level/2), 0)
turn_counter = 0

def battle_start():
    print(f"From behinde a tree, {enemy.name} emerges.\n\nBattle Start")
    enemy_status()
    player_status()
    input(f"\nPress enter to continue")

    if random.randint(1,20) >= 15: #Här så slumpas ett tal och om talet är 15 eller mer så får fienden gå först. Annars så kör spelaren först.
        enemy_turn()
    else:
        player_turn()



def enemy_status():#Används så att spelaren kan få veta hur mycket skada fienden gör och hur mycket liv den har kvar.
    print(f"\nEnemy"
    f"\t\tName : {enemy.name}"
    f"\t\tDmg : {enemy.dmg}"
    f"\t\tHP : {enemy.hp}")

def player_status():
    print(f"\nPlayer"
    f"\t\tName : {player.name}"
    f"\t\tDmg : {player.dmg}"
    f"\t\tHP : {player.hp}")



def enemy_turn():
    time.sleep(2)
    if random.randint(1,20) >= 16:
        print(enemy.name,"missed.")
    else:

        player.hit(enemy.dmg)
    Player(player.name, player.hp, player.dmg, 0)
    player_turn()


def player_turn():
    
    if player.hp <= 0:
        player_dead()
    
    global turn_counter
    if turn_counter > 0:
        turn_counter -= 1
        if turn_counter == 0:
            player.dmg -= 5
    

    try:
        player_choice = int(input("\n1. Action\n2. Inventory\n3. Status\n==> "))
        if player_choice == 1:
            print("\n1. Sword Attack", {inventory.weapon("Sword") + player.dmg}," dmg\n2. Fist Attack", {player.dmg}, "\n3. Return")
            try:
                action = int(input("==> "))
            except:
                print("\nError, expected number, got something else.")    
                time.sleep(2)
                player_turn()
            time.sleep(1)

            if action == 1: #Om val 1 väljs så initieras metoden enenmy.hit där man tillför valuen som hör till inventory.weapon("Sword")
                enemy.hit(inventory.weapon("Sword") + player.dmg, "standard")
                if enemy.hp <=0:
                    battle_end()

            elif action == 2:
                enemy.hit(player.dmg, "standard")
                if enemy.hp == 0 or enemy.hp < 0:
                    battle_end()

            elif action == 3:
                player_turn()

            else:
                print("Non exsistent choice chosen, try again.")
                player_turn()

            input("\nPress enter to continue")
            enemy_turn()

        elif player_choice == 2:
            print("\n")
            inventory.show_inv()
            choice = int(input("\n1. Use Item\n2. Exit Inv\n==> "))
            if choice == 1:
                which_item = int(input("What item do you want to use?\n==>"))
                x = 1
                for item in inventory.items:
                    for a, b in item.items():
                        if a == "type":
                            type = item["type"]
                            continue
                        
                        if type == "health" and x == which_item:
                            player.hp += b
                            print(f"You healed {b} hp, you now have {player.hp} hp.\n")
                        elif type == "dmg_inc" and x == which_item:
                            player.dmg += b
                            turn_counter = 2
                            print("You drank the potion, you now deal 5 extra dmg for two turns\n")
                        x += 1
                enemy_turn()

            elif choice == 2:
                player_turn()
            else:
                print("Non exsistent choice chosen, try again.")
                time.sleep(2)
                player_turn()

        elif player_choice == 3:
            enemy_status()
            player_status()
            input("\nPress enter to continue")
            player_turn()

        else:
            print("Non exsistent choice chosen, try again.")
            time.sleep(2)
            player_turn()

    except ValueError:
        print("\nError, expected number, got something else.")    
        time.sleep(2)
        player_turn()

def battle_end():
    f = open('./save.txt', 'w', encoding='utf-8')
   
    f.write(json.dumps(inventory.weapons)+'\n')#Här skrivs inventory listorna och diktionarisen om till en sträng så att den kan läggas in i save.txt filen.
    f.write(json.dumps(inventory.items)+'\n')
    f.write(json.dumps(level+1))
    f.close
    print("You defeated the enemy!")
    exit()

def player_dead():
    f = open('./save.txt', 'w', encoding='utf-8')
    f.close
    print("\n\nYou got killed! That's too bad!\nTry again.")
    exit()
    


