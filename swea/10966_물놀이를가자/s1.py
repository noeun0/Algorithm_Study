from collections import deque
import sys
sys.stdin = open("input.txt")

di=[0,0,-1,1]
dj=[1,-1,0,0]

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    checked = [[-1] * M for _ in range(N)]
    board = [[i for i in input()]for _ in range(N)]
    queue=deque()
    result=0
    for i in range(N):
        for j in range(M):
            if board[i][j]=='W':
                queue.append((i,j))
                checked[i][j]=0
    while queue:
        ni,nj=queue.popleft()
        for idx in range(4):
            if ni+di[idx] in range(N) and nj+dj[idx] in range(M):
                if checked[ni+di[idx]][nj+dj[idx]] == -1:
                    queue.append((ni+di[idx],nj+dj[idx]))
                    checked[ni+di[idx]][nj+dj[idx]]=checked[ni][nj]+1

    for i in checked:
        result+=sum(i)

    print("#{} {}".format(tc,result))
