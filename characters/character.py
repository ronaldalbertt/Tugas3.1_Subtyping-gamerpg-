from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, name, hp, attack_power):

        self._name = name
        self._hp = hp
        self._max_hp = hp
        self._attack_power = attack_power

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def attack_power(self):
        return self._attack_power

    @abstractmethod
    def attack(self, target):
        pass

    def take_damage(self, damage):

        self._hp -= damage

        if self._hp < 0:
            self._hp = 0

        print(f"{self._name} menerima {damage} damage!")

    def show_status(self):

        print(f"{self._name} | HP: {self._hp}/{self._max_hp}")

    def is_alive(self):
        return self._hp > 0