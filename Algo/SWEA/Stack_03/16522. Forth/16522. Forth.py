import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    STR = input().split()

    number = 0
    operation = 0
    # print(STR)
    for s in STR:
        if s.isdecimal():
            number += 1
        elif s == '.':
            pass
        else:
            operation += 1
    # print(STR)
    stack = []

    for s in STR:
        if number == operation + 1: # number > operation라고 하면, 피연산자의 갯수가 압도적으로 많을 때, 안됨. ex) 10 2 3 5 6 7 4 + * .
            if s.isdecimal():
                stack.append(int(s))
            else:
                if len(stack) >= 2:
                    num2 = stack.pop()
                    num1 = stack.pop()

                    if s == '+':
                        stack.append(num1 + num2)
                    elif s == '-':
                        stack.append(num1-num2)
                    elif s == '*':
                        stack.append(num1*num2)
                    elif s == '/':
                        if num2 != 0:
                            stack.append(num1//num2)
                        else:
                            break
                    else:
                        break

        else:
            break


    if len(stack) == 0:
        print(f'#{t} error')
    else:
        print(f'#{t}', *stack)