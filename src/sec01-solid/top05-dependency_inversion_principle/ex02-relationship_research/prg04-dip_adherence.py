from enum import Enum
from typing import Iterator, Self
from abc import ABC, abstractmethod


class Person:
    """Definition of a person"""

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, value: Self) -> bool:
        return self.name == value.name


class Relationship(Enum):
    """Enum to define the possible relationships"""

    PARENT = 0
    CHILD = 1
    SIBLING = 2


class RelationshipBrowser(ABC):
    """Interface for relationship browsers"""

    @abstractmethod
    def find_all_children_of(self, parent: Person) -> Iterator[Person]:
        pass


class Relationships(RelationshipBrowser):
    """Enables finding of relationships"""

    relations = []

    def add_parent_and_child(self, parent: Person, child: Person):
        """Enables construction of the family tree"""
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, parent: Person) -> Iterator[Person]:
        """Finds all children of parent by name"""
        return (
            r[2]
            for r in self.relations
            if r[0] == parent and r[1] == Relationship.PARENT
        )


class Research:
    """Enables heritage research"""

    def __init__(self, browser: RelationshipBrowser):
        self.browser = browser

    def find_children_of(self, parent: Person):
        """Find children of a parent"""
        if children := self.browser.find_all_children_of(parent):
            for p in children:
                print(f"{parent} has a child called {p}")


def driver():
    """Driver function to demonstrate the functionality"""
    parent = Person("John")
    child1 = Person("Chris")
    child2 = Person("Matt")

    # low-level module
    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    research = Research(relationships)
    research.find_children_of(parent)


if __name__ == "__main__":
    driver()
