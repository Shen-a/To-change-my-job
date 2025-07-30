a, b = input().split()

a_num = a[2]+a[1]+a[0]
a_num = int(a_num)

b_num = b[2]+b[1]+b[0]
b_num = int(b_num)

print(max(a_num, b_num))