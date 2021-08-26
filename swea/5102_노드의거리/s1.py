import sys
sys.stdin = open("input.txt")

def bfs(S):
    queue=[(S,0)]
    while queue:
        a,dis = queue.pop(0)
        if a ==G:
            return dis
        visited[a] =1
        for i in range(1,len(load[a])):
            if load[a][i]==1 and visited[i]==0:
                queue.append((i,dis+1))

    return 0


for tc in range(1,int(input())+1):
    V,E = map(int,input().split()) #v는 노드 #E 는 간선
    load = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited=[0 for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int, input().split())
        load[a][b]+=1
        load[b][a]+=1
    S, G = map(int, input().split())

    print("#{} {}".format(tc, bfs(S)))