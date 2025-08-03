cnt = int(input())
cnt = cnt*2-1

for i in range(cnt // 2 + 1):
    spaces = ' ' * (cnt // 2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

for i in range(cnt // 2 - 1, -1, -1):
    spaces = ' ' * (cnt // 2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

    