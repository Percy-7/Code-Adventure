from collections import defaultdict
from re import finditer

with open('w5p1.txt') as input:
    puzzle_input: list[str] = [i.strip() for i in input]
    puzzle_input_flattened: str = ''.join(puzzle_input)

length: int = len(puzzle_input[0])
wall_coords: set[complex] = {
    complex(*divmod(i, length)[::-1]) for i in (i.start() for i in finditer(r'[^07]', ''.join(puzzle_input)))
}
broken_walls_directions: defaultdict[complex, list[complex]] = defaultdict(list)

wall_directions: dict[str, frozenset[complex]] = {
    '1': frozenset([1, -1]),
    '2': frozenset([1j, -1j]),
    '3': frozenset([-1, 1j]),
    '4': frozenset([-1, -1j]),
    '5': frozenset([1, -1j]),
    '6': frozenset([1, 1j]),
}

rev_wall_directions: dict[frozenset[complex], str] = {v: k for k, v in wall_directions.items()}


def traverse_grid(wall_type: str, wall_coord: complex, entry_direction: complex) -> None:

    if wall_type == '7':
        broken_walls_directions[wall_coord].append(entry_direction)
        return

    wall_coords.discard(wall_coord)

    exit_direction: complex = next(iter(wall_directions[wall_type] - {entry_direction})) * -1
    new_coords: complex = wall_coord + exit_direction
    traverse_grid(puzzle_input[int(new_coords.imag)][int(new_coords.real)], new_coords, exit_direction)


while wall_coords:
    chosen_coord: complex = next(iter(wall_coords))
    wall_type: str = puzzle_input[int(chosen_coord.imag)][int(chosen_coord.real)]
    entry_direction: complex = next(iter(wall_directions[wall_type]))
    traverse_grid(wall_type, chosen_coord, entry_direction)
    traverse_grid(wall_type, chosen_coord, next(iter(wall_directions[wall_type] - {entry_direction})))

symbols = [rev_wall_directions[frozenset(directions)] for directions in broken_walls_directions.values()]
print(''.join(map(str, [symbols.count(str(i)) for i in range(1, 7)])))
