word_arr = []
index_arr = []
cnt = 0

n = int(input())

for i in range(n):
    word_arr.append(input())

for i in range(n):
    temp = word_arr[i]
    print(f"{i+1}th temp: {temp}")

    for j in range(len(word_arr[i])):
        index_arr.append(temp.find(temp[j]))
        temp = temp.replace(temp[j], " ")
        # index_arr.append(temp.find(temp[j]))
        # temp = temp.replace(temp[j], " ",1)

        print(f"temp: {temp}")

    print(f"index_Arr: ", end="")
    print(*index_arr)

    if (min(index_arr) != max(index_arr)):
        cnt += 1
        print(f"cnt: {cnt}")
        print(f"temp: {temp}")
    else:
        print(f"{i+1}th word is not that")
    index_arr=[]
print(cnt)