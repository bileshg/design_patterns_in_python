from .i_mediator import IMediator
from .i_participants import IParticipant


class AdditionRoom(IMediator):
    def __init__(self):
        self.participants: list[IParticipant] = []

    def join(self, participant: IParticipant):
        self.participants.append(participant)

    def broadcast(self, sender: IParticipant, message: str):
        for participant in self.participants:
            if participant is sender:
                continue
            participant.receive(value=int(message))
