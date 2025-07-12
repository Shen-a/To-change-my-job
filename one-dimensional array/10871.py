
n, x = map(int, input().split())
numarr = list(map(int, input().split()))

for i in range(n):
    if(numarr[i] < x):
        print(numarr[i], end=" ")


