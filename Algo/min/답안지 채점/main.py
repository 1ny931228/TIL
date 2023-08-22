T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # N: 학생의 수, M: 문제의 수
    answer = [list(map(int, input().split())) for _ in range(N+1)]

    # print(t, N, M, answer)

    score = []
    perfect_answer = answer[0]

    # print(perfect_answer)
    for i in range(1, N+1): # 처음에 range를 N+2 했는 데, out of range 나옴.
        correct = 0
        bonus = 0
        for j in range(M):

                if answer[0][j] == answer[i][j]: # list index out of range
                    correct += 1
                    correct += bonus
                    bonus += 1
                else:
                    bonus = 0
        score.append(correct)
        score.sort()

        # print(score)

    result = score[-1] - score[0]

    print(f'#{t} {result}')