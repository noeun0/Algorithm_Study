import sys
sys.stdin = open('input.txt')

N,M,D = map(int,input().split()) # 행의 수 , 열의 수, 공격거리 제한
board = [[i for i in map(int,input().split())] for i in range(N)]

print(board)
def attack():
    pass

def go():
    pass


while board:
    attack()
    go()