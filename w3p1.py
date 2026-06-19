from re import findall

with open('w3p1.txt') as input:
    # puzzle_input = [''.join(j for i in input.readlines() for j in i)]
    # puzzle_input = [''.join([j for j in i if j not in ' -\n']) for i in input.readlines()]
    puzzle_input = [int(line[0]) for line in [findall(r'\d+', i) for i in input] if line !=[]]
    # puzzle_input = [list(findall(r'\d+', i) )for i in input]

# print([i for i in puzzle_input if len(i)>1])

size_incomplete_stack: int = len(puzzle_input)
numbers_set = set(puzzle_input)

flips_count = 0

# print(1 in puzzle_input)
# print(sorted(puzzle_input))

while size_incomplete_stack != 0:
    id_largest_number = puzzle_input.index(max(numbers_set))
    print(puzzle_input, flips_count, size_incomplete_stack, id_largest_number, numbers_set)
    # print(puzzle_input)
    # print(size_incomplete_stack)
    numbers_set.remove(puzzle_input[id_largest_number])
    # if puzzle_input == sorted(puzzle_input):
    #     break
    if id_largest_number == len(puzzle_input)-1-(len(puzzle_input)-size_incomplete_stack):
        size_incomplete_stack-=1
        continue
    if id_largest_number != 0:
        puzzle_input[:id_largest_number+1] = puzzle_input[:id_largest_number+1][::-1]
        flips_count+=1
    else:
        pass
    puzzle_input[:size_incomplete_stack] = puzzle_input[:size_incomplete_stack][::-1]
    size_incomplete_stack-=1
    flips_count+=1

print(flips_count)

        


# puzzle_input[0:2] = puzzle_input[0:2][::-1]
# print(puzzle_input)