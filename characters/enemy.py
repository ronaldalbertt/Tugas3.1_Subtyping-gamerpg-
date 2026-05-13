from abc import ABC
from characters.character import Character


class Enemy(Character, ABC):

    def __init__(self, name, hp, attack_power, reward):

        super().__init__(name, hp, attack_power)

        self.reward = reward

    def drop_loot(self):

        print(f"{self.name} menjatuhkan {self.reward} gold!")