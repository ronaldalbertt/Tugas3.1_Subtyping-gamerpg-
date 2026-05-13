from characters.player import Player
from characters.goblin import Goblin


def test_attack():

    player = Player("Knight", 100, 15, 1)
    goblin = Goblin("Goblin")

    player.attack(goblin)

    assert goblin._hp < 50

    print("Test attack berhasil!")


test_attack()