# All nödvändig information importeras.
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

time.sleep(3)

# Start värdena för spelarens weapon, inventory och level sätts här.
weapon = {"Sword": 5}
inv = [{"type": "health", "Health Potion": 10}, {"type": "dmg_inc", "Damage Potion": 5}]
level = 1

# Information från save filen om spelarens weapon, inventory och level tas fram 
# och sätts in i respektive variabel, alltså skriver över start värdena.
# Om det inte finns information för en variabel så används start värdet för den variabeln, 
# för att undvika en spel krasch pga saknad information.


# Först öppnas save filen i läs läge.
f = open('./save.txt', 'r', encoding='utf-8')
# i variabeln används för att läsa av raderna med information i save filen.
# 
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
f.close()

# Här skickas all nödvänding information till dem olika klasserna,
# samtidigt som klasserna och dess metoder och information läggs i variabler
# Här så blir även spelaren och fienden starkare beroende på vilken level spelaren är.'
# Fiendens dmg och hp väljs slumpmässigt för att göra varje strid lite mer unik.
player = Player("Niklas", 20*level, 1*level, 0)
inventory = Inventory(weapon, inv)
enemy = Orc("Big Dude", random.randint(10,20)*level, random.randint(5,10)*(level/2), 0)
turn_counter = 0

def battle_start():
    # Striden startas med ett inledande meddelande och sen skrivs fiendens och spelarens statusar ut.
    print(f"From behinde a tree, {enemy.name} emerges.\n\nBattle Start")
    enemy_status()
    player_status()
    input(f"\nPress enter to continue")

    # Här så bestämms vem som går först genom att ta fram ett slumpmässigt tal mellan 1 och 20. 
    # Om talet är lika med 15 eller mer än 15 så får fiende köra först, annars kör spelaren först.
    if random.randint(1,20) >= 15:
        enemy_turn()
    else:
        player_turn()


def enemy_status():
    # Skriver ut fiendens namn, hur mycket skadan den gör och hur mycket hp den har.
    print(f"\nEnemy"
    f"\t\tName : {enemy.name}"
    f"\t\tDmg : {enemy.dmg}"
    f"\t\tHP : {enemy.hp}")

def player_status():
    # Skriver ut spelarens namn, hur mycket skada spelaren gör och hur mycket hp den har.
    print(f"\nPlayer"
    f"\t\tName : {player.name}"
    f"\t\tDmg : {player.dmg}"
    f"\t\tHP : {player.hp}")


def enemy_turn():
    # Först så pausar koden lite grann för att låta spelaren tänka lite och för att skapa lite spänning.
    # Sen tas ett slumpmässigt tal fram för att se om fienden missar sin attack. 
    # Om talat är lika med 16 eller mer så missar fienden. Annars träffar den.
    # Om fienden träffar så skickas den dmg som fienden gör in i player.hit metoden, 
    # där det räknas ut hur mycket skada spelaren tar och hur mycket liv den har kvar efter.
    # Sen går det över till spelarens tur.
    time.sleep(2)
    if random.randint(1,20) >= 16:
        print(enemy.name,"missed.")
    else:

        player.hit(enemy.dmg)
    player_turn()


