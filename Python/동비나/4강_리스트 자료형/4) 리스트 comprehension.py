# - 리스트를 초기화하는 방법 중 하나입니다.
#   - 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있습니다.
# - 리스트 comprehension은 2차원 리스트를 초기화할 때 효과적으로 사용될 수 있습니다.
# - 특히 N*M 크기의 2차원 리스트를 한번에 초기화 해야할 때 매우 유용합니다.
#   - 좋은 예시 : array = [[0] * m for _ in range(n)]
# - 만약 2차원 리스트를 초기화할 때 다음과 같이 작성하면 예기치 않은 결과가 나올 수 있습니다.
#   - 잘못된 예시 : array = [[0] * m] * n]
#   - 위 코드는 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식 됩니다.

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