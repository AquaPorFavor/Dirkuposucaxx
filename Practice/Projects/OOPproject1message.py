from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email: {message}")
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sms: {message}")
class DiscordNotification(Notification):
    def send(self, message):
        print(f"Discord: {message}")

class User:
    def __init__(self, name):
        self.name = name

    def send_notification(self, notification, message):
        print(f"{self.name} is sending a notification:")
        notification.send(message)

user = User("Lol")
discord = DiscordNotification()
sms = SMSNotification()
email = EmailNotification()

user.send_notification(email, "Hello!")
user.send_notification(sms, "Hello!")
user.send_notification(discord, "Hello!")