board =[]
max_board = 0
temp_max_board = 0
col = 0
row = 0


for i in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    temp_max_board = max(board[i])

    if(temp_max_board > max_board):
        max_board = temp_max_board
        col = i
        row = board[i].index(max_board)

    temp_max_board = 0
    temp_list_max_board =[]

print(max_board)
print(col+1, end=" ")
print(row+1)


