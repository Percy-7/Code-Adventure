from re import findall

with open('w3p2.txt') as input:
    spearheads =  [line[0] for line in [findall(r'-\d+|\d+', i) for i in input] if line != []]
    puzzle_input: list[tuple[str, int]] = [(str(i[0]), int(i[1:])) if '-' in i else ('+', int(i)) for i in spearheads]
    # puzzle_input_unsigned = [int(line[0]) for line in [findall(r'\d+', i) for i in input] if line != []]
    puzzle_input_unsigned = [int(i.replace('-','')) for i in spearheads]
    # puzzle_input = [int(line[0]) for line in [findall(r'\d+', i) for i in input] if line != []]

# print(spearheads)
# print(puzzle_input)

size_incomplete_stack: int = len(puzzle_input)
# numbers_set: set[int] = {i[1] for i in puzzle_input}
numbers_set: set[int] = set(puzzle_input_unsigned)
flips_count: int = 0

# print(max(numbers_set))
# print(puzzle_input_unsigned, '!!!!')

flip_dict = {'-': '+', '+': '-'}

def flip(pancakes: list[tuple[str, int]]) -> list[tuple[str, int]]:
    pancakes = [(flip_dict[pancake[0]], pancake[1]) for pancake in pancakes][::-1]
    return pancakes
    # return([sign, number) for sign in pancakes[::-1] for number in pancakes[::-1])

# print(flip([('-', 3), ('+', 2), ('+', 4), ('+', 1)]))

# puzzle_input = [('', 1), ('+', 2), ('+', 3), ('+', 4)]
# puzzle_input_unsigned = [1, 2, 3, 4]

while size_incomplete_stack != 0:
    
    # id_largest_number = puzzle_input.index(max(numbers_set))
    # numbers_set.remove(puzzle_input[id_largest_number])
    id_largest_number = puzzle_input_unsigned.index(max(numbers_set))
    print(puzzle_input, flips_count, size_incomplete_stack, id_largest_number, numbers_set)
    # print(size_incomplete_stack)
    # print(puzzle_input)
    numbers_set.remove(puzzle_input_unsigned[id_largest_number])
    # if id_largest_number == size_incomplete_stack - 1 and puzzle_input[0][0] == '+':
    if id_largest_number == size_incomplete_stack - 1 and puzzle_input[id_largest_number][0] == '+':
        size_incomplete_stack -= 1
        continue
    if id_largest_number != 0:
        # puzzle_input[: id_largest_number + 1] = puzzle_input[: id_largest_number + 1][::-1]
        puzzle_input[: id_largest_number + 1] = flip(puzzle_input[: id_largest_number + 1])
        puzzle_input_unsigned[: id_largest_number + 1] = puzzle_input_unsigned[: id_largest_number + 1][::-1]
        
        flips_count += 1
    if puzzle_input[0][0] == '+':
        puzzle_input[0] = ('-', puzzle_input[0][1])
        flips_count += 1
    
    # puzzle_input[:size_incomplete_stack] = puzzle_input[:size_incomplete_stack][::-1]
    puzzle_input[:size_incomplete_stack] = flip(puzzle_input[:size_incomplete_stack])
    puzzle_input_unsigned[:size_incomplete_stack] = puzzle_input_unsigned[:size_incomplete_stack][::-1]
    size_incomplete_stack -= 1
    flips_count += 1

print(flips_count)
