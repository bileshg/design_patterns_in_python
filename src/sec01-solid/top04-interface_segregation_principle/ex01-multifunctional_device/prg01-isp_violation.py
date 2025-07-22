from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        ...

    def fax(self, document):
        ...

    def scan(self, document):
        ...


class OldFashionedPrinter(Machine):
    def print(self, document):
        ...

    def fax(self, document):
        ...

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')

# Violates the ISP by using an interface for OldFashionedPrinter
# when it does not support all functionalities from Machine
