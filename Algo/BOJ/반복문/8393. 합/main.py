import sys
sys.stdin = open('input.txt')

N = int(input())

SUM = 0

for n in range(N+1):
    SUM += n

print(SUM)
