case_cnt=int(input())
case=[]

for _ in range(0,case_cnt,1):
    temp = input()
    case.append(temp[0]+temp[-1])

for i in range(case_cnt):
    print(case[i])
