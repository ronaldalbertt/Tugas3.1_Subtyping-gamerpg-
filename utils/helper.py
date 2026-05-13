import os
import time


def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


def pause():

    input("\nTekan ENTER untuk melanjutkan...")


def game_title():

    print("""
=================================
        TERMINAL RPG GAME
=================================
""")


def battle_separator():

    print("\n-----------------------------\n")