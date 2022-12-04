with open('Day1.txt') as file:
    lst = [line.strip() for line in file]

i = 0
total = 0
cal_lst = []
for x in lst:
    if x != '':
        total = total + int(x)

    else:
        cal_lst.append(total)
        total = 0

cal_lst.sort(reverse=True)
print(sum(cal_lst[:3]))