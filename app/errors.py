"""Declaration of classes representing various exception types."""


class TaskError(Exception):
    """There was an error during task execution."""


class NotABugTaskError(TaskError):
    """Task error, but not a bug in the code.

    This exception will be ignored by Sentry.
    """


class F8AConfigurationException(Exception):
    """There was an error during handling configuration."""
