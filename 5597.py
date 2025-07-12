num = []
for i in range(28):
    num.append(int(input()))

num.sort()
num.append(0)
num.append(0)

for i in range(1, 31, 1):
    if i not in num:
        print(i)
