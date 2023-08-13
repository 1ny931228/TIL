import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    STRS = list(input())

    stack = []
    result = 0
#print('{} {}'.format(1, 2))
    for strs in STRS:
        if strs == '(' or strs == '{':
            stack.append(strs)
            # print(stack, 1)
        elif strs == '}':
            if stack and stack[-1] == '{':
                stack.pop()
                # print(stack, 2)
            else:
                stack.append(strs)
                # print(stack, 3)
                break
        elif strs == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                # print(stack, 4)
            else:
                stack.append(strs)
                # print(stack, 5)
                break

    if len(stack) == 0:
        result = 1
    # print(stack)
    print(f'#{t} {result}')
