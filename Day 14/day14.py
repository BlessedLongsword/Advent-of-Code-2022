import numpy as np


def get_cave_data(file, sand_source):

    paths = list(map(lambda x: x.split(' -> '), open(file).read().splitlines()))
    paths = [list(map(lambda x: (int(x.split(',')[1]), int(x.split(',')[0])), path)) for path in paths]

    max_x, max_y = 0, 0
    for path in paths:
        for coord in path:
            max_x, max_y = max(max_x, coord[1]), max(max_y, coord[0])

    cave = np.zeros((2 * max_y, 2 * max_x), dtype=int)
    cave[sand_source] = 2
    for path in paths:
        for i, coord in enumerate(path):
            if i == 0:
                cave[coord] = 1
            else:
                if coord[0] != path[i-1][0]:
                    if coord[0] > path[i-1][0]:
                        cave[path[i-1][0]:coord[0]+1, coord[1]] = 1
                    else:
                        cave[coord[0]:path[i - 1][0]+1, coord[1]] = 1
                else:
                    if coord[1] > path[i-1][1]:
                        cave[coord[0], path[i-1][1]:coord[1]+1] = 1
                    else:
                        cave[coord[0], coord[1]:path[i - 1][1]+1] = 1

    return cave, max_y


def part1(cave, lower_layer, sand_source):
    sand_units = 0
    can_reach_bottom = True
    sand_position = sand_source

    while can_reach_bottom:
        i, j = sand_position
        if cave[i+1, j] == 0:
            sand_position = (i+1, j)
            if sand_position[0] >= lower_layer:
                can_reach_bottom = False
        else:
            if cave[i+1, j-1] == 0:
                sand_position = (i+1, j-1)
            elif cave[i+1, j+1] == 0:
                sand_position = (i+1, j+1)
            else:
                cave[sand_position] = 3
                sand_units += 1
                sand_position = sand_source

    return sand_units


def part2(cave, lower_layer, sand_source):
    cave[lower_layer+2, :] = 1
    sand_units = 0
    reached_source = False
    sand_position = sand_source


    while not reached_source:
        i, j = sand_position
        if cave[i + 1, j] == 0:
            sand_position = (i + 1, j)
            if sand_position[0] >= lower_layer:
                can_reach_bottom = False
        else:
            if cave[i + 1, j - 1] == 0:
                sand_position = (i + 1, j - 1)
            elif cave[i + 1, j + 1] == 0:
                sand_position = (i + 1, j + 1)
            else:
                cave[sand_position] = 3
                sand_units += 1
                reached_source = sand_position == sand_source
                sand_position = sand_source

    f, output = open("output.txt", 'w'), ''
    for i in range(lower_layer + 3):
        for j in range(100, 700):
            if cave[i, j] == 0:
                output += '.'
            elif cave[i, j] == 1:
                output += '#'
            elif cave[i, j] == 2:
                output += '+'
            else:
                output += 'O'
        output += '\n'
    f.write(output)
    f.close()

    return sand_units


_sand_source = (0, 500)
_cave, _lower_layer = get_cave_data('input.txt', _sand_source)
print(part1(_cave, _lower_layer, _sand_source), 'units of sand come to rest.')
_cave, _lower_layer = get_cave_data('input.txt', _sand_source)
print(part2(_cave, _lower_layer, _sand_source), 'units of sand come to rest.')

