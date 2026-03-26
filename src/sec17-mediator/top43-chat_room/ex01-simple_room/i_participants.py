from abc import ABC, abstractmethod


class IParticipant(ABC):
    @abstractmethod
    def say(self, value: int):
        raise NotImplementedError

    @abstractmethod
    def receive(self, value: int):
        raise NotImplementedError
