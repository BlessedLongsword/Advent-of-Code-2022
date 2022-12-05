def get_data(file):
    full_input = open(file).read().splitlines()
    split_point = full_input.index('')
    input_stacks, input_rearrangements = full_input[:split_point], full_input[split_point+1:]
    starting_stacks, rearrangements = dict(), list()
    for line in input_rearrangements:
        line = line.split(' ')
        rearrangements.append((int(line[1]), int(line[3]), int(line[5])))
    for stack in input_stacks[-1].split():
        starting_stacks[int(stack)] = list()
    for line in input_stacks:
        counter = 0
        for i in range(1, len(line), 4):
            counter += 1
            if not line[i] == ' ':
                starting_stacks[counter].append(line[i])
    return starting_stacks, rearrangements


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
    stacks, rearrangements = get_data(file)
    for rearrangement in rearrangements:
        rearrange(rearrangement, stacks, crate_mover_version)
    return explore_stack_tops(stacks)


print('With CrateMover v9000 we get the top sequence:', exercise('input.txt'))
print('With CrateMover v9001 we get the top sequence:', exercise('input.txt', 9001))
