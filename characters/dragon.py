from characters.enemy import Enemy


class Dragon(Enemy):

    def __init__(self, name):

        super().__init__(name, 120, 20, 100)

        self._fire_damage = 15

    def attack(self, target):

        total_damage = self.attack_power + self._fire_damage

        print(f"{self.name} menggunakan Fire Breath ke {target.name}!")

        target.take_damage(total_damage)

    def special_attack(self, target):

        damage = 40

        print(f"{self.name} menggunakan SPECIAL ATTACK ke {target.name}!")

        target.take_damage(damage)