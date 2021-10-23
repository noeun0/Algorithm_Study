import sys
sys.stdin = open('input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):
    global exit1
    global exit2
    queue = []
    queue.append((r,c,0))
    while queue:
        i = queue.pop(0)
        nr,nc,cnt = i[0],i[1],i[2]
        if board[nr][nc] == 1:
            exit1.append([cnt,nr,nc])
        for idx in range(4):
            if nr+dr[idx] in range(N) and nc+dc[idx] in range(N):
                if not checked[nr+dr[idx]][nc+dc[idx]]:
                    checked[nr + dr[idx]][nc + dc[idx]]=1
                    queue.append((nr+dr[idx],nc+dc[idx],cnt+1))

def find(t1,t2):
    global result
    time1= sorted(t1)
    time2= sorted(t2)
    result1=0
    result2=0
    for i in time1:
        if result1<=i:
            result1 = i+1
        else:
            result1+=1
    for i in time2:
        if result2<=i:
            result2 = i+1
        else:
            result2+=1
    result = min(result,(max(result1,result2)))

def choice(cnt,t1,t2):
    global result
    if cnt == lenx:
        find(t1,t2)
        return
    for i in range(2):
        if i == 0:
            t1.append(exitlist[i][cnt][0])
            choice(cnt+1, t1, t2)
            t1.pop(-1)
        else:
            t2.append(exitlist[i][cnt][0])
            choice(cnt+1, t1, t2)
            t2.pop(-1)

for tc in range(1,int(input())+1):

    N = int(input())
    board = [[i for i in map(int,input().split())] for _ in range(N)]
    cnt=0
    num=0
    exitlist=[]
    checked=[[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]==2:
                exit1 = []
                checked = [[0] * N for i in range(N)]
                bfs(i,j)
                exitlist.append(exit1)
    exitlist[0].sort(key = lambda x : x[2])
    exitlist[0].sort(key = lambda x: x[1])
    exitlist[1].sort(key = lambda x: x[2])
    exitlist[1].sort(key = lambda x: x[1])

    lenx=len(exitlist[0])
    result = 100000
    choice(0,[],[])
    print("#{} {}".format(tc,result))