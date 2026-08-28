import re

with open('w5p1.txt') as input:
    puzzle_input: list[str] = [i.strip() for i in input]
    # puzzle_input_flattened: str = input.read().replace('\n', '')
    puzzle_input_flattened: str = ''.join(puzzle_input)

length = len(puzzle_input[0])
# wall_coords = re.findall(r'[^0]', puzzle_input_flattened)
# wall_coords: list = [complex(*divmod(i, 5)) for i in (i.start() for i in re.finditer(r'[^07]', ''.join(puzzle_input)))]
wall_coords: list = [complex(*divmod(i, 5)[::-1]) for i in (i.start() for i in re.finditer(r'[^07]', ''.join(puzzle_input)))]
# wall_coords: list = [complex(*divmod(i, 5)) for i in (i.start() for i in re.finditer(r'[^07]', ''.join(puzzle_input)))]

# wall_directions: dict[str, set[complex]] = {
#     '1': {1, -1},
#     '2': {1j, -1j},
#     '3': {-1, -1j},
#     '4': {1j, -1},
#     '5': {1, 1j},
#     '6': {1, -1j},
# }

wall_directions: dict[str, set[complex]] = {
    '1': {1, -1},
    '2': {1j, -1j},
    '3': {-1, 1j},
    '4': {-1j, -1},
    '5': {1, -1j},
    '6': {1, 1j},
}

# print(wall_directions)
# print(wall_coords)
# print(puzzle_input)

broken_coords: list[complex] = []

def traverse_grid(wall_type: str, wall_coord: complex, entry_direction: complex):
    print(f'running with {wall_type}, on {wall_coord}, entry with {entry_direction}')
    
    
    current_coord = wall_coord
    
    if wall_type == '7':
        print(f'found broken wall at {wall_coord}')
        broken_coords.append(wall_coord)
        return
    
    try:
        wall_coords.remove(wall_coord)
    except ValueError:
        print('fucked at', wall_type, wall_coord, entry_direction)
        raise ValueError
    
    if entry_direction not in wall_directions[wall_type]:
        raise NotImplementedError
    
    exit_direction: complex = next(iter(wall_directions[wall_type] - {entry_direction}))*-1
    # new_coords = wall_coord + entry_direction + exit_direction
    new_coords = wall_coord + exit_direction
    # traverse_grid(puzzle_input[int(new_coords.real)][int(new_coords.imag)], new_coords, exit_direction)
    traverse_grid(puzzle_input[int(new_coords.imag)][int(new_coords.real)], new_coords, exit_direction)
    # print(exit_direction)
    
    
    # traverse_grid()
# print(traverse_grid('1', 1, 1))

# print(wall_coords)

while wall_coords:
    chosen_coord = wall_coords[0]
    # wall_type = puzzle_input[int(chosen_coord.real)][int(chosen_coord.imag)]
    wall_type = puzzle_input[int(chosen_coord.imag)][int(chosen_coord.real)]
    # if wall_type != '7':
    #     print((wall_type, chosen_coord, next(iter(wall_directions[wall_type]))))
    #     traverse_grid(wall_type, chosen_coord, next(iter(wall_directions[wall_type])))
    # else:
    #     print('stupid')
    try:
        print((wall_type, chosen_coord, next(iter(wall_directions[wall_type]))))
        traverse_grid(wall_type, chosen_coord, next(iter(wall_directions[wall_type])))
    except KeyError:
        print(wall_type, chosen_coord)
        raise KeyError

print(broken_coords)