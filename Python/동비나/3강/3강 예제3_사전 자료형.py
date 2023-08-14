data = dict()
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키 데이터만 담은 리스트
print(data.keys())
print(list(data.keys()))

# 값 데이터만 담은 리스트
print(data.values())

# 각 키에 따른 값을 하나씩 출력
for key in data.keys():
   print(key)