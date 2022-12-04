
def rucksack(lst):

    elf = []
    i = 0
    total = 0
    for x in lst:
        h1, h2 = x[:len(x)//2], x[len(x)//2:]
        match = set(h1) & set(h2)

        elf.append(','.join(map(str, match)))

        if elf[i].isupper():
            offset = 26
        else:
            offset = 0

        total = total + ord(elf[i].lower()) - 96 + offset
        i = i + 1

    return total


def rucksack2(lst):

    elf = []
    i = 0
    total = 0
    for x in range(0, len(lst) - 2, 3):
        s1, s2, s3 = lst[x], lst[x+1], lst[x+2]
        match = set(s1) & set(s2) & set(s3)

        elf.append(','.join(map(str, match)))

        if elf[i].isupper():
            offset = 26
        else:
            offset = 0

        total = total + ord(elf[i].lower()) - 96 + offset
        i = i + 1

    return total


def test():
    lst = ['vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw']

    total = rucksack(lst)
    total2 = rucksack2(lst)

    print(total, total2)


def open_file():
    with open('Input_3.txt') as file:
        lst = [line.strip() for line in file]

    total = rucksack(lst)
    total2 = rucksack2(lst)
    print(total, total2)


if __name__ == "__main__":
    test()
    open_file()
