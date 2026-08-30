import itertools
import re
from collections import defaultdict

with open('w5p1.txt') as input:
    puzzle_input: list[str] = [i.strip() for i in input]
    puzzle_input_flattened: str = ''.join(puzzle_input)

length = len(puzzle_input[0])
wall_coords: set[complex] = {complex(*divmod(i, length)[::-1]) for i in (i.start() for i in re.finditer(r'[^07]', ''.join(puzzle_input)))}

wall_directions: dict[str, tuple[complex, complex]] = {
    '1': (1, -1),
    '2': (1j, -1j),
    '3': (-1, 1j),
    '4': (-1, -1j),
    '5': (1, -1j),
    '6': (1, 1j),
}

complex_to_wasd: dict[complex, str] = {1: 'd', -1 : 'a', 1j: 's', -1j: 'w'}

rev_wall_directions: dict[tuple[str, str], str] = {tuple(sorted(complex_to_wasd[i] for i in v)): k for k,v in wall_directions.items()} # type: ignore

broken_walls_directions: defaultdict[complex, list[str]] = defaultdict(list)

def traverse_grid(wall_type: str, wall_coord: complex, entry_direction: complex):
    print(f'running with {wall_type}, on {wall_coord}, entry with {entry_direction}')
    
    if wall_type == '7':
        print(f'found broken wall at {wall_coord}')
        # broken_walls_directions[wall_coord].append(entry_direction)
        broken_walls_directions[wall_coord].append(complex_to_wasd[entry_direction])
        # print('ran')
        return
    
    wall_coords.discard(wall_coord)
    
    # exit_direction: complex = next(iter(wall_directions[wall_type] - {entry_direction}))*-1
    exit_direction: complex = next(iter(set(wall_directions[wall_type]) - {entry_direction}))*-1
    new_coords = wall_coord + exit_direction
    # traverse_grid(puzzle_input[int(new_coords.real)][int(new_coords.imag)], new_coords, exit_direction)
    traverse_grid(puzzle_input[int(new_coords.imag)][int(new_coords.real)], new_coords, exit_direction)

while wall_coords:
    chosen_coord = next(iter(wall_coords))
    wall_type = puzzle_input[int(chosen_coord.imag)][int(chosen_coord.real)]
    # print((wall_type, chosen_coord, next(iter(wall_directions[wall_type]))))
    entry_direction  = next(iter(wall_directions[wall_type]))
    traverse_grid(wall_type, chosen_coord, entry_direction)
    traverse_grid(wall_type, chosen_coord, next(iter(set(wall_directions[wall_type]) - {entry_direction})))

print(broken_walls_directions)

symbol_map = [(coord, rev_wall_directions[tuple(sorted(directions))]) for coord, directions in broken_walls_directions.items()] # type: ignore

# print(sorted([i[1] for i in symbol_map]))

# print([list(i[1]) for i in itertools.groupby(sorted([i[1] for i in symbol_map]), int)])
# print(list(map(len, [list(i[1]) for i in itertools.groupby(sorted([i[1] for i in symbol_map]), int)])))
print(''.join(list(map(str, (map(len, [list(i[1]) for i in itertools.groupby(sorted([i[1] for i in symbol_map]), int)]))))))