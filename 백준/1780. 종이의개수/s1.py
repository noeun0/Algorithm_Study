import sys
sys.stdin = open('input.txt')

def findp(board,N):
    for i in range(0, N, N // 3):
        for j in range(0, N, N // 3):
            paper = set()
            paperlist = []
            for turn in range(N // 3):
                paper = paper | set(board[i + turn][j:j + N // 3])
                paperlist.append(board[i + turn][j:j + N // 3])
            if len(paper) == 1:
                cnt[paper.pop() + 1] += 1
            else:
                findp(paperlist, N // 3)


N = int(input())
board = [[i for i in map(int,input().split())] for i in range(N)]
cnt = [0,0,0]

all=set()
for i in range(N):
    all = all | set(board[i])
if len(all)==1:
    cnt[all.pop() + 1] += 1
    for i in cnt:
        print(i)

else:
    findp(board,N)

    for i in cnt:
        print(i)