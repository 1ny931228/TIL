T = int(input())

for t in range(1, T + 1):
    N = list(input())
    # print(t, N)

    stack = [] # 빈 stack을 만들어 괄호 검사를 실시함
    # print(N)
    for i in N:
        if not stack: #빈 stack 경우와 아닌 경우를 나눠서 구현
            if i == '(' or i == '{': # 여는 괄호는 모두 stack에 넣음
                stack.append(i)
            else:
                stack.append(i) # 그외의 것은 모두 stack에 넣지만 괄호가 맞지 않기 때문에 괄호 검사를 종료
                break
        elif stack:
            if i == '(' or i == '{':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(': # 닫는 괄호인 경우는 여는 괄호가 있어야지 stack을 계속 진행하게 함
                    stack.pop()
                else:
                    stack.append(i)
                    break
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
                    break

    # print(stack)
    Plus = []
    if len(stack) == 0:
        result = N



    else:
        result = -1

    print(f'#{t} {result}')