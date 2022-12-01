from collections import Counter


def top_elfs_calories(file, n):
    snacks = open(file, 'r').readlines()
    bags = Counter()
    elf = 0
    for snack in snacks:
        if snack.strip():
            bags[elf] += int(snack)
        else:
            elf += 1
    return sum(calories[1] for calories in bags.most_common(n))


print('Answer to question 1: ', top_elfs_calories('input.txt', 1), 'calories')
print('Answer to question 2: ', top_elfs_calories('input.txt', 3), 'calories')
