from .env_selector import EnvironmentFactorySelector
from .testing_client import TestingClient

if __name__ == "__main__":
    # Example usage, change this to "staging" or "production" for different environments
    environment = "development"

    factory = EnvironmentFactorySelector.select_factory(environment=environment)
    client = TestingClient(factory=factory)

    # Get database connection
    database_connection = client.get_database_connection()
    print("Database Connection:", database_connection)

    # Get mock services
    mock_services = client.get_mock_services()
    print("Mock Services:", mock_services)
