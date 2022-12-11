
def get_motions(file):
    return list(map(lambda x: (x[0], int(x[2:])), [line for line in open(file).read().splitlines()]))


def distance(p1, p2):
    return [abs(p1[0] - p2[0]), abs(p1[1] - p2[1])]


def move_head(state, visited, motion, knots):
    direction, steps = motion
    for i in range(steps):
        if direction == 'R':
            state['H'][0] += 1
        elif direction == 'L':
            state['H'][0] -= 1
        elif direction == 'U':
            state['H'][1] += 1
        elif direction == 'D':
            state['H'][1] -= 1
        for j in range(knots - 2):
            if j == 0:
                move_knot(state, visited, 'H', j)
            else:
                move_knot(state, visited, j - 1, j)
        if knots > 2:
            move_knot(state, visited, knots - 3, 'T')
        else:
            move_knot(state, visited, 'H', 'T')


def move_knot(state, visited, head, tail):
    ht_distance = distance(state[head], state[tail])
    if ht_distance[0] > 1:
        state[tail][0] += 1 if state[tail][0] < state[head][0] else -1
        if ht_distance[1] == 1:
            state[tail][1] += 1 if state[tail][1] < state[head][1] else -1
    if ht_distance[1] > 1:
        state[tail][1] += 1 if state[tail][1] < state[head][1] else -1
        if ht_distance[0] == 1:
            state[tail][0] += 1 if state[tail][0] < state[head][0] else -1
    if tail == 'T':
        visited.add(tuple(state[tail]))


def perform_motions(motions, knots):
    state = {'H': [0, 0],  'T': [0, 0]}
    for i in range(knots - 2):
        state[i] = [0, 0]
    visited_positions = {(0, 0)}
    for motion in motions:
        move_head(state, visited_positions, motion, knots)
    return len(visited_positions)


print('(Part 1) The tail of the rope visits', perform_motions(get_motions('input.txt'), 2), 'positions at least once.')
print('(Part 2) The tail of the rope visits', perform_motions(get_motions('input.txt'), 10), 'positions at least once.')
