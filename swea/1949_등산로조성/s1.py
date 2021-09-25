import sys
sys.stdin = open("input.txt")



def scmap(i,j,height,cnt,chance):
    global checked
    global result
    result = max(result, cnt)

    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    for idx in range(4):
        if i+di[idx] in range(N) and j+dj[idx] in range(N) and checked[i+di[idx]][j+dj[idx]]==0:
            if load[i+di[idx]][j+dj[idx]]<height:
                checked[i + di[idx]][j + dj[idx]] = 1
                scmap(i+di[idx],j+dj[idx],load[i+di[idx]][j+dj[idx]],cnt+1,chance)
                checked[i + di[idx]][j + dj[idx]] = 0
            elif chance==0:
                for mi in range(1,K+1):

                    if load[i+di[idx]][j+dj[idx]]-mi<height:
                        checked[i + di[idx]][j + dj[idx]] = 1
                        scmap(i+di[idx], j+dj[idx], load[i+di[idx]][j+dj[idx]]-mi, cnt+1, chance+1)
                        checked[i + di[idx]][j + dj[idx]] = 0


for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    load=[]
    result=0
    start=0

    for _ in range(N):
        load_line=list(map(int,input().split()))
        start=max(max(load_line),start)
        load.append(load_line)

    for i in range(N):
        for j in range(N):
            if load[i][j]==start:
                checked = [[0 for _ in range(N)] for _ in range(N)]
                checked[i][j] += 1
                scmap(i,j,start,1,0)
    print("#{} {}".format(tc,result))
