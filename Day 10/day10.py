
def part1(file, critical_cycle, step_cycles, n_steps):
    program = open(file).read().splitlines()
    signal = 1
    cycle = 0
    step_counter = 0
    signal_strengths = list()

    for line in program:
        if line[:4] == 'noop':
            cycle += 1
            if cycle == critical_cycle + step_counter * step_cycles:
                signal_strengths.append(signal * cycle)
                step_counter += 1
        else:
            for i in range(2):
                cycle += 1
                if cycle == critical_cycle + step_counter * step_cycles:
                    signal_strengths.append(signal * cycle)
                    step_counter += 1
                signal += int(line[5:]) if i == 1 else 0
        if cycle == n_steps:
            break

    return sum(signal_strengths)


def part2(file):
    program = open(file).read().splitlines()
    signal = 1
    cycle = 0
    crt = ''
    for line in program:
        if line[:4] == 'noop':
            crt += '#' if signal - 1 <= cycle % 40 <= signal + 1 else '.'
            cycle += 1
            crt += '\n' if cycle % 40 == 0 else ''
        else:
            for i in range(2):
                crt += '#' if signal - 1 <= cycle % 40 <= signal + 1 else '.'
                signal += int(line[5:]) if i == 1 else 0
                cycle += 1
                crt += '\n' if cycle % 40 == 0 else ''
    return crt


print('The sum of these signal strengths is', part1('input.txt', 20, 40, 5))
print(part2('input.txt'))


