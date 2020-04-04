"""Exceptions used in the toppra library."""


class ToppraError(Exception):
    """A generic error class used in the toppra library."""
    pass


class BadInputVelocities(ToppraError):
    """Raise when given input velocity is invalid."""
    pass


class SolverNotFound(ToppraError):
    pass
