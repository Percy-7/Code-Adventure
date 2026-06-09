with open('w1p2.txt') as input:
    puzzle_input: list[str] = [''.join([j for j in i.strip('\n') if j not in [',', '.', '-', "'"]]) for i in input]

# print(puzzle_input[:4])
dict_list = [dict(zip(puzzle_input[i+1], puzzle_input[0])) for i in range(3)]
# sets_list = [{puzzle_input[i+1] for i in range(3)}]
# directions_dict =  dict([(char, i) for i in range(3) for char in puzzle_input[i+1]])
directions_dict =  {char:i for i in range(3) for char in puzzle_input[i+1]}

# print(dict_list[0])

print(directions_dict)