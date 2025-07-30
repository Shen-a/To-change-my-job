alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total_time = 0

word = input()

for i in range(len(word)):
    num = alphabet.index(word[i])
    
    # print(f"word{i} = {word[i]}, num = {num}")

    if (0 <= num <= 2): #ABC
        total_time += 3

    elif (3 <= num <= 5): #DEF
        total_time += 4

    elif (6 <= num <= 8): #GHI
        total_time += 5

    elif (9 <= num <= 11): #JKL
        total_time += 6

    elif (12 <= num <= 14): #MNO
        total_time += 7

    elif (15 <= num <= 18): #PQRS
        total_time += 8

    elif (19 <= num <= 21): #TUV
        total_time += 9
    else:
        total_time += 10
    
    # print(f"Total Time = {total_time}")


print(total_time)
