word_arr = []
cnt = 0

n = int(input())

for i in range(n):
    word_arr.append(input())

for i in range(n):
    for j in range(len(word_arr[i])):
        if word_arr[i] in word_arr[i][j]:
            cnt += 1
            word_arr[i] = word_arr[i][j].replace(word_arr[i][j], " ")
            print(f"cnt: {cnt}")
            print(f"word_arr[{i}]: {word_arr[i]}")

print(cnt)