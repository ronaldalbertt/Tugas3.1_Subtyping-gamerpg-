from characters.player import Player
from characters.goblin import Goblin
from characters.dragon import Dragon

from items.weapon import Weapon
from items.potion import Potion

from systems.battle_system import BattleSystem
from systems.inventory_system import InventorySystem


def show_menu():

    print("\n=== RPG MENU ===")
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


def show_equipment(player):

    print("\n=== EQUIPMENT ===")

    if player.weapon:
        print(f"Weapon : {player.weapon.name}")
        print(f"Bonus Damage : {player.weapon.damage}")
    else:
        print("Belum memakai weapon")


def use_potion_menu(player):

    found_potion = None

    for item in player.inventory:

        if isinstance(item, Potion):
            found_potion = item
            break

    if found_potion:

        player.use_potion(found_potion)

        InventorySystem.remove_item(player, found_potion)

    else:
        print("Potion tidak tersedia!")


def equip_weapon_menu(player):

    found_weapon = None

    for item in player.inventory:

        if isinstance(item, Weapon):
            found_weapon = item
            break

    if found_weapon:

        player.equip_weapon(found_weapon)

    else:
        print("Weapon tidak tersedia!")


def shop_menu(player):

    print("\n=== SHOP ===")
    print("1. Buy Potion (50 Gold)")
    print("2. Buy Steel Sword (100 Gold)")
    print("0. Kembali")

    choice = input("Pilih item: ")

    if choice == "1":

        if player.gold >= 50:

            potion = Potion("Health Potion", 50, 30)

            player._gold -= 50

            InventorySystem.add_item(player, potion)

        else:
            print("Gold tidak cukup!")

    elif choice == "2":

        if player.gold >= 100:

            sword = Weapon("Steel Sword", 100, 20)

            player._gold -= 100

            InventorySystem.add_item(player, sword)

        else:
            print("Gold tidak cukup!")


def main():

    player = Player("Knight", 100, 15, 1)

    starter_sword = Weapon("Iron Sword", 100, 10)
    starter_potion = Potion("Health Potion", 50, 30)

    InventorySystem.add_item(player, starter_sword)
    InventorySystem.add_item(player, starter_potion)

    while True:

        show_menu()

        choice = input("Pilih menu: ")

        # STATUS
        if choice == "1":

            player.show_status()

            print(f"Level : {player.level}")
            print(f"Gold  : {player.gold}")

        # INVENTORY
        elif choice == "2":

            InventorySystem.show_inventory(player)

        # USE POTION
        elif choice == "3":

            use_potion_menu(player)

        # EQUIP WEAPON
        elif choice == "4":

            equip_weapon_menu(player)

        # FIGHT GOBLIN
        elif choice == "5":

            enemy = Goblin("Goblin Hijau")

            battle = BattleSystem(player, enemy)
            battle.start_battle()

        # FIGHT DRAGON
        elif choice == "6":

            enemy = Dragon("Dragon Api")

            battle = BattleSystem(player, enemy)
            battle.start_battle()

        # EQUIPMENT
        elif choice == "7":

            show_equipment(player)

        # REST
        elif choice == "8":

            player._hp = player.max_hp

            print("HP berhasil dipulihkan!")

        # SHOP
        elif choice == "9":

            shop_menu(player)

        # EXIT
        elif choice == "0":

            print("Game selesai.")
            break

        else:

            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()