word = input()

cnt = 0

alphabet = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
alphabet_cnt = []

for i in range(len(alphabet)):
    alphabet_cnt.append(word.find(alphabet[i]))

print(*alphabet_cnt)


            
    
