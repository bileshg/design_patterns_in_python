from abc import ABC, abstractmethod


class Creature(ABC):
    @property
    @abstractmethod
    def attack(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def defense(self):
        raise NotImplementedError
