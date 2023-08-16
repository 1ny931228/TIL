import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    input()
    STR = list(input())

    stack = []
    postfix = ''

    for s in STR:
        if not stack and s == '+':
            stack.append(s)
        else:
            postfix += s

    postfix += stack.pop()
    result = []

    for p in postfix:
        if p != '+':
            result.append(int(p))
        else:
            num1 = result.pop()
            num2 = result.pop()
            result.append(num1+num2)

    print(f'#{t}', *result)