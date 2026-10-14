# Design Rationale

Records why key design decisions were made.

## Baseline

The `Task` class in `app/logic.py` represents the existing system. It prints a message when a task is completed, so notification behaviour is hard-coded inside the class.
## Notification spike

The hard-coded `print` in `Task.complete()` was replaced by injected `Notifier` objects. New notification channels can now be added without modifying `Task`, which follows the Open-Closed Principle and removes the rigidity found in the baseline.