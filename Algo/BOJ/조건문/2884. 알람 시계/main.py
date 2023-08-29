import sys
sys.stdin = open('input.txt')

H, M = map(int, input().split())

# print(H, M)

if 45 <= M < 60:
     M -= 45
elif 0 <= M < 45:
    M = 60 - (45 - M)
    if H != 0:
        H -= 1
    elif H == 0:
        H = 24 + (H - 1)


print(H, M)
