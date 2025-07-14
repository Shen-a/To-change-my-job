
input_num =[]
calc_num = []
cnt=1
st=0

for i in range(10):
    input_num.append(int(input()))

for i in range(10):
    calc_num.append(input_num[i]%42)

# print(*calc_num)

while st <= 9:
    temp = calc_num[st]
    calc_num.pop(calc_num.index(temp))
    for i in range(8):
        if(temp == calc_num[i]):
            calc_num[calc_num.index(temp)] = []
    calc_num.append(temp)
    st += 1

if(0 in calc_num):
    calc_num =  [v for v in calc_num if v]
    calc_num.append(0)
else:
    calc_num =  [v for v in calc_num if v]

# print(*calc_num)
print(len(calc_num))


