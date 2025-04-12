import Live
from .SMK25 import SMK25


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return SMK25(c_instance)

# local variables:
# tab-width: 4
