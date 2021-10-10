from collections import deque
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    M, N, K = map(int, input().split())  # 가로 세로 개수
    board = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        ix, iy = map(int, input().split())
        board[iy][ix] = 1

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque()

    cnt=0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                board[y][x] = 0
                queue.append((y,x))
                while queue:
                    ny,nx = queue.popleft()
                    for i in range(4):
                        cx = nx+dx[i]
                        cy = ny+dy[i]
                        if cx in range(M) and cy in range(N):
                            if board[cy][cx]==1:
                                board[cy][cx] = 0
                                queue.append((cy,cx))


                cnt+=1

    print(cnt)
