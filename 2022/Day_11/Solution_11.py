
def monkey():
    M_0 = {
        'items': [65, 58, 93, 57, 66],
        'op': ['*', 7],
        'test': 19,
        'true': 6,
        'false': 4,
        'inspect': 0
    }

    M_1 = {
        'items': [76, 97, 58, 72, 57, 92, 82],
        'op': ['+', 4],
        'test': 3,
        'true': 7,
        'false': 5,
        'inspect': 0

    }

    M_2 = {
        'items': [90, 89, 96],
        'op': ['*', 5],
        'test': 13,
        'true': 5,
        'false': 1,
        'inspect': 0
    }

    M_3 = {
        'items': [72, 63, 72, 99],
        'op': ['^', 2],
        'test': 17,
        'true': 0,
        'false': 4,
        'inspect': 0
    }

    M_4 = {
        'items': [65],
        'op': ['+', 1],
        'test': 2,
        'true': 6,
        'false': 2,
        'inspect': 0
    }

    M_5 = {
        'items': [97, 71],
        'op': ['+', 8],
        'test': 11,
        'true': 7,
        'false': 3,
        'inspect': 0
    }

    M_6 = {
        'items': [83, 68, 88, 55, 87, 67],
        'op': ['+', 2],
        'test': 5,
        'true': 2,
        'false': 1,
        'inspect': 0
    }

    M_7 = {
        'items': [64, 81, 50, 96, 82, 53, 62, 92],
        'op': ['+', 5],
        'test': 7,
        'true': 3,
        'false': 0,
        'inspect': 0
    }

    lst = [M_0, M_1, M_2, M_3, M_4, M_5, M_6, M_7]

    return lst


def test():
    M_0 = {
        'items': [79, 98],
        'op': ['*', 19],
        'test': 23,
        'true': 2,
        'false': 3,
        'inspect': 0
    }

    M_1 = {
        'items': [54, 65, 75, 74],
        'op': ['+', 6],
        'test': 19,
        'true': 2,
        'false': 0,
        'inspect': 0
    }

    M_2 = {
        'items': [79, 60, 97],
        'op': ['^', 2],
        'test': 13,
        'true': 1,
        'false': 3,
        'inspect': 0
    }

    M_3 = {
        'items': [74],
        'op': ['+', 3],
        'test': 17,
        'true': 0,
        'false': 1,
        'inspect': 0
    }

    lst = [M_0, M_1, M_2, M_3]
    return lst


def op_worry(sym, mag, old):
    if sym == '*':
        return old * mag
    if sym == '+':
        return old + mag
    if sym == '^':
        return pow(old, mag)


def concern1(worry):
    return worry // 3


def concern2(worry, common):
    return worry % common


def test_worry(worry, div):
    return worry % div


def throw_worry(throw, m, key):
    m_catch = m[key]
    if m_catch == 0:
        lst[0]['items'].append(throw)
    if m_catch == 1:
        lst[1]['items'].append(throw)
    if m_catch == 2:
        lst[2]['items'].append(throw)
    if m_catch == 3:
        lst[3]['items'].append(throw)
    if m_catch == 4:
        lst[4]['items'].append(throw)
    if m_catch == 5:
        lst[5]['items'].append(throw)
    if m_catch == 6:
        lst[6]['items'].append(throw)
    if m_catch == 7:
        lst[7]['items'].append(throw)

    m['items'].pop(0)


lst = monkey()

common = 1
for x in lst:
    common = common * x['test']

for r in range(10000):
    for m in lst:
        for i in range(len(m['items'])):
            m['items'][0] = op_worry(m['op'][0], m['op'][1], m['items'][0])
            m['items'][0] = concern2(m['items'][0], common)
            test_output = test_worry(m['items'][0], m['test'])
            if test_output == 0:
                throw_worry(m['items'][0], m, 'true')
            else:
                throw_worry(m['items'][0], m, 'false')

            m['inspect'] = m['inspect'] + 1
    print(r)


num = []
for x in lst:
    num.append(x['inspect'])

num.sort()
print(num[-1] * num[-2])


