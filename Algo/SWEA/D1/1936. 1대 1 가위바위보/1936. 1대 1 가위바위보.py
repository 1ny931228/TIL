import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())

# print(A, B)

if A == 1 and B == 3:
    print('A')
elif A == 3 and B == 1:
    print('B')
elif A > B:
    print('A')
elif A < B:
    print('B')