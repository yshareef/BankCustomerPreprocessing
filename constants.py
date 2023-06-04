import os


class Constants:
    cwd = os.getcwd()  # dirname(abspath(__file__))
    BASE_DIR = os.path.dirname(cwd)
    DATA_DIR = os.path.join(cwd, 'data')
    CACHE_DIR = os.path.join(cwd, 'cache')
