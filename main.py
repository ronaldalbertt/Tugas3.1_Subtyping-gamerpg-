from characters.player import Player
from characters.goblin import Goblin
from characters.dragon import Dragon

from items.weapon import Weapon
from items.potion import Potion

from systems.battle_system import BattleSystem
from systems.inventory_system import InventorySystem


# =========================
# UI / DISPLAY
# =========================

def clear_line():
    print("-" * 35)


def show_title():
    clear_line()
    print("        TEXT RPG GAME")
    clear_line()


def show_menu():
    print("\n[ MENU UTAMA ]")
    print("1. Lihat Status")
    print("2. Lihat Inventory")
    print("3. Gunakan Potion")
    print("4. Equip Weapon")
    print("5. Lawan Goblin")
    print("6. Lawan Dragon")
    print("7. Lihat Equipment")
    print("8. Rest / Heal")
    print("9. Shop")
    print("0. Exit")


def pause():
    input("\nTekan ENTER untuk lanjut...")


# =========================
# PLAYER INFO
# =========================

def show_status(player):

    clear_line()
    print("STATUS PLAYER")
    clear_line()

    player.show_status()

    print(f"Level : {player.level}")
    print(f"Gold  : {player.gold}")


def show_equipment(player):

    clear_line()
    print("EQUIPMENT")
    clear_line()

    if player.weapon:
        print(f"Weapon       : {player.weapon.name}")
        print(f"Bonus Damage : +{player.weapon.damage}")
    else:
        print("Belum memakai weapon.")


# =========================
# INVENTORY SYSTEM
# =========================

def use_potion_menu(player):

    potion_found = None

    for item in player.inventory:

        if isinstance(item, Potion):
            potion_found = item
            break

    if potion_found:

        player.use_potion(potion_found)
        InventorySystem.remove_item(player, potion_found)

    else:
        print("Potion tidak tersedia!")


def equip_weapon_menu(player):

    weapon_found = None

    for item in player.inventory:

        if isinstance(item, Weapon):
            weapon_found = item
            break

    if weapon_found:

        player.equip_weapon(weapon_found)

    else:
        print("Weapon tidak tersedia!")


# =========================
# BATTLE SYSTEM
# =========================

def fight_goblin(player):

    enemy = Goblin("Goblin Hijau")

    battle = BattleSystem(player, enemy)
    battle.start_battle()


def fight_dragon(player):

    enemy = Dragon("Dragon Api")

    battle = BattleSystem(player, enemy)
    battle.start_battle()


# =========================
# SHOP SYSTEM
# =========================

def shop_menu(player):

    while True:

        clear_line()
        print("SHOP")
        clear_line()

        print(f"Gold Kamu : {player.gold}")
        print("\n1. Health Potion  (50 Gold)")
        print("2. Steel Sword    (100 Gold)")
        print("0. Kembali")

        choice = input("\nPilih item: ")

        # BUY POTION
        if choice == "1":

            if player.gold >= 50:

                potion = Potion("Health Potion", 50, 30)

                player._gold -= 50

                InventorySystem.add_item(player, potion)

                print("Berhasil membeli Health Potion!")

            else:
                print("Gold tidak cukup!")

        # BUY WEAPON
        elif choice == "2":

            if player.gold >= 100:

                sword = Weapon("Steel Sword", 100, 20)

                player._gold -= 100

                InventorySystem.add_item(player, sword)

                print("Berhasil membeli Steel Sword!")

            else:
                print("Gold tidak cukup!")

        # EXIT SHOP
        elif choice == "0":

            break

        else:
            print("Pilihan tidak valid!")

        pause()


# =========================
# PLAYER ACTION
# =========================

def rest_player(player):

    player._hp = player.max_hp

    print("HP berhasil dipulihkan!")


# =========================
# GAME SETUP
# =========================

def create_player():

    player = Player("Knight", 100, 15, 1)

    starter_sword = Weapon("Iron Sword", 100, 10)
    starter_potion = Potion("Health Potion", 50, 30)

    InventorySystem.add_item(player, starter_sword)
    InventorySystem.add_item(player, starter_potion)

    return player


# =========================
# MAIN GAME LOOP
# =========================

def main():

    player = create_player()

    while True:

        show_title()
        show_menu()

        choice = input("\nPilih menu: ")

        # STATUS
        if choice == "1":

            show_status(player)
            pause()

        # INVENTORY
        elif choice == "2":

            clear_line()
            print("INVENTORY")
            clear_line()

            InventorySystem.show_inventory(player)

            pause()

        # USE POTION
        elif choice == "3":

            use_potion_menu(player)
            pause()

        # EQUIP WEAPON
        elif choice == "4":

            equip_weapon_menu(player)
            pause()

        # FIGHT GOBLIN
        elif choice == "5":

            fight_goblin(player)
            pause()

        # FIGHT DRAGON
        elif choice == "6":

            fight_dragon(player)
            pause()

        # EQUIPMENT
        elif choice == "7":

            show_equipment(player)
            pause()

        # REST / HEAL
        elif choice == "8":

            rest_player(player)
            pause()

        # SHOP
        elif choice == "9":

            shop_menu(player)

        # EXIT
        elif choice == "0":

            clear_line()
            print("Game selesai. Terima kasih sudah bermain!")
            clear_line()

            break

        # INVALID INPUT
        else:

            print("Pilihan tidak valid!")
            pause()


if __name__ == "__main__":
    main()