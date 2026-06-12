from functools import cache
from re import findall

with open('w2p1.txt') as input:
    input_sequence: str = input.read()


@cache
def batches_of_two(count: int, char: str) -> str:
    return f'2{char}' * (count // 2) + f'1{char}' * (count % 2 != 0)


for i in range(65):
    text_chunks = [batches_of_two(len(i), i[0]) for i in findall(r'1+|2+', input_sequence)]
    input_sequence = ''.join(text_chunks)

print(len(''.join(text_chunks)))
