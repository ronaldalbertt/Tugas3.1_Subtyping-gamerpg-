from characters.character import Character
class Player(Character):

    def __init__(self, name, hp, attack_power, level):

        super().__init__(name, hp, attack_power)

        self._level = level
        self._gold = 0

        self.inventory = []
        self.weapon = None

    @property
    def level(self):
        return self._level

    @property
    def gold(self):
        return self._gold

    def add_gold(self, amount):

        self._gold += amount

    def attack(self, target):

        print(f"{self.name} menyerang {target.name}!")

        target.take_damage(self.attack_power)

    def equip_weapon(self, weapon):

        if self.weapon is not None:
            self._attack_power -= self.weapon.damage

        self.weapon = weapon
        self._attack_power += weapon.damage

        print(f"{self.name} memakai weapon {weapon.name}")

    def use_potion(self, potion):

        self._hp += potion.heal_amount

        if self._hp > self._max_hp:
            self._hp = self._max_hp

        print(f"{self.name} menggunakan potion!")

    def heal_full(self):

        self._hp = self._max_hp

        print(f"{self.name} kembali ke HP penuh!")