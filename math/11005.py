temp = []
st=1
ans=[]
len_temp = 0

n, b = input().split()
b = int(b)
n = int(n)

while st!=0:
    if(n//b == 0 and n%b==0):
        st=0
        break
    else:
        temp.append(n%b)
        n = n//b

temp.reverse()
len_temp = len(temp)

for i in range(len_temp):
    if (temp[i] > 9):
        ans.append(chr(temp[i]+55))
    else:
        ans.append(str(temp[i]))

for i in ans:
    print(i, end="")
