from abc import ABC, abstractmethod


class Printer(ABC):
    """Interface for printers"""
    @abstractmethod
    def print(self, document: str):
        """Print the document content"""
        pass


class Scanner(ABC):
    """Interface for scanners"""
    @abstractmethod
    def scan(self, document: str):
        """Scan the document"""
        pass


class MyPrinter(Printer):
    """Printer implementation"""
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    """Photocopier implementation"""
    def print(self, document):
        print(document)

    def scan(self, document):
        print("your document has been scanned!")


def driver():
    """Driver function to demonstrate the functionality"""
    my_printer = MyPrinter()
    photocopier = Photocopier()

    my_document = "Test document"

    my_printer.print(my_document)
    photocopier.print(my_document)
    photocopier.scan(my_document)


if __name__ == "__main__":
    driver()
