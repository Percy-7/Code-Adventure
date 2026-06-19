from re import findall

with open('w3p1.txt') as input:
    puzzle_input = [int(line[0]) for line in [findall(r'\d+', i) for i in input] if line != []]

size_incomplete_stack: int = len(puzzle_input)
numbers_set = set(puzzle_input)
flips_count = 0

while size_incomplete_stack != 0:
    id_largest_number = puzzle_input.index(max(numbers_set))
    numbers_set.remove(puzzle_input[id_largest_number])
    if id_largest_number == size_incomplete_stack - 1:
        size_incomplete_stack -= 1
        continue
    if id_largest_number != 0:
        puzzle_input[: id_largest_number + 1] = puzzle_input[: id_largest_number + 1][::-1]
        flips_count += 1
    puzzle_input[:size_incomplete_stack] = puzzle_input[:size_incomplete_stack][::-1]
    size_incomplete_stack -= 1
    flips_count += 1

print(flips_count)
