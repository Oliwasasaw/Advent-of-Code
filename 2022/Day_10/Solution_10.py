import numpy as np
import pandas as pd

with open('Input_10.txt') as file:
    lst = [line.split(' ') for line in file]
    lst = [x[-1].rstrip() for x in lst]


def CPU(memory, count, reg, cycle, i, d):

    for x in range(count):
        reg = reg + memory[-1]
        memory[-1] = memory[1]
        memory[1] = memory[0]
        memory[0] = 0

        cycle = cycle + 1

        row = np.floor(i / 40)
        print(row, i-(40*row), i)
        if i - (40*row) == reg or i - (40*row) == reg-1 or i - (40*row) == reg+1:

            d.loc[row, i - (40*row)] = '#'

        i = i + 1

    return memory, reg, cycle, i, d


reg = 1
cycle = 0
memory = [0, 0, 0]
total = 0
i = 0

n_rows = 6
n_cols = 40
d = pd.DataFrame(np.zeros((n_rows, n_cols)))
d = d.replace(0, '.')

for x in lst:
    if x == 'noop':
        count = 1
        push = 0
    else:
        count = 2
        push = x

    memory[0] = int(push)

    memory, reg, cycle, i, d = CPU(memory, count, reg, cycle, i, d)

print(d.to_string())

