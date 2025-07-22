from abc import ABC, abstractmethod
from typing import Any, Sequence


class Powerable(ABC):
    """Interface for devices that can be turned on and off"""

    def __enter__(self):
        """Context manager to allow proper device usage"""
        self.turn_on()
        return self

    def __exit__(self, *args, **kwargs):
        """Context manager to allow proper device usage"""
        self.turn_off()

    @abstractmethod
    def turn_on(self):
        """Turns on the device"""
        pass

    @abstractmethod
    def turn_off(self):
        """Turns off the device"""
        pass


class ChannelChangeable(Powerable, ABC):
    """Interface for Powerable devices that can switch between channels"""
    @abstractmethod
    def change_channel(self, channel: int):
        """Change the channel on which the device currently operates"""
        pass


class VolumeControllable(Powerable, ABC):
    """Interface for Powerable devices that can adjust volume levels"""
    @abstractmethod
    def adjust_volume(self, volume: int):
        """Change the volume which the device currently produces"""
        pass


class Command(ABC):
    """Interface for command structuring"""
    @abstractmethod
    def execute(self, on: Any):
        """Executes a command"""
        pass


class RemoteControl:
    """Implements the execution orchestration of the commands"""
    def __init__(self, device: Powerable):
        self.device = device

    def __enter__(self):
        """Implements the context managers of the object"""
        self.device.__enter__()
        return self

    def __exit__(self, *args, **kwargs):
        """Implements the context managers of the object"""
        self.device.__exit__()

    def operate(self, commands: Sequence[Command]):
        """Executes a list of commands"""
        for command in commands:
            command.execute(self.device)


class MethodCommand(Command):
    """Class to execute commands on a object"""
    def __init__(self, method: str, *args, **kwargs):
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def execute(self, on: Any):
        """Executes the command on the object"""
        getattr(on, self.method)(*self.args, **self.kwargs)


class TV(ChannelChangeable, VolumeControllable):
    """Allows for TV devices"""
    def turn_on(self):
        print("TV turned on")

    def turn_off(self):
        print("TV turned off")

    def change_channel(self, channel: int):
        print(f"TV channel changed to {channel}")

    def adjust_volume(self, volume: int):
        print(f"TV volume adjusted to {volume}")


class Stereo(VolumeControllable):
    """Allows for Stereo devices"""
    def turn_on(self):
        print("Stereo turned on")

    def turn_off(self):
        print("Stereo turned off")

    def adjust_volume(self, volume: int):
        print(f"Stereo volume adjusted to {volume}")

if __name__ == "__main__":

    tv_commands = [
        MethodCommand(method="change_channel", **{"channel": 5}),
        MethodCommand(method="adjust_volume", **{"volume": 20}),
    ]

    stereo_commands = [
        MethodCommand("adjust_volume", 20),
    ]

    tv_remote = RemoteControl(TV())
    with tv_remote:
        tv_remote.operate(tv_commands)

    with RemoteControl(Stereo()) as stereo_remote:
        stereo_remote.operate(stereo_commands)

    with TV() as tv:
        tv.change_channel(channel=4)
