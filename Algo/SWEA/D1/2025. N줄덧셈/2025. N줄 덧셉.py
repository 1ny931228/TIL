import sys
sys.stdin = open('input.txt')

N = int(input())
# print(N)
SUM = 0

for n in range(1, N+1):
    SUM += n

print(SUM)