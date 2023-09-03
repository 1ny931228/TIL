book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'


changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0

print(f'{guide}\n{total}\n{changes}\n{total-int(rental)}')