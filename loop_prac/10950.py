
t = input()
t = int(t)

case=[]

for i in range(0,t,1):
    temp, temp1 = input().split()
    temp = int(temp)
    temp1 = int(temp1)
    case.append(temp + temp1)

for i in range(len(case)):
    print(f"{case[i]}")

