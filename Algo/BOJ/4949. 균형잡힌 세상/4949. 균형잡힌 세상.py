import sys
sys.stdin = open('input.txt')


while True:
    STRS = list(input())
    stack = []

    if STRS == ['.']:
        break
    # print(STRS)
    for i in STRS:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break


    print(stack)
