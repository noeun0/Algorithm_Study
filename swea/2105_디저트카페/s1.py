import sys
sys.stdin = open("input.txt")


def sumf(sr,sc,x,y):
    cnt=0
    check=[]

    for i in range(1, x+1):
        if board[sr+i][sc-i] not in check:
            check.append(board[sr+i][sc-i])
            cnt+=1
        else:
            return -1

    for i in range(1, x+1):
        if sr+i+y in range(N) and sc-i+y in range(N) and board[sr+i+y][sc-i+y] not in check:
            check.append(board[sr+i+y][sc-i+y])
            cnt+=1
        else:
            return -1

    for i in range(y+1):
        if board[sr+i][sc+i] not in check :
            check.append(board[sr+i][sc+i])
            cnt+=1
        else:
            return -1

    for i in range(1,y):
        if sr+i+x in range(N) and sc+i-x in range(N) and board[sr+i+x][sc+i-x] not in check:
            check.append(board[sr+i+x][sc+i-x])
            cnt+=1
        else:
            return -1
    return cnt

for tc in range(1,int(input())+1):

    N = int(input())
    board = [[i for i in map(int,input().split())] for _ in range(N)]
    maxr=-1
    for sr in range(N):
        for sc in range(1,N-1):
            result = 0
            for x in range(1, N):
                if sr+x in range(N-1) and sc-x in range(N):
                    for y in range(1, N):
                        if sr + y in range(N) and sc + y in range(N):
                            maxr=max(maxr,sumf(sr,sc,x,y))
    print("#{} {}".format(tc,maxr))
