T = int(input())

for t in range(1, T+1):
    s = list(input())

    new_s = []

    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            new_s.append(s[i])
            print(new_s)
        else:
            new_s.pop()
            print(new_s)


-.-----------


T = int(input())

for t in range(1, T+1):
    s = list(input())

    new_s = [s[0]]  # 최소한 첫 번째 문자는 추가되어야 합니다.

    for i in range(1, len(s)):
        if s[i] != s[i-1]:  # 이전 문자와 다르면 추가
            new_s.append(s[i])

    result = len(new_s)
    print(f'#{t} {result}')