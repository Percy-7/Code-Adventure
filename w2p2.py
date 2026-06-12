from functools import cache
from re import findall

with open('w2p2.txt') as input:
    input_sequence: str = input.read()


@cache
def batches_of_two(count: int, char: str) -> str:
    return f'2{char}' * (count // 2) + f'1{char}' * (count % 2 != 0)


for i in range(10):
    text_chunks = (batches_of_two(len(i), i[0]) for i in findall(r'1+|2+', input_sequence))
    input_sequence = ''.join(text_chunks)


print(input_sequence)
print(len(findall(r'1{3}|2{3}', input_sequence)))