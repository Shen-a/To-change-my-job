t = int(input())
a=[]
b=[]
result=[]

for i in range(0, t, 1):
    temp, temp1 = input().split()
    temp = int(temp)
    temp1 = int(temp1)
    a.append(temp)
    b.append(temp1)
    result.append(temp+temp1)

for i in range(0, t, 1):
    print(f"Case #{i+1}: {a[i]} + {b[i]} = {result[i]}")
