
hour, min = input().split()
set_time = input()

hour = int(hour)
min = int(min)
set_time = int(set_time)

temp = min + set_time
min = temp%60
hour += temp/60

hour = int(hour)

if(hour >= 24):
    print(f"{hour-24} {min}")
else:
    print(f"{hour} {min}")