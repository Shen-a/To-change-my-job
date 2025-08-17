case_x=[]
case_y=[]
dist_x = 0
dist_y = 0

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    case_x.append(a)
    case_y.append(b)

# print(f"case_x = {case_x}")
# print(f"case_y = {case_y}")

case_x.sort()
case_y.sort()

dist_x = case_x[-1] - case_x[0]
dist_y = case_y[-1] - case_y[0]

print(dist_x * dist_y)