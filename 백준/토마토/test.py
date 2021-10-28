import sys
from collections import deque
sys.stdin = open('input.txt')

M, N, H = map(int, sys.stdin.readline().split())
tomatos = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]


def check(tomatos):
    global M, N, H
    for h in range(H):
        for x in range(N):
            if 0 in tomatos[h][x]:
                return 'ok'

    else:
        return 'error'




def days(tomatos):
    global M, N, H
    dist = [[[-1] * M for _ in range(N)] for _ in range(H)]
    ans = 0
    dq = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dh = [-1, 1]

    for h in range(H):
        for x in range(N):
            for y in range(M):
                if tomatos[h][x][y] == 1 and dist[h][x][y] == -1:
                    dist[h][x][y] += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if dist[h][nx][ny] == -1 and tomatos[h][nx][ny] == 0:
                                tomatos[h][nx][ny] += 1
                                dq.append([h, nx, ny])
                                dist[h][nx][ny] = dist[h][x][y] + 1

                    for k in range(2):
                        nh = h + dh[k]
                        if 0 <= nh < H:
                            if dist[nh][x][y] == -1 and tomatos[nh][x][y] == 0:
                                tomatos[nh][x][y] += 1
                                dq.append([nh, x, y])
                                dist[nh][x][y] = dist[h][x][y] + 1

    while dq:
        z, i, j = dq.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if dist[z][nx][ny] == -1 and tomatos[z][nx][ny] == 0:
                    tomatos[z][nx][ny] += 1
                    dq.append([z, nx, ny])
                    dist[z][nx][ny] = dist[z][i][j] + 1

        for k in range(2):
            nz = z + dh[k]
            if 0 <= nz < H:
                if dist[nz][i][j] == -1 and tomatos[nz][i][j] == 0:
                    tomatos[nz][i][j] += 1
                    dq.append([nz, i, j])
                    dist[nz][i][j] = dist[z][i][j] + 1

    for i in range(H):
        for j in range(N):
            if 0 in tomatos[i][j]:
                return -1

            elif ans < max(dist[i][j]):
                ans = max(dist[i][j])
    else:
        return ans

if check(tomatos) == 'error':
    print(0)
else:
    print(days(tomatos))