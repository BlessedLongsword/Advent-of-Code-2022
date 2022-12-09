
def get_motions(file):
    return list(map(lambda x: (x[0], int(x[2])), [line for line in open(file).read().splitlines()]))


def move_head(state, visited, move):
    direction, steps = move
    for i in range(steps):
        if direction == 'R':
            state['H'][0] += 1
        elif direction == 'L':
            state['H'][0] -= 1
        elif direction == 'U':
            state['H'][1] += 1
        elif direction == 'D':
            state['H'][1] -= 1
        move_tail(state, visited)
        print(state.items())


def distance(p1, p2):
    return [abs(p1[0] - p2[0]), abs(p1[1] - p2[1])]


def move_tail(state, visited):
    ht_distance = distance(state['H'], state['T'])
    if ht_distance[0] > 1:
        state['T'][0] += 1 if state['T'][0] < state['H'][0] else -1
        if ht_distance[1] == 1:
            state['T'][1] += 1 if state['T'][1] < state['H'][1] else -1
    elif ht_distance[1] > 1:
        state['T'][1] += 1 if state['T'][1] < state['H'][1] else -1
        if ht_distance[0] == 1:
            state['T'][0] += 1 if state['T'][0] < state['H'][0] else -1
    visited.add(tuple(state['T']))


def perform_motions(motions):
    state = {'H': [0, 0], 'T': [0, 0]}
    visited_positions = {(0, 0)}
    for motion in motions:
        move_head(state, visited_positions, motion)
    return len(visited_positions)


print(perform_motions(get_motions('input.txt')))
