T = 10

for t in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))

    count = 0

    for h in range(2, N - 2):
        if height[h] > height[h - 2] and height[h] > height[h - 1] and height[h] > height[h + 1] and height[h] > height[
            h + 2]:
            a1 = height[h] - height[h - 2]
            a2 = height[h] - height[h - 1]
            a3 = height[h] - height[h + 1]
            a4 = height[h] - height[h + 2]

            min_lst = [a1, a2, a3, a4]
            MIN = min(min_lst)
            count += MIN

    print(f'#{t} {count}')