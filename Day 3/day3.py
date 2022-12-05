
def exercise1(file):
    rucksacks = open(file, 'r').read().splitlines()
    priority_sum = 0

    for rucksack in rucksacks:
        compartment1 = set(rucksack[:len(rucksack)//2])
        compartment2 = set(rucksack[len(rucksack)//2:])
        odd_one_out = compartment1.intersection(compartment2)
        if len(odd_one_out) > 1 or len(odd_one_out) < 1:
            return 'Wait, what...?'
        else:
            item_type = odd_one_out.pop()
            priority_sum += ord(item_type) - 96 if item_type.islower() else ord(item_type) - 38

    return priority_sum


def exercise2(file):
    rucksacks = open(file, 'r').read().splitlines()
    priority_sum = 0
    for i in range(0, len(rucksacks), 3):
        item_type = set(rucksacks[i]).intersection(set(rucksacks[i+1]).intersection(set(rucksacks[i+2]))).pop()
        priority_sum += ord(item_type) - 96 if item_type.islower() else ord(item_type) - 38
    return priority_sum


print('The sum of the priorities is', exercise1('input.txt'))
print('The sum of the priorities is', exercise2('input.txt'))
