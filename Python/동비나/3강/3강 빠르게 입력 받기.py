# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있습니다.
# 파이썬의 경우 sys 라이브러리에 정의되어 있는  sys.stdin.readline()메서드를 이용합니다.
# 단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip()메서드를 함께 사용합니다.

import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)

# 출력할 변수들
 a = 1
 b = 2
 print(a, b)
 print(7, end=" ")
 print(8, end=" ")

 # 출력할 변수
 answer = 7
 print("정답은" + str(answer) + "입니다.")
 print(f'정답은 {answer}입니다.')