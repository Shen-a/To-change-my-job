temp = []
final_n = 0

n, b = input().split()

n = list(n)
for i in range(len(n)):
    if (n[i].isdecimal()):
        n[i] = int(n[i])
    else:
        n[i] = int(ord(n[i]))
# print(n)

b = int(b)

for i in range(len(n)):
    if n[i] > 9:
        temp.append((n[i]-55)*(b**(len(n)-i-1)))
    else:
        temp.append(n[i]*(b**(len(n)-i-1)))

# print(temp)

for i in range(len(n)):
    final_n += temp[i]
temp = []

print(final_n)