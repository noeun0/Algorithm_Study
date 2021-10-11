import sys
sys.stdin = open('input.txt')
import itertools


def func(x,y):
    dx = [1,-1,0,0,1,-1,1,-1]
    dy = [0,0,-1,1,1,-1,-1,1]
    for i in range(N):
        if x+dx[i] in range(N) and y+dy[i] in range(N):
            if board[x+dx[i]][y+dy[i]]==1:
                board[x + dx[i]][y + dy[i]]+=1
                break
            else:
                board[x + dx[i]][y + dy[i]]=1
                func(x + dx[i],y + dy[i])


for tc in range(1, int(input())+1):
    N = int(input())
    listQ = list(itertools.combinations(range(N*N),N))
    result=0
    for case in listQ:
        board = [[0 for _ in range(N)] for _ in range(N)]
        count=0
        for Q in case:
            x = Q//N
            y = Q%N

            func(x,y)
            for i in board:
                for j in i:
                    if j==2:
                        count+=1
            if count==0:
                result+=1

    print("#{} {}".format(tc,result))