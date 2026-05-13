from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, name, price):

        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @abstractmethod
    def use(self):
        pass