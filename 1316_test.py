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
        # print(f"i: {i} / j: {j}")

        if temp[j] in word_arr[i]:
            st=1
            
            while st != 0:
                index_arr.append(temp.find(temp[j]))
                temp = temp.replace(temp[j], " ",1)
                print(f"temp: {temp}")
                # print(f"index_Arr: {index_arr}")
                
                if "-1" in index_arr: break
                elif "0" in index_arr: break
                else: break

            print(f"index_{word_arr[i]} = ", end="")
            print(*index_arr)

            index_arr=[]

