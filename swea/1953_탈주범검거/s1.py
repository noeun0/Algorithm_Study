from collections import deque
import sys
sys.stdin = open("input.txt")

def way(r,c):
    queue =deque()
    queue.append((r,c))
    checked[r][c]=1
    dr=[1,-1,0,0] #하,상,좌,우
    dc=[0,0,-1,1]
    b_pipe=[[1,2,5,6],[1,2,4,7],[1,3,6,7],[1,3,4,5]]
    p_pipe=[[1,2,4,7],[1,2,5,6],[1,3,4,5],[1,3,6,7]]
    while queue:
        v = queue.popleft()
        r,c=v[0],v[1]
        for i in range(4):
            if r+dr[i] in range(N) and c+dc[i] in range(M):
                if checked[r+dr[i]][c+dc[i]]==0:
                    if pipe[r][c] in b_pipe[i] and pipe[r+dr[i]][c+dc[i]] in p_pipe[i]:
                        queue.append([r+dr[i],c+dc[i]])
                        checked[r+dr[i]][c+dc[i]]=checked[r][c]+1

for tc in range(1,int(input())+1):
    N,M,R,C,L = map(int,input().split())
    pipe=[[i for i in map(int,input().split())] for _ in range(N)]
    checked=[[0 for _ in range(M)] for _ in range(N)]
    result=0
    way(R,C)
    for i in checked:
        for j in i:
            if j>0 and j<=L:
                result+=1
    print("#{} {}".format(tc,result))