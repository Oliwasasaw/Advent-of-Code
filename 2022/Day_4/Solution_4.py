import re
import numpy as np


def section(lst):

    total = 0
    for x in lst:
        id_pair = re.split(',|-', x)
        id_pair = list(map(int, id_pair))

        test1 = np.sign(id_pair[2] - id_pair[0])
        test2 = np.sign(id_pair[3] - id_pair[1])

        if test1 != test2 or test1 == test2 == 0:
            total = total + 1

    return total


def section2(lst):
    total = 0
    for x in lst:
        id_pair = re.split(',|-', x)
        id_pair = list(map(int, id_pair))

        test1 = np.sign(id_pair[2] - id_pair[1])
        test2 = np.sign(id_pair[3] - id_pair[0])

        if test1 != test2 or test1 == 0 or test2 == 0:
            total = total + 1

    return total


def test():
    lst =   ['2-4,6-8',
             '2-3,4-5',
             '5-7,7-9',
             '2-8,3-7',
             '6-6,4-6',
             '2-6,4-8']

    output = section(lst)
    output2 = section2(lst)
    print(output, output2)


def open_file():
    with open('Day4.txt') as file:
        lst = [line.strip() for line in file]

    output = section(lst)
    output2 = section2(lst)
    print(output, output2)


if __name__ == "__main__":
    test()
    open_file()
