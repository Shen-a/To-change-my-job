standard_chess_pices = [1, 1, 2, 2, 2, 8]
needs_chess_pices = [0, 0, 0, 0, 0, 0]

current_chess_pices = input().split()
current_arr = list(current_chess_pices)
current_arr = list(map(int, current_arr))

# print(current_arr)

for i in range(6):
    needs_chess_pices[i] = standard_chess_pices[i] - current_arr[i]

print(*needs_chess_pices)

