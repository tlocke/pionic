from pionic.core import load, loads, PionException, dumps, dump
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = [load, loads, PionException, dumps, dump]
