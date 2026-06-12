import re
from functools import cache

with open('w2p1.txt') as input:
    input_sequence: str = input.read()

iterations: int = 65

# test_str: str = '1112211'
# print(re.findall(r'1+|2+', test_str))

@cache
def batches_of_two(count: int, char: str) -> str:
    return (f'2{char}'*(count//2)+f'1{char}'*(count%2!=0))


for i in range(iterations):
    text_chunks: list = re.findall(r'1+|2+', input_sequence)
    text_chunks = [batches_of_two(len(i), i[0]) for i in text_chunks]
    input_sequence = ''.join(text_chunks)
    # print(text_chunks)
    print(i)
    
# print(''.join(text_chunks))
print(len(''.join(text_chunks)))


# print(batches_of_two(3,'1'))

# print(repr(input_sequence))