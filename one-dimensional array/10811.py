basket=[]
temp=[]

n, m = map(int, input().split())



for cnt in range(1,n+1,1):
    basket.append(cnt)

for cnt in range(m):

    i, j = map(int, input().split())
    
    i-=1

    for n in range(i, j, 1):
        temp.append(basket.pop(i))

    temp.reverse()
    

    for n in range(i, j, 1):
        basket.insert(n, temp.pop(0))

    # print(f"temp: {temp}")
    # print(f"basket: {basket}")
    # print(f"reverse temp: {temp}")
    # print(f"after basket: {basket}")

print(*basket)



