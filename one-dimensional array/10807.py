cnt=0

n = int(input())
num = list(map(int, input().split()))
v = int(input())

for i in range(0,n,1):
    if(num[i] == v):
        cnt+=1


print(cnt)
