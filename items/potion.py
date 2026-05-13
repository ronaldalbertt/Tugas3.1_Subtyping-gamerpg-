from items.item import Item


class Potion(Item):

    def __init__(self, name, price, heal_amount):

        super().__init__(name, price)

        self._heal_amount = heal_amount

    @property
    def heal_amount(self):
        return self._heal_amount

    def use(self):

        self.heal()

    def heal(self):

        print(f"Potion {self.name} memulihkan HP")