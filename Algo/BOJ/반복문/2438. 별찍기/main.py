import sys
sys.stdin = open('input.txt')

N = int(input())

star = 1
while star <= N:
    print('*' * star)
    star += 1
    if star > N:
        break
