"""
            [J] [Z] [G]
            [Z] [T] [S] [P] [R]
[R]         [Q] [V] [B] [G] [J]
[W] [W]     [N] [L] [V] [W] [C]
[F] [Q]     [T] [G] [C] [T] [T] [W]
[H] [D] [W] [W] [H] [T] [R] [M] [B]
[T] [G] [T] [R] [B] [P] [B] [G] [G]
[S] [S] [B] [D] [F] [L] [Z] [N] [L]
 1   2   3   4   5   6   7   8   9

I am just a human, reading this input
and transforming it accordingly is a
pain, I'll just hardcode it since it's
not that long
"""


def get_data_noob(file):
    starting_stacks = {1: ['R', 'W', 'F', 'H', 'T', 'S'], 2: ['W', 'Q', 'D', 'G', 'S'], 3: ['W', 'T', 'B'],
                       4: ['J', 'Z', 'Q', 'N', 'T', 'W', 'R', 'D'], 5: ['Z', 'T', 'V', 'L', 'G', 'H', 'B', 'F'],
                       6: ['G', 'S', 'B', 'V', 'C', 'T', 'P', 'L'], 7: ['P', 'G', 'W', 'T', 'R', 'B', 'Z'],
                       8: ['R', 'J', 'C', 'T', 'M', 'G', 'N'], 9: ['W', 'B', 'G', 'L']}
    rearrangements = list()
    for line in open(file, 'r').read().splitlines():
        line = line.split(' ')
        rearrangements.append((int(line[1]), int(line[3]), int(line[5])))
    return starting_stacks, rearrangements


def get_data_full_parse(file):
    pass


def rearrange(rearrangement, stacks, crate_mover_version=9000):
    n_boxes, og_stack, d_stack = rearrangement
    boxes_to_move = stacks[og_stack][:n_boxes]
    if crate_mover_version == 9001:
        boxes_to_move.reverse()
    for box in boxes_to_move:
        stacks[d_stack].insert(0, box)
        stacks[og_stack].pop(0)


def explore_stack_tops(stacks):
    result = ''
    for i in range(len(stacks)):
        if len(stacks[i+1]) > 0:
            result += stacks[i+1][0]
    return result


def exercise(file, crate_mover_version=9000):
    stacks, rearrangements = get_data_noob(file)
    print('INIT: ', stacks.values())
    print('\n\n')
    for rearrangement in rearrangements:
        rearrange(rearrangement, stacks, crate_mover_version)
        print('STEP: ', stacks.values())
        print('\n\n')
    return explore_stack_tops(stacks)


print('With CrateMover v9000 we get the top sequence:', exercise('input.txt'))
print('With CrateMover v9001 we get the top sequence:', exercise('input.txt', 9001))
