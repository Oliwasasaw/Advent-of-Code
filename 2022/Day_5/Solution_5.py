import re

with open('Input_5.txt') as file:
    text = file.read()
    lst = text.split("\n")

depth = lst.index(' 1   2   3   4   5   6   7   8   9')
crates_initial = lst[:depth]
move_initial = lst[depth + 2:]

moves = [(re.findall('\d+', x)) for x in move_initial]
moves = [[int(x) for x in group] for group in moves]

crates = []
for x in crates_initial:
    temp = re.sub(' {4}', '-', x).replace(' ', '').replace('[', '').replace(']', '')
    temp = temp + '-' * (9 - len(temp))
    crates.append(temp)

cols = []
for x in range(9):
    cols.append([item[x] for item in crates if item[x] != '-'])

for x in moves:
    amount, start, end = x[0], x[1] - 1, x[2] - 1
    pick = cols[start][:amount]
    pick.reverse()
    del cols[start][:amount]
    cols[end] = pick + cols[end]

output = [item[0] for item in cols]
print(''.join(output))
