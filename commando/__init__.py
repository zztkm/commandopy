import logging
from .commando import Commando as _Command

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = '0.2.0'

__all__ = ["commando"]

commando = _Command()
