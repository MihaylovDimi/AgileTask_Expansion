"""Unit tests for the AgileTask logic."""

import unittest

from unittest.mock import Mock

from app.logic import Task


class TestTask(unittest.TestCase):

    def test_new_task_is_not_done(self):
        self.assertFalse(Task("Write report").done)

    def test_completing_task_marks_it_done(self):
        task = Task("Write report")
        task.complete()
        self.assertTrue(task.done)
        def test_completing_task_notifies_every_notifier(self):
        first, second = Mock(), Mock()
        Task("Write report", notifiers=[first, second]).complete()
        first.notify.assert_called_once_with("Task 'Write report' completed")
        second.notify.assert_called_once_with("Task 'Write report' completed")    