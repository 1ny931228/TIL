for t in range(1, 11):
    N = int(input())
    str_list = list(input())

    # print(t, N, str_list)

    stack = []
    postfix = ''
    priority = {'+': 1, '*': 2}

    for s in str_list:
        if s.isdecimal():
            postfix += s
        elif not stack:
            stack.append(s)
        else:
            while stack and priority[stack[-1]] >= priority[s]:
                postfix += stack.pop()
            stack.append(s)

    while stack:
        postfix += stack.pop() # stack에 부호가 몇개 남아있는 지 모르니, 반복문을 써줌

    num_list = []

    for ps in postfix:
        if ps.isdecimal():
            num_list.append(int(ps))
        elif ps == '*':
            num2 = num_list.pop()
            num1 = num_list.pop()
            num_list.append(num1 * num2)
        elif ps == '+':
            num2 = num_list.pop()
            num1 = num_list.pop()
            num_list.append(num1 + num2)

    print(f'#{t}', *num_list)

