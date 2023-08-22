for t in range(1, 11):
    N = int(input())
    str_list = list(input())

    stack = []
    postfix = []
    priority = {'+': 1, '*': 2}

    for s in str_list:
        if s.isdecimal():
            postfix.append(s)
        elif not stack:
            stack.append(s)
        elif:
            while stack and priority[stack[-1]] >= priority[s]:
                postfix.append(stack.pop())
            stack.append(s)


    while stack:
        postfix.append(stack.pop())

        