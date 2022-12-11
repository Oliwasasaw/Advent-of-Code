
import pandas as pd

with open('Input_8.txt') as file:
    lst = [list(line.strip()) for line in file]

lst = [[int(x) for x in i] for i in lst]

row_len = len(lst)
col_len = len(lst[0])

data = pd.DataFrame(lst)

visible = col_len * 2 + (row_len - 2) * 2
record = 0
for i in range(1, row_len - 1):
    row = list(data.loc[i])
    for j in range(1, col_len - 1):
        a = data.loc[i, j]
        col = list(data.loc[:, j])

        temp_row = list(map(lambda x: x - a, row))
        temp_col = list(map(lambda x: x - a, col))

        l = temp_row[:j]
        r = temp_row[j+1:]
        u = temp_col[:i]
        d = temp_col[i+1:]

        if max(l) >= 0:
            l_new = reversed(l)
            res = next(x for x, val in enumerate(l_new) if val >= 0)
            score_1 = res + 1
        else:
            score_1 = len(l)

        if max(r) >= 0:
            res = next(x for x, val in enumerate(r) if val >= 0)
            score_2 = res + 1
        else:
            score_2 = len(r)

        if max(u) >= 0:
            u_new = reversed(u)
            res = next(x for x, val in enumerate(u_new) if val >= 0)
            score_3 = res + 1
        else:
            score_3 = len(u)

        if max(d) >= 0:
            res = next(x for x, val in enumerate(d) if val >= 0)
            score_4 = res + 1
        else:
            score_4 = len(d)

        score = score_1 * score_2 * score_3 * score_4

        if score > record:
            record = score

        if max(l) >= 0 and max(r) >= 0 and max(u) >= 0 and max(d) >= 0:
            pass
        else:
            visible = visible + 1

print('Part 1: ' + str(visible))
print('Part 2: ' + str(record))
