
# n = int(input())
# numarr = list(map(int, input().split()))

# print(min(numarr), end=" ")
# print(max(numarr), end="")



import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

print(min(arr), end=" ")
print(max(arr), end="")