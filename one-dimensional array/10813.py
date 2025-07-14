basket = []
temp = 0

n, m = map(int, input().split())

for i in range(1, n+1, 1):
    basket.append(i)

for cnt in range(1, m+1, 1):
    i, j = map(int, input().split())
    i-=1
    j-=1

    temp = basket[i] 
    basket[i] = basket[j]
    basket[j] = temp

print(*basket)    