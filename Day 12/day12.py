import numpy as np
import heapq


def get_heightmap(file):
    lines = open(file).read().splitlines()
    heightmap = np.zeros((len(lines), len(lines[0])), dtype=int)
    start, target = None, None
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'S':
                heightmap[i, j] = 0
                start = (i, j)
            elif char == 'E':
                heightmap[i, j] = ord('z') - ord('a') + 1
                target = (i, j)
            else:
                heightmap[i, j] = ord(char) - ord('a') + 1
    return heightmap, start, target


def get_possible_moves(heightmap, position, visited):
    possible_moves = list()
    i, j = position
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for di, dj in directions:
        if not any([i + di < 0, i + di > heightmap.shape[0] - 1, j + dj < 0, j + dj > heightmap.shape[1] - 1]):
            if heightmap[i + di, j + dj] - heightmap[i, j] <= 1 and (i + di, j + dj) not in visited:
                possible_moves.append((i + di, j + dj))
    return possible_moves


def dijkstra(heightmap, start, target):
    dist = dict()
    prev = dict()
    visited = set()
    pq = []

    dist[start] = 0
    prev[start] = None
    heapq.heappush(pq, (dist[start], start))
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if (i, j) != start:
                dist[(i, j)] = float('inf')
                prev[(i, j)] = None

    while pq:
        priority, position = heapq.heappop(pq)
        visited.add(position)
        if position == target:
            break
        for move in get_possible_moves(heightmap, position, visited):
            alt = dist[position] + 1
            if alt < dist[move]:
                dist[move] = alt
                prev[move] = position
                heapq.heappush(pq, (alt, move))

    return dist, prev


def part1(heightmap, start, target):
    dist, prev = dijkstra(heightmap, start, target)
    return dist[target]


def part2(heightmap, start, target):
    min_fewest_steps = part1(heightmap, start, target)
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if heightmap[i, j] == 1:
                min_fewest_steps = min(part1(heightmap, (i, j), target), min_fewest_steps)
    return min_fewest_steps


data_values = get_heightmap('input.txt')
print('(Part 1) The fewest steps required are', part1(*data_values), 'steps.')
print('(Part 2) The fewest steps required are', part2(*data_values), 'steps.')



