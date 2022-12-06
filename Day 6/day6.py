
def exercise(file, distance):
    datastream_buffer = open(file, 'r').readline()
    sequence_unique = set()
    sequence = ''
    processed_chars = 0
    for char in datastream_buffer:
        processed_chars += 1
        prev_seq_len = len(sequence_unique)
        sequence_unique.add(char)
        sequence += char
        if len(sequence_unique) == prev_seq_len:
            sequence = update_sequence(sequence_unique, sequence, char)
        if len(sequence_unique) == distance:
            break
    return processed_chars


def update_sequence(sequence_set, sequence, dupe):
    dupe_idx = sequence.index(dupe)
    for char in sequence[:dupe_idx+1]:
        sequence_set.remove(char)
    sequence_set.add(dupe)
    return sequence[dupe_idx+1:]


print(exercise('input.txt', 4), ' characters need to be processed.')
print(exercise('input.txt', 14), ' characters need to be processed.')
