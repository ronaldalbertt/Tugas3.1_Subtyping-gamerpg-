from systems.inventory_system import InventorySystem
from items.potion import Potion


class BattleSystem:

    def __init__(self, player, enemy):

        self.player = player
        self.enemy = enemy

    def start_battle(self):

        print("\n=== BATTLE START ===")

        while self.player.is_alive() and self.enemy.is_alive():

            self.player.show_status()
            self.enemy.show_status()

            print("\n1. Attack")
            print("2. Show Inventory")
            print("3. Use Potion")
            print("4. Exit Battle")

            choice = input("Pilih aksi: ")

            if choice == "1":

                self.player.attack(self.enemy)

            elif choice == "2":

                InventorySystem.show_inventory(self.player)
                continue

            elif choice == "3":

                potion_found = False

                for item in self.player.inventory:

                    if isinstance(item, Potion):

                        self.player.use_potion(item)

                        self.player.inventory.remove(item)

                        potion_found = True
                        break

                if not potion_found:
                    print("Tidak ada potion!")

                continue

            elif choice == "4":

                print("Player melarikan diri!")
                return

            else:

                print("Pilihan tidak valid!")
                continue

            if self.enemy.is_alive():

                self.enemy.attack(self.player)

        self.check_winner()

    def check_winner(self):

        print("\n=== BATTLE END ===")

        if self.player.is_alive():

            print(f"{self.player.name} menang!")

            self.enemy.drop_loot()

        else:

            print(f"{self.enemy.name} menang!")