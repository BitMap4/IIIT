from os     import listdir
from typing import Iterable
from random import shuffle, seed

def read_reviews(directory: str) -> Iterable[list[str]]:
    """return a list of reviews from the directory"""
    seed(177013)
    dir_list = listdir(directory)
    shuffle(dir_list)
    for file in dir_list:
        # n -= 1
        with open(directory + '/' + file) as f:
            # if not n: yield None
            # for x in f.read().split(): yield x
            yield f.read().split()

def count_reviews(directory: str) -> int:
    """return number of files in directory"""
    return len(listdir(directory))
