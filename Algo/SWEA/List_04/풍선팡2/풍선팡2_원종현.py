for m in range(int(input())):
    res=0
    N,M=map(int,input().split())
    li=[list(map(int,input().split())) for _ in range(N)]
    for x in range(N):
        for y in range(M):
            t=0
            for dx,dy in [[0,0],[0,1],[0,-1],[1,0],[-1,0]]:
                nx=x+dx
                ny=y+dy
                if 0<=nx<N and 0<=ny<M:
                    t+=li[nx][ny]
                else:
                    continue
            res=max(res,t)
    print(f'#{m+1}',res)