
def get_commands_and_outputs(file):
    return open(file).read().splitlines()


def get_dir_tree(file):
    commands_and_outputs = get_commands_and_outputs(file)
    current_dir = list()
    dir_tree = dict()
    for line in commands_and_outputs:
        if line[0] == '$':
            if line[2:5] == 'cd ':
                if line[5:] == '..':
                    current_dir.pop()
                else:
                    current_dir.append(line[5:])
        else:
            if len(dir_tree) == 0:
                dir_tree[(current_dir[-1], None)] = list()
            elif (current_dir[-1], tuple(current_dir[:-1])) not in dir_tree and current_dir[-1] != '/':
                dir_tree[(current_dir[-1], tuple(current_dir[:-1]))] = list()
            if current_dir[-1] == '/':
                dir_tree[(current_dir[-1], None)].append(line)
            else:
                dir_tree[(current_dir[-1], tuple(current_dir[:-1]))].append(line)
    return dir_tree


def get_dir_size(dir_tree, current_dir, parents):
    size = 0
    for element in dir_tree[(current_dir, parents)]:
        if element[:4] == 'dir ':
            if parents is None:
                new_parents = [current_dir]
            else:
                new_parents = list(parents)
                new_parents.append(current_dir)
            size += get_dir_size(dir_tree, element[4:], tuple(new_parents))
        else:
            size += int(element.split(' ')[0])
    return size


def count_dir_sizes(dir_tree, max_size):
    sizes = list()
    for key in dir_tree.keys():
        dir_size = get_dir_size(dir_tree, key[0], key[1])
        if dir_size <= max_size:
            sizes.append(dir_size)
    return sum(sizes)


def find_dir_to_delete(dir_tree, total_space, unused_space_needed):
    sizes = list()
    used_space = 0
    for i, key in enumerate(dir_tree.keys()):
        if i == 0:
            used_space = get_dir_size(dir_tree, key[0], key[1])
            dir_size = used_space
        else:
            dir_size = get_dir_size(dir_tree, key[0], key[1])
        if (total_space - used_space) + dir_size >= unused_space_needed:
            sizes.append(dir_size)
    return min(sizes)


print('The sum of the total sizes of the directories is ', count_dir_sizes(get_dir_tree('input.txt'), 100000))
print('The total size of that directory is ', find_dir_to_delete(get_dir_tree('input.txt'), 70000000, 30000000))
