with open('w1.txt') as input:
    puzzle_input: list[str] = [''.join([j for j in i.strip('\n') if j not in [',', '.', '-', "'"]]) for i in input]

backward_dict: dict[str, str] = dict(zip(puzzle_input[1], puzzle_input[0], strict=True))

words: str = ''.join([text[::-1] if i % 2 == 0 else text for i, text in enumerate(puzzle_input[2:])])
words_translated: str = ''.join([backward_dict.get(i, i) for i in words])
words_translated_list: list[str] = words_translated.split()
five_letter_words: list[str] = sorted({i for i in words_translated_list if len(i) == 5})

print(five_letter_words[19])
