__author__ = 'PerminovMA@live.ru'

from time import time
from random import randint


def generate_filename(filename):
    """returns the new name for save on the server"""
    return str(time()).replace('.', '_') + str(randint(0, 100000)) + filename[filename.rfind('.'):]