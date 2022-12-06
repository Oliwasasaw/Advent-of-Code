

def signal(text, length):
    for x in range(len(text) - length - 1):
        if len(set(text[x:x + length])) == len(text[x:x + length]):
            print(x + length)
            break


def test(length):
    a = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    b = 'nppdvjthqldpwncqszvftbrmjlhg'
    c = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    d = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

    signal(a, length)
    signal(b, length)
    signal(c, length)
    signal(d, length)


def open_file():
    with open('Input_6.txt') as file:
        text = file.read()

    return text


if __name__ == "__main__":
    text = open_file()
    test(14)
    signal(text, 14)

