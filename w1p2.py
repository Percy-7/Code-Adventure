with open('w1p2.txt') as input:
    puzzle_input: list[str] = [''.join([j for j in i.strip('\n') if j not in [',', '.', '-', "'"]]) for i in input]

puzzle_input[3], puzzle_input[2] = puzzle_input[2], puzzle_input[3]

dict_list = [dict(zip(puzzle_input[i+1], puzzle_input[0])) for i in range(3)]
directions_dict =  {char: 1j**i for i in range(4) for char in puzzle_input[i]}

# print(dict_list)
# print(directions_dict)

