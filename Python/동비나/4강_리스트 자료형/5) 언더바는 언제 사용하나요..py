# - 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할때, 언더바(_)를 자주 사용합니다.

# 코드 1부터 9까지의 자연수를 더하기
SUM = 0
for i in range(1, 10):
    SUM += i
print(SUM)

# 코드 2: "Hello World"를 5번 출력하기
for _ in range(5):
    print("Hello World")