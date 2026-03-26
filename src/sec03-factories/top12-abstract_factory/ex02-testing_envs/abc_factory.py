from abc import ABC, abstractmethod


class TestingEnvironmentFactory(ABC):
    """Abstract factory for Testing envs"""

    @abstractmethod
    def create_database_connection(self):
        pass

    @abstractmethod
    def create_mock_services(self):
        pass
