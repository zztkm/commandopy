import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = "2.1.0"

from .commando import Commando

__all__ = ["Commando"]