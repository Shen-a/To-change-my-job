
hour, min = input().split()

hour = int(hour)
min = int(min)

if(hour == 0 and min >= 45):
    print(f"0 {min-45}")
elif(hour == 0 and min <= 45):
    print(f"23 {(min-45)+60}")
elif(min >= 45):
    print(f"{hour} {min-45}")
else:
    print(f"{hour-1} {(min-45)+60}")
