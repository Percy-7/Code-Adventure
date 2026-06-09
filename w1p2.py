with open('w1p2.txt') as input:
    puzzle_input: list[str] = [i.strip('\n') for i in input]

puzzle_input[3], puzzle_input[2] = puzzle_input[2], puzzle_input[3]
char_grid: list[str] = puzzle_input[5:]
char_dict: dict[str, str] = {
    weird_char: char for i in range(4) for weird_char, char in zip(puzzle_input[i + 1], puzzle_input[0])
}
directions_dict: dict[str, complex] = {char: 1j**i for i in range(4) for char in puzzle_input[i]}


def in_bounds(coords: complex) -> bool:
    return (coords.real in range(len(char_grid[0])) and coords.imag in range(len(char_grid)))


pointer: complex = 0 + 0j
direction: complex = 1j
visited_coords: set = set()
translated_phrase: str = ''

while in_bounds(pointer) and pointer not in visited_coords:
    current_char: str = char_grid[int(pointer.imag)][int(pointer.real)]
    visited_coords.add(pointer)
    translated_phrase += char_dict.get(current_char, current_char)
    direction = directions_dict.get(current_char, direction)
    pointer += direction

translated_words: list[str] = translated_phrase.split()
print(translated_words[translated_words.index('NAMED') + 1])
