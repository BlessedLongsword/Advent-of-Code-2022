
def get_notes(file):
    lines = open(file).read().splitlines()
    counter = 0
    notes = dict()
    while counter < len(lines):
        monkey = int(lines[counter][7:-1])
        starting_items = list(map(int, lines[counter + 1][18:].split(', ')))
        operation = (lines[counter + 2][23], lines[counter + 2][25:])
        test = int(lines[counter + 3][21:])
        test_result = (int(lines[counter + 5][30:]), int(lines[counter + 4][29:]))
        notes[monkey] = {'starting_items': starting_items, 'operation': operation,
                         'test': test, 'test_result': test_result, 'inspections': 0}
        counter += 7
    return notes


def execute_monkey_turn(notes, monkey, divisors_prod, part):
    for item in notes[monkey]['starting_items']:
        operation, number = notes[monkey]['operation']
        divisor = notes[monkey]['test']
        target_monkeys = notes[monkey]['test_result']
        number = item if number == 'old' else int(number)
        item = manage_worry(item, number, operation, divisors_prod, part)
        notes[target_monkeys[int(item % divisor == 0)]]['starting_items'].append(item)
        notes[monkey]['inspections'] += 1
    notes[monkey]['starting_items'] = []


def manage_worry(worry, number, operation, divisors_prod, part):
    if part == 1:
        worry = worry + number if operation == '+' else worry * number
        return int(worry / 3)
    elif part == 2:
        return (worry + number) % divisors_prod if operation == '+' else (worry * number) % divisors_prod
    else:
        print('Something is wrong...')
        return 0


def get_monkey_business(notes, n_rounds, part):
    divisors_prod = 1
    for k in range(len(notes)):
        divisors_prod *= notes[k]['test']
    for _ in range(n_rounds):
        for i in range(len(notes)):
            execute_monkey_turn(notes, i, divisors_prod, part)
    monkey_inspections = [notes[j]['inspections'] for j in range(len(notes))]
    monkey_inspections.sort()
    return monkey_inspections[-1] * monkey_inspections[-2]


print('The monkey business after 20 rounds is', get_monkey_business(get_notes('input.txt'), 20, 1))
print('The monkey business after 10000 rounds is', get_monkey_business(get_notes('input.txt'), 10000, 2))

