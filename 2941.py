croatia_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cnt=0

word_input = input()

for i in range(len(croatia_alphabet)):
    for _ in range(len(word_input)):
            if  croatia_alphabet[i] in word_input:
                cnt += 1
                
                # print(f"croatia alphabet: {croatia_alphabet[i]}")
                # print(f"cnt: {cnt}")
                
                #replace는 변경이 아닌 문자열 반환이기에 이렇게 다시 받아줄게 필요함.
                # replace 함수는 이렇게 타겟 문자열, 변환될 문자열, 반복횟수 로 구성되어있음 
                word_input = word_input.replace(croatia_alphabet[i], " ", 1)
                
                # print(f"받은 단어: {word_input}")
    
print(cnt)
# print(word_input)

