# 조건문
# - 조건문은 프로그램의 흐름을 제어하는 문법입니다.
# - 조건문을 이용해 조건에 따라서 프로그램의 로직을 설정할 수 있습니다.

# 들여쓰기
# - 파이썬에서는 코드의 블록을 들여쓰기로 지정합니다.

score = 85

if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print('성적이 70점 미만입니다.')
    print('조금 더 분발하세요.')

print('프로그램을 종료합니다.') # if와 상관없이 무조건 실행이 됨.