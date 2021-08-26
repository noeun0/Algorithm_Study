import sys
sys.stdin = open("input.txt")


def bfs(sx, sy):
    global load
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [(sx, sy,0)]
    while queue:
        sx, sy, dis = queue.pop(0)
        load[sx][sy] = 5
        for i in range(4):
            if (sx + dx[i]) in range(N) and (sy + dy[i]) in range(N):
                if load[sx + dx[i]][sy + dy[i]] == 0:
                    queue.append((sx + dx[i], sy + dy[i], dis+1))
                elif (sx + dx[i])==ex and (sy + dy[i])==ey:
                    return dis
    return 0

for tc in range(1,int(input())+1):
    N = int(input())
    load = []
    for _ in range(N):
        load.append(list(map(int,input())))
    for i in range(N):
        for j in range(N):
            if load[i][j]==2:
                sx,sy = i,j

            elif load[i][j]==3:
                ex,ey= i,j

    print("#{} {}".format(tc,bfs(sx,sy)))