def player_turn():
    
    # Det första som sker på spelarens tur är att koden kollar ifall spelaren har 0 eller mindre hp.
    # Om spelaren har 0 eller mindre hp, så är spelaren död och har förlorat
    # och då körs player_dead() funktionen som avslutar spelet.
    if player.hp <= 0:
        player_dead()
    
    # Den här biten kod används för spelarens damage potion.
    # När spelaren har druckit damage potionen så verkar den i två rundor.
    # Den här biten kod håller koll på hur många rundor som gått 
    # och när två rundor har gått så tas damage potion effekten bort.
    global turn_counter
    if turn_counter > 0:
        turn_counter -= 1
        if turn_counter == 0:
            player.dmg -= 5
    
    # En try och except används för felhantering.
    try:
        # Spelaren får ett val om vad de vill göra på sin runda.
        # Spelaren kan välja mellan 3 saker.
        # Nr 1 är Action, där spelaren kan välja på olika sätt att attackera.
        # Nr 2 är Inventory, där kan spelaren använda de items den har i sitt inventory.
        # Nr 3 är Status, där kan spelaren kolla statusen av spelaren och fienden.
        player_choice = int(input("\n1. Action\n2. Inventory\n3. Status\n==> "))
        if player_choice == 1:
            # Om spelaren valde val 1 så får den ett till val där den väljer hur den vill attackera, 
            # eller om spelaren har ångrat sig så kan den gå tillbaka.
            print("\n1. Sword Attack", {inventory.weapon("Sword") + player.dmg}," dmg\n2. Fist Attack", {player.dmg}, "\n3. Return")
            # En till try och except används för att kolla ifall spelaren har angett en siffra och inte något annat.
            try:
                action = int(input("==> "))
            except:
                print("\nError, expected number, got something else.")    
                time.sleep(2)
                player_turn()
            time.sleep(1)

            # Om spelaren valde val 1 så attackerar spelaren med sitt svärd 
            # och den skada svärdet gör plus den bas skada som spelaren gör läggs ihop och skickas in i metoden enemy.hit().
            # I den metoden så räknas det ut hur mycket skada fienden tar, subtraherar det från fiendens hp 
            # och skickar tillbaka hur mycket hp fienden har kvar.
            # Ifall fiendens hp blir 0 eller mindre så körs funktionen battle_end() och spelet avslutas.
            # Samtidigt så skickas attack typen standard med, det är en del av spelet som för nuvarandet inte används.
            if action == 1:
                enemy.hit(inventory.weapon("Sword") + player.dmg, "standard")
                if enemy.hp <=0:
                    battle_end()

            # Om spelaren valde val 2 så attackerare den med sin näve.
            # Samma sak som i val 1 sker, men enbart spelarens bas skada skickas in till enemy.hit()
            elif action == 2:
                enemy.hit(player.dmg, "standard")
                if enemy.hp <= 0:
                    battle_end()

            # Om spelaren valde val 3, så körs spelarens tur om på nytt och den kan välja något av de andra valen.
            elif action == 3:
                player_turn()

            # Om spelaren skrev in en siffra som inte används i något val, som var något annat än 1 till 3, 
            # så skrivs ett fel meddelande ut och spelarens tur körs om på nytt.
            else:
                print("Non exsistent choice chosen, try again.")
                player_turn()

            #När spelarens tur är över så går det över till fiendens tur.
            input("\nPress enter to continue")
            enemy_turn()
        
        elif player_choice == 2:
            # Om spelaren valde val 2 så frå spelaren nya val. Först så skrivs inventoryt ut och visar spelaren vad som finns i det.
            # Sen får spelaren välja om den vill använda något item, eller om den vill gå ur inventoryt.
            print("\n")
            inventory.show_inv()
            choice = int(input("\n1. Use Item\n2. Exit Inv\n==> "))
            if choice == 1:
                #Om spelaren valde val 1 så får den välja vilket item den vill använda.
                # När spelaren skrivit in siffran av det item den vill använda så körs en hel del kod igång.
                # Först så skapas variabeln x, som håller koll på hur många gånger lopparna körs och får värdet 1.
                # Sen så körs en for loop där variabeln item skapas 
                # och som körs igenom inventory.items som är en lista där det ligger olika dictionaries med items i sig.
                # I dictionarien så ligger det vad det är för typ av item, namnet av itemet och värdet av itemet.

                # Item får värdet av en dictionary som ligger i inventory.items listan. Det dictionariet körs sen i en till for lopp.
                # For loopen använder items() funktionen som kollar igenom ett dictionary 
                # och ger ut vad som finns i det alltså namnet och värdet. Den informationen läggs i variabelerna
                # a och b.
                # Sen kollar koden ifall den är på type delen av dictionariet, om den är det så läggs vad det är för type
                # in i variabeln type. Sen går den vidare i for loppen. Om den inte är på vad det är för type av item
                # så kör den effekten av itemet. Genoma att kolla vad det är för typ av item.
                # Sen är det fiendens tur.
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
                            del inventory.items[x-1]

                        elif type == "dmg_inc" and x == which_item:
                            player.dmg += b
                            turn_counter = 2
                            print("You drank the potion, you now deal 5 extra dmg for two turns\n")
                            del inventory.items[x-1]
                        x += 1
                enemy_turn()


            elif choice == 2:
                # Om spelaren inte vill använda ett item, så körs spelarens runda om på nytt och spelaren kan välja om.
                player_turn()
            else:
                #Om spelaren valde ett val som inte finns så körs spelarens runda om igen och den kan välja på nytt.
                print("Non exsistent choice chosen, try again.")
                time.sleep(2)
                player_turn()

        elif player_choice == 3:
            # Om spelaren valde val 3 så skrivs fiendens och spelarens statusar ut och sen körs spelarens runda om igen och den kan
            # attackera eller använda ett item.
            enemy_status()
            player_status()
            input("\nPress enter to continue")
            player_turn()

        else:
            # Om spelaren valde ett val som inte finns så körs spelarens runda om igen och den kan välja på nytt.
            print("Non exsistent choice chosen, try again.")
            time.sleep(2)
            player_turn()

    except ValueError:
        # Om spelaren valde något som inte var en siffra så skrivs ett fel meddelande ut och spelaren kan välja igen.
        print("\nError, expected number, got something else.")    
        time.sleep(2)
        player_turn()

def battle_end():
    # När striden är slut och spelaren har vunnit så sparas data till save.txt filen.
    # Den information som sparas är spelarens svärd och hur mycket skada den gör,
    # Vad som finns i spelarens inventory och vilken level spelaren är.
    # Först öppnas text filen på skriv läge.
    f = open('./save.txt', 'w', encoding='utf-8')
    # Sen konverteras informationen i form av variabler till strings och skrivs sen in i save filen.
    f.write(json.dumps(inventory.weapons)+'\n')
    f.write(json.dumps(inventory.items)+'\n')
    f.write(json.dumps(level+1))
    # Sen stängs filen och spelaren får ett gratulations meddelande. Sen avslutas all kod.
    f.close()
    print("You defeated the enemy!")
    exit()

def player_dead():
    # När striden är slut och spelaren har förlorat så öppnas save filen och 
    # all data som kan ha funnits där raderas och spelaren måste starta om från början.
    # Sen avslutas koden.
    f = open('./save.txt', 'w', encoding='utf-8')
    f.close()
    print("\n\nYou got killed! That's too bad!\nTry again.")
    exit()
    


