from characters.enemy import Enemy


class Goblin(Enemy):

    def __init__(self, name):

        super().__init__(name, 50, 10, 25)

        self._sneak_bonus = 5

    def attack(self, target):

        total_damage = self.attack_power + self._sneak_bonus

        print(f"{self.name} menggunakan Sneak Attack ke {target.name}!")

        target.take_damage(total_damage)