blackboard_word = []
temp_word = []
new_word = []
one_sentence = []
result = ""

for i in range(5):
    blackboard_word.append(list(map(str, input())))

for i in range(5):
    if len(blackboard_word[i]) < 15:
        j = 15 - len(blackboard_word[i])
        for add in range(j):
            blackboard_word[i].append(" ")
        
# print(blackboard_word[1][0])
# print(blackboard_word[2][0])

for j in range(15):
    for i in range(5):
        temp_word.append(blackboard_word[i][j])
        if " " in temp_word:
            temp_word.remove(" ")

    new_word.append(temp_word)
    temp_word = []

for i in new_word:
    for j in i:
        one_sentence.append(j)

result = "".join(one_sentence)
result = result.strip()

print(result)

# 원본
# for j in range(15):
#     for i in range(5):
#         temp_word.append(blackboard_word[i][j])
#     new_word.append(temp_word)
#     temp_word = []

# for i in new_word:
#     for j in i:
#         one_sentence.append(j)

# result = "".join(one_sentence)
# result = result.strip()

# print(result)

