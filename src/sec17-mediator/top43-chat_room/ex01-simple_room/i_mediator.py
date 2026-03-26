from abc import ABC, abstractmethod

from .i_participants import IParticipant


class IMediator(ABC):
    @abstractmethod
    def join(self, participant: IParticipant):
        raise NotImplementedError

    @abstractmethod
    def broadcast(self, sender: IParticipant, message: str):
        raise NotImplementedError
