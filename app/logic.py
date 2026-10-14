"""Task logic for the AgileTask expansion. Notifications are injected, not hard-coded."""

from abc import ABC, abstractmethod


class Notifier(ABC):
    """Interface for anything that can send a notification."""

    @abstractmethod
    def notify(self, message):
        """Send the message to whoever should receive it."""


class ConsoleNotifier(Notifier):
    """Spike notifier that prints messages to the console."""

    def notify(self, message):
        print(message)


class Task:
    """A single task in the AgileTask system."""

    def __init__(self, title, notifiers=None):
        self.title = title
        self.done = False
        self.notifiers = notifiers or []

    def complete(self):
        self.done = True
        for notifier in self.notifiers:
            notifier.notify(f"Task '{self.title}' completed")