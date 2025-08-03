st=1

string_input = input()
string_div_by_2 = int(len(string_input)/2)

# print(f"len: {string_div_by_2}")

if string_input[0] == string_input[-1]:
    for i in range(1,string_div_by_2,1):
        if(string_input[i] != string_input[-i-1]):
            print("0")
            st=0
            break
    if st==1:
        print("1")
else:
    print("0")


