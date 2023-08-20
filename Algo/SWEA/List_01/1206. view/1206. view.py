for t in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))

    good_view = 0

    for i in range(N):
        if height[i] > height[i-1] and height[i] > height[i-2] and height[i] > height[i+1] and height[i] > height[i+2]:
            good_view += height[i] - max(height[i-1], height[i-2], height[i+1], height[i+2])

    print(f'#{t} {good_view}')