
s = int(input())

for _ in range(s):
    repeat, case = input().split()
    repeat = int(repeat)

    for i in range(len(case)):
        for j in range(repeat):
            if (i == len(case)-1) and (j == repeat-1):
                print(case[i])
            else:
                print(case[i], end="")

