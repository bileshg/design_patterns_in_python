from abc import ABC, abstractmethod


class User:
    """
    A class to construct representations of user for a certain platform.
    """

    def __init__(self, username: str, email: str, phone_number: str):
        self._username = username
        self._email = email
        self._phone_number = phone_number

    @property
    def username(self) -> str:
        """
        A property for the username of the user.

        :return: the user's username
        """
        return self._username

    @property
    def email(self) -> str:
        """
        A property for the email address of the user.

        :return: the user's email address
        """
        return self._email

    @property
    def phone_number(self) -> str:
        """
        A property for the phone number of the user.

        :return: the user's phone number
        """
        return self._phone_number


class SenderInterface(ABC):
    """
    Interface to send messages. Each implementation should represent a new communication medium.
    """

    @abstractmethod
    def send(self, recipient_info: User, message: str):
        pass


class EmailSender(SenderInterface):
    """
    This class provides the shell for an email oriented implementation of the SenderInterface. The actual logic of
    sending emails is not implemented, instead a message suggesting the email is being sent is presented.
    """

    def __init__(self, *args, **kwargs): ...

    def send(self, recipient_info: User, message: str) -> None:
        """
        Sends the email message to a provided recipient.

        :param recipient_info: A user instance containing all info needed to send the email to the user.
        :param message: the actual email
        """
        print(
            f"Sending email to {recipient_info.username} at address {recipient_info.email}: {message}"
        )

    # implement email sending logic here


class SMSSender(SenderInterface):
    """
    This class provides the shell for an sms oriented implementation of the SenderInterface. The actual logic of
    sending messages via sms is not implemented, instead a message suggesting the sms is being sent is presented.
    """

    def __init__(self, *args, **kwargs): ...

    def send(self, recipient_info: User, message: str) -> None:
        """
        Sends the sms message to a provided recipient.

        :param recipient_info: A user instance containing all info needed to send the sms to the user.
        :param message: the actual sms
        """
        print(f"Sending SMS to {recipient_info.phone_number}: {message}")

    # implement SMS sending logic here


# other sender implementations can be added similarly


class UserManager:
    """
    Manages the registered users and allows to contact them via a provided SenderInterface implementation.
    """

    def __init__(self):
        self._users: dict[str, User] = {}

    def add_user(self, user: User) -> None:
        """
        Add a user to the registry.

        :param user: the User representation of the user you want to add to the registry,
        """
        self._users[user.username] = user

    def remove_user(self, user: User) -> None:
        """
        Permanently removes a user to the registry.

        :param user: the User representation of the user you want to remove from the registery,
        """
        del self._users[user.username]

    @property
    def usernames(self) -> list[str]:
        """
        Provides a list of the usernames of all registered users.
        """
        return list(self._users)

    def get_users(self) -> dict[str, User]:
        """
        A mapping of the registered User object and their usernames.
        """
        return self._users

    def send_message_to_all_users(self, sender: SenderInterface, message: str) -> None:
        """
        Sends a message to all users separately via the injection SenderInterface implementation.

        :param sender: the SenderInterface implementation
        :param message: the message to send to all users in the registry
        """
        for user in self._users.values():
            sender.send(recipient_info=user, message=message)


def driver():
    user1 = User(username="JohnDoe", email="john@example.com", phone_number="xxxxx")
    user2 = User(username="JaneDoe", email="jane@example.com", phone_number="xxxxx")

    user_manager = UserManager()
    user_manager.add_user(user1)
    user_manager.add_user(user2)

    print(user_manager.usernames)
    # send an email and a sms message to all users
    user_manager.send_message_to_all_users(
        sender=EmailSender(), message="Welcome to our emailing platform!"
    )
    user_manager.send_message_to_all_users(
        sender=SMSSender(), message="Welcome to our SMS platform!"
    )


if __name__ == "__main__":
    driver()
