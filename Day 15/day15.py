
def get_report(file):
    report = dict()

    for line in open(file).read().splitlines():
        sensor_slice, beacon_slice = line.split(':')
        x_sensor, y_sensor = sensor_slice[10:].split(', ')
        x_beacon, y_beacon = beacon_slice[22:].split(', ')
        p_sensor = (int(x_sensor[2:]), int(y_sensor[2:]))
        p_beacon = (int(x_beacon[2:]), int(y_beacon[2:]))
        report[p_sensor] = (p_beacon, manhattan_dist(p_sensor, p_beacon))

    return report


def manhattan_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def get_extremes(report):
    x_min, y_min, x_max, y_max = float('inf'), float('inf'), 0, 0

    for key, value in report.items():
        x_sensor, y_sensor = key
        x_beacon, y_beacon = value[0]
        x_min = min(x_min, x_sensor, x_beacon)
        y_min = min(y_min, y_sensor, y_beacon)
        x_max = max(x_max, x_sensor, x_beacon)
        y_max = max(y_max, y_sensor, y_beacon)

    return x_min, y_min, x_max, y_max


def visualize_report(report):
    visualization = ''
    x_min, y_min, x_max, y_max = get_extremes(report)
    max_dist = max([value[1] for value in report.values()])

    sensors_set = set(report.keys())
    beacons_set = set([value[0] for value in report.values()])

    for j in range(y_min - max_dist, y_max + max_dist + 1):
        for i in range(x_min - max_dist, x_max + max_dist + 1):
            if (i, j) in sensors_set:
                visualization += 'S'
            elif (i, j) in beacons_set:
                visualization += 'B'
            else:
                in_range = False
                for sensor in report.keys():
                    if manhattan_dist((i, j), sensor) <= report[sensor][1]:
                        visualization += '#'
                        in_range = True
                        break
                if not in_range:
                    visualization += '.'

        visualization += '\n'

    f = open('visualization.txt', 'w')
    f.write(visualization)
    f.close()


def add_interval(intervals, new_interval, start, end):
    if not intervals:
        i_start, i_end = new_interval
        if i_end >= start:
            i_start = start if i_start < start else i_start
            if i_start <= end:
                i_end = end if i_end > end else i_end
                intervals.append((i_start, i_end))
    else:
        i_start, i_end = new_interval
        if i_end >= start:
            i_start = start if i_start < start else i_start
            if i_start <= end:
                i_end = end if i_end > end else i_end
                intervals.append((i_start, i_end))
                intervals = fix_overlaps(intervals)
    return intervals


def fix_overlaps(intervals):
    fixed_intervals = list()
    current_min = float('inf')
    current_min_idx = 0
    for i, interval in enumerate(intervals):
        if interval[0] < current_min:
            current_min = interval[0]
            current_min_idx = i
    interval_start, interval_end = intervals.pop(current_min_idx)
    while intervals:
        interval_start, interval_end = fix_first_component(intervals, fixed_intervals, interval_start, interval_end)
    fixed_intervals.append((interval_start, interval_end))
    return fixed_intervals


def fix_first_component(intervals, fixed_intervals, interval_start, interval_end):

    if not intervals:
        return interval_start, interval_end

    current_min = float('inf')
    current_min_idx = 0
    for i, interval in enumerate(intervals):
        if interval[0] < current_min:
            current_min = interval[0]
            current_min_idx = i
    if current_min <= interval_end:
        if intervals[current_min_idx][1] > interval_end:
            interval_end = intervals[current_min_idx][1]
            intervals.pop(current_min_idx)
            return fix_second_component(intervals, fixed_intervals, interval_start, interval_end)
        else:
            intervals.pop(current_min_idx)
            return fix_first_component(intervals, fixed_intervals, interval_start, interval_end)
    else:
        fixed_intervals.append((interval_start, interval_end))
        interval_start, interval_end = intervals.pop(current_min_idx)
        return interval_start, interval_end


def fix_second_component(intervals, fixed_intervals, interval_start, interval_end):

    if not intervals:
        return interval_start, interval_end

    current_min = float('inf')
    current_min_idx = 0
    for i, interval in enumerate(intervals):
        if interval[1] < current_min:
            current_min = interval[1]
            current_min_idx = i
    if current_min <= interval_end:
        intervals.pop(current_min_idx)
        return fix_second_component(intervals, fixed_intervals, interval_start, interval_end)
    else:
        if intervals[current_min_idx][0] <= interval_end:
            intervals.pop(current_min_idx)
            interval_end = current_min
            return fix_first_component(intervals, fixed_intervals, interval_start, interval_end)
        else:
            fixed_intervals.append((interval_start, interval_end))
            interval_start, interval_end = intervals.pop(current_min_idx)
            return interval_start, interval_end


def part1(report, row):
    discarded_positions = set()
    sensors_set = set(report.keys())
    beacons_set = set([value[0] for value in report.values()])
    for sensor in sensors_set:
        distance = report[sensor][1]
        if sensor[1] + distance >= row or sensor[1] - distance <= row:
            rel_distance = distance - abs(row - sensor[1])
            discarded_positions.update([(i, row)
                                        for i in range(sensor[0] - rel_distance, sensor[0] + rel_distance + 1)])
    return len(discarded_positions.difference(sensors_set.union(beacons_set)))


def part2(report, start, end):
    from tqdm import tqdm

    sensors_set = set(report.keys())
    found_beacon_spot = False
    x_beacon, y_beacon = 0, 0
    for row in tqdm(range(start, end)):
        discarded_ranges = list()
        if found_beacon_spot:
            break
        for sensor in sensors_set:
            distance = report[sensor][1]
            if sensor[1] + distance >= row or sensor[1] - distance <= row:
                rel_distance = distance - abs(row - sensor[1])
                discarded_ranges = add_interval(discarded_ranges, (sensor[0] - rel_distance,
                                                                   sensor[0] + rel_distance), start, end)
        prev_range_end = discarded_ranges[0][1]
        for _range in discarded_ranges[1:]:
            if prev_range_end + 1 != _range[1]:
                x_beacon, y_beacon = _range[0] - 1, row
                found_beacon_spot = True
                break

    return x_beacon * end + y_beacon


_report = get_report('input.txt')
_row = 2000000
# The visualize method is just for show with small inputs
# visualize_report(_report)
print('In the row', _row, 'there are', part1(_report, _row), 'positions where a beacon cannot be present.')
print('The tuning frequency is', part2(_report, 0, 4000000))
