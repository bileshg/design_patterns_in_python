from abc import ABC, abstractmethod


class Remote(ABC):
    def __init__(self, device):
        self._device = device

    @abstractmethod
    def power(self):
        raise NotImplementedError

    @abstractmethod
    def set_channel(self, channel):
        raise NotImplementedError


class BasicRemote(Remote):
    def __init__(self, device):
        super().__init__(device)

    def power(self) -> None:
        if self._device.is_on:
            self._device.power_off()
        else:
            self._device.power_on()

    def set_channel(self, channel) -> None:
        self._device.set_channel(channel)


class AdvancedRemote(Remote):
    def __init__(self, device):
        super().__init__(device)

    def power(self) -> None:
        if self._device.is_on:
            self._device.power_off()
        else:
            self._device.power_on()

    def set_channel(self, channel) -> None:
        self._device.set_channel(channel)
        print(f"Channel {channel} saved to favorites")
