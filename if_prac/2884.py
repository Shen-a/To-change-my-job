hour, min = input().split()

hour = int(hour)
min = int(min)

min -= 45

if(min<0 and (hour-1)>=0 ):
    print(f"{hour-1} {min+60}")
elif(min<0 and (hour-1)<0 ):
    print(f"23 {min+60}")
elif(min>0):
    print(f"{hour} {min}")
else:
    print(f"{hour} {min}")
