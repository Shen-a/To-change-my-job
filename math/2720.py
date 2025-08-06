request_cent = []
case = []
recipet_cent = [0, 0, 0, 0]

quarter = 25
dime = 10
nickel = 5
penny = 1


t = int(input())
for i in range(t):
    request_cent.append(int(input())) 

for i in range(t):
    recipet_cent = [0, 0, 0, 0]
    st=1

    while st!=0:
        # print(f"{i+1}th request cent: {request_cent[i]}")
        if(request_cent[i] > 0):
            if request_cent[i]//quarter != 0:
                recipet_cent[0] = request_cent[i]//quarter
                request_cent[i] %= quarter
                # print(f"request cent: {request_cent[i]} / qurter")

            elif request_cent[i]//dime != 0:
                recipet_cent[1] = request_cent[i]//dime
                request_cent[i] %= dime
                # print(f"request cent: {request_cent[i]} / dime")
            
            elif request_cent[i] // nickel != 0:
                recipet_cent[2] = request_cent[i] // nickel
                request_cent[i] %= nickel
                # print(f"request cent: {request_cent[i]} / nickel")
            
            else:
                recipet_cent[3] = request_cent[i] // penny
                request_cent[i] %= penny
                # print(f"request cent: {request_cent[i]} / penny")
        else:
            st=0
    case.append(recipet_cent)
    
# print(*case)

for i in case:
    for j in i:
        print(j, end=" ")
    print()