class InventorySystem:

    @staticmethod
    def add_item(player, item):

        player.inventory.append(item)

        print(f"{item.name} ditambahkan ke inventory")

    @staticmethod
    def remove_item(player, item):

        if item in player.inventory:

            player.inventory.remove(item)

            print(f"{item.name} dihapus dari inventory")

    @staticmethod
    def show_inventory(player):

        print("\n=== INVENTORY ===")

        if not player.inventory:
            print("Inventory kosong")
            return

        for index, item in enumerate(player.inventory, start=1):

            print(f"{index}. {item.name}")