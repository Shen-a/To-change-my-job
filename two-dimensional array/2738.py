
n, m = input().split()
n = int(n)
m = int(m)

a_arr = []
b_arr = []

for col in range(n):
    a_arr.append(list(map(int, input().split() ) ) )

for col in range(n):
    b_arr.append(list(map(int, input().split() ) ) )

#circulate
for col in range(len(a_arr)):
    for row in range(len(a_arr[0])):
        a_arr[col][row] += b_arr[col][row]

for col in a_arr:
    for row in col:
        print(row, end=" ")
    print()