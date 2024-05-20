import os
import pathlib

base_directory = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
data_directory = os.path.join(base_directory, 'data')


def get_directory_absolute_path():
    """
    Return the absolute path of the root project based on this file.
    """
    return pathlib.Path(__file__).parent.parent.parent.resolve()
