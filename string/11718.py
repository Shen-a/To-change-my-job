st=1
while st!=0:
    try:
        s=input()
        print(s)
        st=1
    except EOFError:
        st=0
        break
