from items.item import Item


class Weapon(Item):

    def __init__(self, name, price, damage):

        super().__init__(name, price)

        self._damage = damage

    @property
    def damage(self):
        return self._damage

    def use(self):

        self.equip()

    def equip(self):

        print(f"Weapon {self.name} dipasang")