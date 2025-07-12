result=[]
cnt=0
n=1

while n!=0:
    temp, temp1 = input().split()
    temp = int(temp)
    temp1 = int(temp1)

    if(temp==0 and temp1==0):
        n=0
        break
    else:
        result.append(temp+temp1)
        cnt+=1

for i in range(0, cnt, 1):
    print(f"{result[i]}")
