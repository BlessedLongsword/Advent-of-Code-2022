
def get_packets(file, part):

    if not 1 <= part <= 2:
        print('Part has to be 1 or 2!')
        return 0

    lines = open(file).read().splitlines()
    packets = []

    for i in range(0, len(lines), 3):
        if part == 1:
            packets.append([eval(lines[i]), eval(lines[i + 1])])
        if part == 2:
            packets.append(eval(lines[i]))
            packets.append(eval(lines[i+1]))

    return packets


def compare(left, right):

    if isinstance(left, int) and isinstance(right, int):
        return left == right, left < right

    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)

    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

    else:
        n_left, n_right = len(left), len(right)
        exploring = True
        result = True
        for i in range(max(n_left, n_right)):
            if exploring:
                if n_left - i == 0 and n_right - i > 0:
                    return False, True
                if n_left - i > 0 and n_right - i == 0:
                    return False, False
                exploring, result = compare(left[i], right[i])
            else:
                break
        return exploring, result


def part1(packets):
    return sum([(i + 1) * int(compare(packets[i][0], packets[i][1])[1]) for i in range(len(packets))])


def part2(packets, divider1, divider2):

    if divider1 == divider2:
        print('Dividers must be different!')
        return 0

    divider1_position = 1 + int(compare(divider2, divider1)[1])
    divider2_position = 1 + int(compare(divider1, divider2)[1])

    for packet in packets:
        divider1_position += int(compare(packet, divider1)[1])
        divider2_position += int(compare(packet, divider2)[1])

    return divider1_position * divider2_position


print('The sum of the indices is', part1(get_packets('input.txt', 1)))
print('The decoder key is', part2(get_packets('input.txt', 2), [[2]], [[6]]))
