import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    input()
    NUMS = list(map(int, input().split('+')))

    # print(t, NUMS)

    # 숫자만 뽑아서, result에 값을 더해주자!

    result = 0

    for num in NUMS:
        result += num

    print(f'#{t} {result}')