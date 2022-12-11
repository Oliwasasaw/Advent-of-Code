import numpy as np
import pandas as pd


def rope_sim(rope_len, direct, distance):
    n_rows = 1000
    n_cols = 1000
    d = pd.DataFrame(np.zeros((n_rows, n_cols)))

    h_row = 500
    h_col = 500

    d.loc[h_row, h_col] = 1

    rope_lst = []
    for i in range(rope_len):
        rope_lst.append([h_row, h_col])

    i = 0
    for x in direct:
        for y in range(distance[i]):
            for z in range(rope_len):
                if z == 0:
                    if x == 'U':
                        h_row = h_row - 1
                    if x == 'D':
                        h_row = h_row + 1
                    if x == 'R':
                        h_col = h_col + 1
                    if x == 'L':
                        h_col = h_col - 1

                    h = [h_row, h_col]
                    rope_lst[z] = h

                else:
                    dif = list(np.subtract(rope_lst[z - 1], rope_lst[z]))

                    if (abs(dif[0]) + abs(dif[1])) == 2 and (dif[0] == 0 or dif[1] == 0):
                        t_row = rope_lst[z][0] + 1 * np.sign(dif[0])
                        t_col = rope_lst[z][1] + 1 * np.sign(dif[1])

                    elif (abs(dif[0]) + abs(dif[1])) == 3:
                        t_row = rope_lst[z][0] + 1 * np.sign(dif[0])
                        t_col = rope_lst[z][1] + 1 * np.sign(dif[1])

                    elif (abs(dif[0]) + abs(dif[1])) > 3:
                        t_row = rope_lst[z][0] + 1 * np.sign(dif[0])
                        t_col = rope_lst[z][1] + 1 * np.sign(dif[1])

                    else:
                        t_row = rope_lst[z][0]
                        t_col = rope_lst[z][1]

                    t = [t_row, t_col]
                    rope_lst[z] = t

                    if z == rope_len - 1:
                        d.loc[t_row, t_col] = 1
        i = i + 1

    return d.to_numpy().sum()


def open_file():
    with open('Input_9.txt') as file:
        lst = [line.split(' ') for line in file]

    return [x[0] for x in lst], [int(x[1]) for x in lst]


if __name__ == "__main__":
    direct, distance = open_file()
    output_1 = rope_sim(2, direct, distance)
    output_2 = rope_sim(10, direct, distance)

    print('Part 1: ' + str(output_1))
    print('Part 2: ' + str(output_2))
