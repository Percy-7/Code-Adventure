from functools import cache
from re import findall, finditer

with open('w2p2.txt') as input:
    input_sequence: str = input.read()


@cache
def batches_of_two(count: int, char: str) -> str:
    return f'2{char}' * (count // 2) + f'1{char}' * (count % 2 != 0)


for i in range(65):
    text_chunks = (batches_of_two(len(i.group()), i.group()[0]) for i in finditer(r'1+|2+', input_sequence))
    input_sequence = ''.join(text_chunks)
    print(i)


print(len(findall(r'1{3}|2{3}', input_sequence)))
