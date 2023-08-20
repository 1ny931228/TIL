for t in range(1, 11):
    N = int(input())
    str_list = list(input())

    # print(t, N, nums_list)

    stack = []
    postfix = ''

    for str in str_list:
        if not stack and str == '+':
            stack.append(str)
        elif str.isdecimal():
            postfix += str
        elif stack and str == '+' :
            postfix += str

    postfix += '+'
    num_stack =[]

    for ps in postfix:
        if ps != '+':
            num_stack.append(int(ps))
        else:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            num_stack.append(num1+num2)
    print(f'#{t}', *num_stack)
