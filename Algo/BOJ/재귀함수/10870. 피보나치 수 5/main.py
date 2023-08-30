import sys
sys.stdin = open('input.txt')

def pibo(f1, f2, N, cnt):
    if cnt == N:
        print(f1) # 값을 인출했으면 좋겠어
        return
    else:
        f_next = f1 + f2
        pibo(f2, f_next, N, cnt + 1)

N = int(input())

pibo(0, 1, N, 0)