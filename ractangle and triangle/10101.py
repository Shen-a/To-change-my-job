
a = int(input())
b = int(input())
c = int(input())

# print(a,b,c)

if a+b+c > 180 or a+b+c < 180:
    print("Error")
elif (a+b+c == 180) and (a==b and b==c and a==c):
    print("Equilateral")
elif (a+b+c == 180) and (a==b or b==c or a==c):
    print("Isosceles")
elif (a+b+c == 180) and (a!=b and b!=c and a!=c):
    print("Scalene")