from abc import ABC, abstractmethod
from typing import Any


class NotificationService(ABC):
    """Interface for notification methods"""

    @abstractmethod
    def send_notification(self, recipient: Any, message: str):
        pass


class EmailService(NotificationService):
    """Service to send emails"""

    def send_notification(self, recipient: str, message: str):
        # Implementation to send an email
        print(f"Email sent to '{recipient}': {message}")


class SMSService(NotificationService):
    """Service to send SMS messages"""

    def send_notification(self, recipient: str, message: str):
        # Implementation to send an SMS
        print(f"SMS sent to '{recipient}': {message}")


class PushNotificationService(NotificationService):
    """Service to send push notifications"""

    def send_notification(self, recipient: str, message: str):
        # Implementation to send a push notification
        print(f"Push notification sent to '{recipient}': {message}")


class NotificationServiceClient:
    """Notification client. Should only have a single instance per NotificationService implementation"""

    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def send_notification(self, recipient: Any, message: str):
        """Send the notification through the notification_service"""
        try:
            self.notification_service.send_notification(recipient, message)
        except Exception as e:
            print(f"Error sending notification to '{recipient}': {str(e)}")


def driver():
    """Driver function to demonstrate the usage of NotificationService"""
    email_service = EmailService()
    sms_service = SMSService()
    push_notification_service = PushNotificationService()

    client_email = NotificationServiceClient(email_service)
    client_sms = NotificationServiceClient(sms_service)
    client_push_notification = NotificationServiceClient(push_notification_service)

    client_email.send_notification("user@example.com", "Hello via email!")
    client_sms.send_notification("123456789", "Hello via SMS!")
    client_push_notification.send_notification("user", "Hello via push notification!")


if __name__ == "__main__":
    driver()
