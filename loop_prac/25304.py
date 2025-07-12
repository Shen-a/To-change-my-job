
total_price = int(input())
kind = int(input())
receipt = 0

for i in range(0, kind, 1):
    price, cnt = input().split()
    price = int(price)
    cnt = int(cnt)
    receipt += (price * cnt)

'''print(f"{receipt}")'''

if(total_price == receipt):
    print("Yes")
else:
    print("No")