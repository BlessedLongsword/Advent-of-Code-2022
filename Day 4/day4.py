
def getData(file):
    pairs = [line.split(',') for line in open(file, 'r').read().splitlines()]
    return list(map(lambda x: [tuple(x[0].split('-')), tuple(x[1].split('-'))], pairs))


def exercise(file, number):
    assignment_pairs = getData(file)
    full_containment = 0
    for range1, range2 in assignment_pairs:
        range_values1 = set(range(int(range1[0]), int(range1[1]) + 1))
        range_values2 = set(range(int(range2[0]), int(range2[1]) + 1))
        range_intersections = range_values1.intersection(range_values2)
        if number == 1:
            full_containment += range_intersections == range_values1 or range_intersections == range_values2
        elif number == 2:
            full_containment += len(range_intersections) != 0
        else:
            return 'What the hell?'
    return full_containment


print('A range fully contains the other in', exercise('input.txt', 1), 'assignments')
print('Ranges overlap in', exercise('input.txt', 2), 'assignments')

