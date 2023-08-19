array = [3, 5, 1, 2, 4] #5개의 데어터(N=5)
summary = 0 # 합계를 저장할 변수

# 모든 데이터를 하나씩 확인하며 합계를 계산
for i in array:
    summary += i

print(summary)

for i in range(len(array)):
    summary += array[i]

# 결과를 출력
print(summary)