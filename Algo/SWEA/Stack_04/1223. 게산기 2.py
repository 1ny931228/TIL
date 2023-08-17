import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    nums = list(input())

    # print(t, N, nums)

    stack = []
    postfix = ''

    for num in nums:
        if num.isdecimal():
            stack.append(num)
        elif len(stack) >= 2:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if num == '+':
                stack.append(num1 + num2)
            elif num == '*':
                stack.append(num1 * num2)

    print(f'#{t}', *stack)


# N = int(input())
# infix = input()
# postfix = ''
# stack = [0] * N
# top = -1
# icp = {'+': 1, '*': 2}  # 연산자 우선순위
# for i in range(N):
#     if '0' <= infix[i] <= '9':  # 피연산자인 경우
#         postfix += infix[i]
#     else:  # 연산자인 경우
#         if top > -1 and icp[stack[top]] >= icp[infix[i]]:  # stack[top] 우선순위가 같거나 높으면  pop
#             postfix += stack[top]
#             top -= 1
#         top += 1
#         stack[top] = infix[i]
# while top > -1:     # 남아있는 연산자를 수식뒤에 붙임
#     postfix += stack[top]
#     top -= 1
# print(postfix)