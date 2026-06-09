with open('w1.txt') as input:
    puzzle_input = [i.strip('\n') for i in input]

backward_dict: dict[str, str] = dict(zip(puzzle_input[1], puzzle_input[0], strict=True))
# words_list = ''.join(puzzle_input[2:]).split()

words = ''.join([text[::-1] if i%2==0 else text for i, text in enumerate(puzzle_input[2:])])
words_translated = ''.join([backward_dict.get(i,i) for i in words])
words_translated_list = words_translated.split()

print(words_translated_list)
# print(puzzle_input[2:])
# print(words)
# print(words_translated)
# print('K' in backward_dict)
# print(words_list)