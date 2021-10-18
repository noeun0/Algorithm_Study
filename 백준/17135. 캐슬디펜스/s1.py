from itertools import permutations
import sys

sys.stdin = open('input.txt')

# 세개를 선택하는 경우

dx = [-1, 0, 0]
dy = [0, -1, 1]


def choice(n, th):
    global arr
    if len(th) == 3:

        arr.append(th)
        return
    for i in range(M):
        th.append(i)
        choice(n + 1, th)
        th.pop(-1)


def attack():
    # 무조건 앞으로 한칸 가고, 그 후로 왼 오 위
    pass


def go():
    board.pop(-1)


N, M, D = map(int, input().split())  # 행의 수 , 열의 수, 공격거리 제한
board = [[i for i in map(int, input().split())] for i in range(N)]
arr = []
t_list = []
choice(0, t_list)
print(arr)

while 1 in board[-1]:
    go()
