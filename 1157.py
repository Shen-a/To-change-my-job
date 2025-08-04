alphabet = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cnt_arr = []
cnt=0
max_cnt = 0
max_index = 0

word = input()
word = word.upper()

for i in range(len(alphabet)):
    for j in range(len(word)):
        if(alphabet[i] == word[j]):
            cnt += 1
    cnt_arr.append(cnt)
    cnt=0

# print(*cnt_arr)

max_cnt = max(cnt_arr)
max_index = cnt_arr.index(max_cnt)
cnt_arr.pop(max_index)

if (max_cnt == max(cnt_arr)):
    print("?")
else:
    print(alphabet[max_index])