from sys import argv
from itertools import count
from itertools import cycle


def my_gen_count(start, stop):
    try:
        for el in count(int(start)):
            print(el)
            if el == int(stop):
                break
    except ValueError:
        print(f"Wrong input")


def my_gen_cycle(ls, counter):
    ls = list(ls)
    counter = int(counter)
    iterator = cycle(ls)
    while counter != 0:
        print(next(iterator))
        counter -= 1


my_gen_count(1, 5)
my_gen_cycle("abc", 5)

