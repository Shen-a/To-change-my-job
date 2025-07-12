t = int(input())
result=[]

for i in range(0, t, 1):
    temp, temp1 = input().split()
    temp = int(temp)
    temp1 = int(temp1)
    result.append(temp+temp1)

for i in range(0, t, 1):
    print(f"Case #{i+1}: {result[i]}")
