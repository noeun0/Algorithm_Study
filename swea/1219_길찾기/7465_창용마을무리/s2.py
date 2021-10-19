import sys
sys.stdin = open("input.txt")

def make_set(x):
    p[x] = x
    rank[x] = 0

def find_set(x):
    if p[x]!=x:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1



for tc in range(1, int(input())+1):
    V,E = map(int,input().split())
    cnt=0
    p = [0]*(V + 1)
    rank = [0] * (V + 1)

    for i in range(V+1):
        make_set(i)

    for i in range(E):
        a,b = map(int,input().split())
        union(a,b)
    ans =0
    for i in range(1, V+1):
        if i == p[i]:
            ans+=1
    print("#{} {}".format(tc, ans))



