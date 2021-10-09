import sys
sys.stdin = open('input.txt')



dr = [0,0,-1,1]
dc = [1,-1,0,0]


def dfs(r,c,a):
    global result
    if len(a)==7:
        result.add(a)
        return


    for idx in range(4):
        if r+dr[idx] in range(4) and c+dc[idx] in range(4):
            #print(a)
            a += board[r+dr[idx]][c+dc[idx]]
            dfs(r+dr[idx],c+dc[idx],a)
            a = a[:-1]


for tc in range(1, int(input())+1):
    result = set()
    board = [[i for i in (input().split())] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            a = ""
            dfs(i,j,a)
    print("#{} {}".format(tc,len(result)))
