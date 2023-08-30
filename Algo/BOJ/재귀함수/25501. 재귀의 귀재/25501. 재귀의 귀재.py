import sys
sys.stdin = open('input.txt')

T = int(input())
cnt = 0

def isPanlindrome(s, e, STR):
    if STR[s] != STR[e]:
        return 0
    elif STR[s] == STR[e]:
        s += 1
        e -= 1
        isPanlindrome(s, e)

# def recursion():

for t in range(T):
    STR = list(input())
    print(STR)
    print(isPanlindrome(0, -1, STR))