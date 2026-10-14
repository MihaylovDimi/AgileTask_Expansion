"""Task logic for the AgileTask system (baseline)."""


class Task:
    """A single task in the AgileTask system."""

    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True
        print(f"Task '{self.title}' completed")