import logging
from .commando import Commando as _Command

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = '1.0.0'

__all__ = ["commando"]

commando = _Command()
