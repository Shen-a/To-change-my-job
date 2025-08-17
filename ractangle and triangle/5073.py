st = 1
case = []
temp_2_max = []
len_case = 0

while st!=0:
    a,b,c = map(int, input().split())

    if a==b==c==0:
        st=0
        break
    else:
        x,y,z = sorted([a,b,c])
        print(f"x,y,z = {x}, {y}, {z}")
        if z >= x+y:
            print("Invalid")
        elif x==z:
            print("Equilateral")
        elif x==y or y==z:
            print("Isosceles")
        else:
            print("Scalene")
    x=0
    y=0
    z=0