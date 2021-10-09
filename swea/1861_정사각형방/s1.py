import sys
sys.stdin = open("input.txt")

dr = [0,0,-1,1]
dc = [1,-1,0,0]
def dfs(r,c):
    global schecked
    global checked
    global cnt
    for i in range(4):
        if r+dr[i] in range(N) and c+dc[i] in range(N):

            if board[r+dr[i]][c+dc[i]]-board[r][c]==1 and checked[r+dr[i]][c+dc[i]]==0:
                cnt+=1
                checked[r+dr[i]][c+dc[i]] = 1
                schecked[r + dr[i]][c + dc[i]] = 1
                dfs(r+dr[i],c+dc[i])
                checked[r + dr[i]][c + dc[i]] = 0


for tc in range(1,int(input())+1):
    N = int(input())
    board = [[i for i in map(int,(input()).split())] for _ in range(N)]
    result = 0
    schecked= [[0 for _ in range(N)] for _ in range(N)]
    checked = [[0 for _ in range(N)] for _ in range(N)]
    where = 100000
    for i in range(N):
        for j in range(N):
            if schecked[i][j]==0:
                cnt = 1
                dfs(i,j)

                if cnt > result:
                    result = cnt
                    where = board[i][j]
                elif cnt ==result:
                    where = min(where, board[i][j])

    print("#{} {} {}".format(tc,where, result))

