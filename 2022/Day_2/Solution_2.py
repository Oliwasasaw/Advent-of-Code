import pandas as pd

with open('Day2.txt') as file:
    lst = [line.strip() for line in file]

w = 6
d = 3
l = 0

win_table = [[3+l, 1+l, 2+l],
             [1+d, 2+d, 3+d],
             [2+w, 3+w, 1+w]]

df = pd.DataFrame(win_table, index=['X', 'Y', 'Z'], columns=['A', 'B', 'C'])

total = 0
for x in lst:
    score = df.loc[x[2], x[0]]

    total = total + score

print(total)