import sys
sys.stdin = open("input.txt")


def func1(n):
    global result
    if n<=N:
        func1(n*2)
        result= result+tree[n][0]
        func1(n*2+1)

for tc in range(1,11):
    N = int(input())
    tree= [[] for _ in range(N+1)]
    tree_l=[[] for _ in range(N+1)]
    for _ in range(N):
        list_n = list(input().split())
        tree[int(list_n[0])].append(list_n[1])
        tree_l[int(list_n[0])]=list(int(i) for i in list_n[2:])
    result=''
    func1(1)
    print("#{} {}".format(tc,result))

