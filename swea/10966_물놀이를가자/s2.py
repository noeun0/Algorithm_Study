from collections import deque
import sys
sys.stdin = open("input.txt")

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    grid = [input() for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0
    while queue:
        oi, oj = queue.popleft()
        for k in range(4):
            ni, nj = oi + di[k], oj + dj[k]
            if ni in range(N) and nj in range(M) and visited[ni][nj] == -1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[oi][oj] + 1
    print(visited)
    result = sum(map(sum, visited))

    print('#{} {}'.format(tc, result))