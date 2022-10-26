from ast import Or
from multiprocessing.sharedctypes import Value
import os
from pydoc import plain
import intro
from battle import battle_start
import time
from minigame import minigame
import sys

def menu():
    try:
        choice = int(input("\nText Spelet"
        "\n---------"
        "\n1. New Game"
        "\n2. Continue"
        "\n3. Credits"
        "\n4. Fun Mini Game"
        "\n5. Exit"
        "\n ==>")) 
        if choice == 1:
            f = open('./save.txt', 'w', encoding='utf-8')
            f.close
            battle_start()
        elif choice == 2:
            battle_start()
            pass
        elif choice == 3:
            print("A game created by Lucas C.")
            time.sleep(3)
            menu()
        elif choice == 4:
            minigame()
        elif choice == 5:
            exit()
        else:
            print("\nNon existent choice chosen.")
            menu()
    except ValueError:
        print("Error, a number was expected, got something else.")
        menu()
menu()