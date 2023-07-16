from ._version import VERSION

__version__ = VERSION

# --------------------------------------------------------------------------- #
# Packages                                                                    #
# --------------------------------------------------------------------------- #

# import settings....

# --------------------------------------------------------------------------- #
# Classes                                                                     #
# --------------------------------------------------------------------------- #

# Required to parse version before build?
try:
    from .basesettings import BaseSettings
except ModuleNotFoundError:
    pass


# --------------------------------------------------------------------------- #
# Objects                                                                     #
# --------------------------------------------------------------------------- #
