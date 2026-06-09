with open('w1p2.txt') as input:
    # puzzle_input: list[str] = [''.join([j for j in i.strip('\n') if j not in [',', '.', '-', "'"]]) for i in input]
    puzzle_input: list[str] = [i.strip('\n') for i in input]

puzzle_input[3], puzzle_input[2] = puzzle_input[2], puzzle_input[3]

char_dict = {weird_char: char for i in range(4) for weird_char, char in zip(puzzle_input[i+1], puzzle_input[0]) }
directions_dict =  {char: 1j**i for i in range(4) for char in puzzle_input[i]}

char_grid = puzzle_input[5:]

def in_bounds(coords: complex) -> bool:
    return(coords.real in range(len(char_grid[0])) and coords.imag in range(len(char_grid)))
def get_element(coords:complex) -> str:
    return char_grid[int(coords.imag)][int(coords.real)]

print(char_dict)

pointer: complex = 0+0j
direction: complex = 1j
visited_coords: set = set()

translated_phrase: str = ''
while True:
    current_char = get_element(pointer)
    if current_char == ' ':
        translated_phrase += ' '
        pointer+=direction
        continue
    visited_coords.add(pointer)
    translated_phrase += char_dict.get(current_char, current_char)
    try:
        direction = directions_dict[current_char]
    except KeyError:
        pass
    pointer+=direction
    if not in_bounds(pointer) or pointer in visited_coords:
        break

    print(translated_phrase)

print('\n\n')
print(translated_phrase)