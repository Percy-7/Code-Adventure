with open('w1.txt') as input:
    puzzle_input = [''.join([j for j in i.strip('\n') if j not in [',','.','-', '\'']]) for i in input]

backward_dict: dict[str, str] = dict(zip(puzzle_input[1], puzzle_input[0], strict=True))

words = ''.join([text[::-1] if i%2==0 else text for i, text in enumerate(puzzle_input[2:])])
words_translated = ''.join([backward_dict.get(i,i) for i in words])
words_translated_list = words_translated.split()

five_letter_words = sorted({i for i in words_translated_list if len(i) == 5})
print(five_letter_words[19])

# checked = set()
# count: int = 0
# for i in five_letter_words:
#     if i not in checked:
#         checked.add(i)
#         count+=1
#     if count == 20:
#         print(i)