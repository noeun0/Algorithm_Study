import sys
from collections import deque
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    cnt=0
    board = [[0]*(N+1) for i in range(N+1)]

    for _ in range(M):
        a,b = map(int,input().split())
        board[a][b]+=1
        board[b][a]+=1

    queue = deque()
    for x in range(1,N+1):
        if sum(board[x])==0:
            cnt+=1
        if 1 in board[x]:
            queue.append(x)
            cnt+=1
            while queue:
                num = queue.popleft()
                for y in range(N+1):
                    if board[num][y]==1:
                        board[num][y]=x+1
                        queue.append(y)
    print("#{} {}".format(tc, cnt))