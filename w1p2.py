with open('w1p2.txt') as input:
    # puzzle_input: list[str] = [''.join([j for j in i.strip('\n') if j not in [',', '.', '-', "'"]]) for i in input]
    puzzle_input: list[str] = [i.strip('\n') for i in input]

puzzle_input[3], puzzle_input[2] = puzzle_input[2], puzzle_input[3]

dict_list = [dict(zip(puzzle_input[i+1], puzzle_input[0])) for i in range(3)]
# dict_list = dict(*dict(zip(puzzle_input[i+1], puzzle_input[0])) for i in range(3))
char_dict = {weird_char: char for i in range(3) for weird_char, char in zip(puzzle_input[i+1], puzzle_input[i]) }
print(char_dict)

# dict_list = {puzzle_input[i+1]: puzzle_input[0] for i in range(3)}
# test= {**d for d in dict_list}
directions_dict =  {char: 1j**i for i in range(4) for char in puzzle_input[i]}

# print(dict_list)
# print(directions_dict)

char_grid = puzzle_input[5:]

def in_bounds(coords: complex) -> bool:
    return(coords.real in range(len(char_grid[0])) and coords.imag in range(len(char_grid)))
def get_element(coords:complex) -> str:
    return char_grid[int(coords.imag)][int(coords.real)]

pointer: complex = 0+0j
direction: complex = 1j
visited_coords: set = set()

# translated_phrase: str = ''
# while True:
#     visited_coords.add(pointer)
#     translated_phrase += dict_list.get(get_element(pointer), get_element(pointer))

# print(dict_list)