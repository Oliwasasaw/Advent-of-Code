import pandas as pd
import numpy as np
with open('Input_12.txt') as file:
    lst = [line.strip() for line in file]

lst = [[*x] for x in lst]
lst = [[ord(x) - 96 for x in y] for y in lst]
start_lst = []

df = pd.DataFrame(lst)
i = 0
for x in lst:
    j = 0
    for y in x:
        if y == -13:
            start = [i, j]
            df.loc[start[0], start[1]] = 1
        if y == -27:
            end = [i, j]
            df.loc[end[0], end[1]] = 26
        if y == 1:
            start_lst.append([i, j])
        j = j + 1
    i = i + 1


class Maze:
    def __init__(self, maze):
        self.df = maze
        self.limit = list(maze.shape)
        self.network = pd.DataFrame(np.zeros((self.limit[0], self.limit[1])))


class Cell:
    def __init__(self, pos):
        self.pos = pos


def path_find(open_lst, maze):
    offset = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    maze.network.loc[start[0], start[1]] = 1

    while open_lst:
        pos_cur = open_lst.pop(0)
        cur_cell = Cell(pos_cur)

        for x in offset:
            pos_new = [pos_cur[0] + x[0], pos_cur[1] + x[1]]
            move = False
            if 0 <= pos_new[0] < maze.limit[0] and 0 <= pos_new[1] < maze.limit[1]:
                if maze.df.loc[pos_new[0], pos_new[1]] - maze.df.loc[cur_cell.pos[0], cur_cell.pos[1]] <= 1:
                    move = True

            if move and maze.network.loc[pos_new[0], pos_new[1]] == 0:
                open_lst.append(pos_new)
                maze.network.loc[pos_new[0], pos_new[1]] = maze.network.loc[pos_cur[0], pos_cur[1]] + 1
                if pos_new == end:
                    open_lst = []
                    break
    return maze


# Part 1
open_lst = [start]
maze_complete = path_find(open_lst, Maze(df))
output_1 = maze_complete.network.loc[end[0], end[1]] - 1

# Part 2
output_lst = []
i = 1
final = len(start_lst)
for x in start_lst:
    print(f'{i}/{final}')
    open_lst = [x]
    maze_complete = path_find(open_lst, Maze(df))

    output_lst.append(maze_complete.network.loc[end[0], end[1]])
    i = i + 1

output_lst = [i for i in output_lst if i != 0]
print(f'Part 1: {output_1}')
print(f'Part 2: {min(output_lst)}')
