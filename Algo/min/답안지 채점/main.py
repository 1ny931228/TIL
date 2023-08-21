T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # N: 학생의 수, M: 문제의 수
    answer = [list(map(int, input().split())) for _ in range(N+1)]

    # print(t, N, M, answer)

    bonus = 0
    score = []
    s = 0
    correct = answer[0]

    # print(correct)
    for i in range(1, N):
        for j in range(N):

            # print(answer[i][j])
            if answer[0][j] == answer[i][j]:
                s += 1
                bonus += 1
                s += bonus
            else:
                bonus = 0

        if s > 0:
            score.append(s)

        print(score)







    # score.sort()

    # result = score[-1] - score[0]
    # print(f'#{t} {result}')
