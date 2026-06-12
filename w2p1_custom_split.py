from collections.abc import Generator
from functools import cache
from re import findall

# from re import findall, finditer

# with open('w2p2.txt') as input:
#     input_sequence: str = input.read()




def split(sequence: Generator[str]):
    current_char: str = next(sequence)
    count: int = 1
    
    for char in sequence:
        # count = 0
        # print(char, current_char, count)
        if count == 2:
            # yield (count, current_char, 'yikes')
            # yield (count, current_char)
            yield str(count)
            yield current_char
            # yield current_char*count
            current_char = char
            count = 1
            continue
        
        if current_char == char:
            count+=1
            current_char = char
            # yield 'what'
        else:
            # yield (count, current_char)
            yield str(count)
            yield current_char
            # yield current_char*count
            count = 1
            current_char = char
    # yield (count, current_char)
    yield str(count)
    yield current_char
    # yield current_char*count

 
@cache
def batches_of_two(count: int, char: str) -> str:
    return f'2{char}' * (count // 2) + f'1{char}' * (count % 2 != 0)

# input_sequence: Generator[str] = (i for i in '121')



# input_sequence: Generator[str] = (i for i in '11212')
input_sequence: Generator[str] = (i for i in '12111112121112111212212112111212')



# # print([i for i in split(input_sequence)])

for i in range(65):
    input_sequence = (i for i in split(input_sequence))
    print(i)

print('loop done!')
    # print(i)

# print(str(input_sequence))
# print(len(findall(r'1{3}|2{3}', ''.join(input_sequence))))
# print(sum(1 for _ in input_sequence))


def compress(sequence: Generator[str]):
    current_char: str = next(sequence)
    count: int = 1
    
    for char in sequence:
        # count = 0
        # print(char, current_char, count)
        
        if current_char == char:
            count+=1
            current_char = char
            # yield 'what'
        else:
            yield (count, current_char)
            # yield str(count)
            # yield current_char
            # yield current_char*count
            count = 1
            current_char = char
    yield (count, current_char)
    # yield str(count)
    # yield current_char

# print([i for i in compress(input_sequence)])
# print(sum(i[0] for i in compress(input_sequence)))
print(sum(i[0]==3 for i in compress(input_sequence)))

# repetitions = 1
# count = 0

# input_sequence: Generator[str] = (i for i in '11121')

# current_char: str = next(input_sequence)
# for char in input_sequence:
#     # print(char, current_char, repetitions)
    
#     if char == current_char:
#         repetitions += 1
#     else:
#         if repetitions == 3:
#             count += 1
#         current_char = char
#         repetitions = 1
#     # if repetitions > 3:
#     #     count -=1

# print(count)

# print(''.join(input_sequence))
# print(len(list(input_sequence)))

# for i in range(65):
#     text_chunks = (batches_of_two(len(i.group()), i.group()[0]) for i in finditer(r'1+|2+', input_sequence))
#     input_sequence = ''.join(text_chunks)
#     print(i)


# print(len(findall(r'1{3}|2{3}', input_sequence)))


# string_generator: Generator[str] = (i for i in '112133')
# string_generator: Generator[str] = (i for i in '1221112221221211221221212211221112212211222111221211')



# print([i for i in split(string_generator)])
# print(''.join([str(i[0])+i[1] for i in split(string_generator)]))