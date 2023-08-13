import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    STRS = list(input())

    # print(t, STRS)

    stack = []

    for STR in STRS:
        if len(stack) == 0:
            stack.append(STR)
        elif len(stack) != 0:
            if stack[-1] == STR:
                stack.pop()
            else:
                stack.append(STR)

    result = len(stack)

    print(f'#{t} {result}')