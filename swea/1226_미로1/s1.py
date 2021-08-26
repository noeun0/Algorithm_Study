import sys
sys.stdin = open("input.txt")


def bfs(sx, sy):
    global load
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [(sx, sy)]
    while queue:
        sx, sy = queue.pop(0)
        load[sx][sy] = 9
        for i in range(4):
            if (sx + dx[i]) in range(1,15) and (sy + dy[i]) in range(1,15):

                if load[sx + dx[i]][sy + dy[i]] == 0:
                    queue.append((sx + dx[i], sy + dy[i]))
                elif load[sx + dx[i]][sy + dy[i]] == 3:
                    return 1
    return 0

for tc in range(1,11):
    N = int(input())

    load = []
    for _ in range(16):
        load.append(list(map(int,input())))
    print("#{} {}".format(tc,bfs(1,1)))



