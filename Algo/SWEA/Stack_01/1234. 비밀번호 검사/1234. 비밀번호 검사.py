import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    N, NUMS = input().split()

    # print(N, NUMS)

    n = int(N)
    nums = list(NUMS)

    # print(n, nums)

    stack = []

    for i in nums:
        if not stack:
            stack.append(i)
        elif stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    # print(stack)

    print(f'#{t}', ''.join(stack))