# - 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue를 사용합니다.
# - 1부터 9까지의 홀수의 합을 구할 때 다음과 같이 작성할 수 있습니다.

result = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i
print(result)