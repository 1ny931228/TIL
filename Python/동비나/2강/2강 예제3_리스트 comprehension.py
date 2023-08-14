# 0부터9까지의 수를 포함하는 리스트
array = [i for i in range(10)]

print(array)

# 0부터 19까지 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 9)]

print(array)

# comprehension VS 일반적인 코드
array = [i for i in range(20) if i % 2 == 1]

print(array)

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

# 예시
N = 3
M = 5
MAP = [[i] * M for _ in range(N)]