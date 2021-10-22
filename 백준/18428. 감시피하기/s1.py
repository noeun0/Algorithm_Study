import sys
sys.stdin = open('input.txt')

def choice(cnt, board):
    global anw
    if cnt ==3:
        for i in tlist:
            result=find(i[0],i[1],board)
            if result == False:
                return
        anw = 'YES'
        return

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                choice(cnt+1, board)
                board[i][j] = 'X'

dr = [0,1,-1,0]
dc = [1,0,0,-1]

def find(r,c,board):
    global anw
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        while nr in range(N) and nc in range(N) and board[nr][nc]!='O':
            if board[nr][nc]=='S':
                return False
            nr +=dr[i]
            nc +=dc[i]
    return True


N = int(input())
board = [[i for i in input().split()] for _ in range(N)]
tlist = []
for i in range(N):
    for j in range(N):
        if board[i][j]=='T':
            tlist.append([i,j])
anw="NO"
choice(0,board)
print(anw)